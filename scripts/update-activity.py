#!/usr/bin/env python3
"""Refresh README Activity column with full ISO dates from GitHub.

Priority per repo:
  1) latest GitHub Release published_at  -> kind=release
  2) latest git tag commit/tagger date   -> kind=tag
  3) latest commit committer date        -> kind=commit

Requires: GitHub CLI (`gh`) authenticated (`gh auth login`).

Usage:
  python3 scripts/update-activity.py
  python3 scripts/update-activity.py --readme README.md --data data/activity.json
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

GITHUB_URL_RE = re.compile(r"https://github\.com/([^/\s\)]+)/([^/\s\)#]+)")
SHIELDS_OR_DATE_RE = re.compile(
    r"(?:"
    r"\[!\[[^\]]*\]\(https://img\.shields\.io/github/[^)]+\)\]\([^)]+\)"
    r"|"
    r"\[[0-9]{4}-[0-9]{2}-[0-9]{2}\]\([^)]+\)(?:<br>`?(?:release|tag|commit)`?)?"
    r"|"
    r"`?[0-9]{4}-[0-9]{2}-[0-9]{2}`?(?:<br>`?(?:release|tag|commit)`?)?"
    r")"
)


def gh_api(path: str, jq: str | None = None) -> tuple[int, str, str]:
    cmd = ["gh", "api", path]
    if jq:
        cmd += ["--jq", jq]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def fetch_activity(owner: str, repo: str) -> dict:
    code, out, err = gh_api(
        f"repos/{owner}/{repo}/releases/latest",
        '.tag_name + "\\t" + .published_at',
    )
    if code == 0 and out:
        tag, _, published = out.partition("\t")
        return {
            "owner": owner,
            "repo": repo,
            "kind": "release",
            "ref": tag,
            "date": (published or "")[:10],
        }

    code, tag, err = gh_api(f"repos/{owner}/{repo}/tags?per_page=1", ".[0].name // empty")
    if code == 0 and tag:
        date = None
        # Prefer commit metadata behind the tag name via commits API on the tag ref
        code2, commit_date, _ = gh_api(
            f"repos/{owner}/{repo}/commits/{tag}",
            ".commit.committer.date // empty",
        )
        if code2 == 0 and commit_date:
            date = commit_date[:10]
        else:
            code3, sha, _ = gh_api(
                f"repos/{owner}/{repo}/git/ref/tags/{tag}",
                ".object.sha // empty",
            )
            if code3 == 0 and sha:
                code4, tag_date, _ = gh_api(
                    f"repos/{owner}/{repo}/git/tags/{sha}",
                    ".tagger.date // empty",
                )
                if code4 == 0 and tag_date:
                    date = tag_date[:10]
                else:
                    code5, commit_date, _ = gh_api(
                        f"repos/{owner}/{repo}/commits/{sha}",
                        ".commit.committer.date // empty",
                    )
                    if code5 == 0 and commit_date:
                        date = commit_date[:10]
        return {
            "owner": owner,
            "repo": repo,
            "kind": "tag",
            "ref": tag,
            "date": date,
        }

    code, out, err = gh_api(
        f"repos/{owner}/{repo}/commits?per_page=1",
        ".[0].commit.committer.date // empty",
    )
    if code == 0 and out:
        return {
            "owner": owner,
            "repo": repo,
            "kind": "commit",
            "ref": None,
            "date": out[:10],
        }

    return {
        "owner": owner,
        "repo": repo,
        "kind": "unknown",
        "ref": None,
        "date": None,
        "error": err[:200],
    }


def activity_cell(info: dict) -> str:
    owner, repo = info["owner"], info["repo"]
    kind = info.get("kind") or "unknown"
    date = info.get("date")
    if not date or kind == "unknown":
        return "—"

    if kind == "release":
        url = f"https://github.com/{owner}/{repo}/releases"
    elif kind == "tag":
        url = f"https://github.com/{owner}/{repo}/tags"
    else:
        url = f"https://github.com/{owner}/{repo}/commits"

    return f"[{date}]({url})<br>`{kind}`"


def collect_repos(readme: str) -> list[tuple[str, str]]:
    repos = sorted(set(GITHUB_URL_RE.findall(readme)))
    cleaned: list[tuple[str, str]] = []
    for owner, repo in repos:
        if owner in {"advisories"}:
            continue
        if any(ch in repo for ch in "?#"):
            continue
        cleaned.append((owner, repo))
    return cleaned


def patch_readme(readme: str, activity: dict[tuple[str, str], dict]) -> str:
    lines_out: list[str] = []
    header_cols: list[str] | None = None

    for line in readme.splitlines():
        if not line.startswith("|"):
            header_cols = None
            lines_out.append(line)
            continue

        if re.match(r"^\|\s*-+", line):
            lines_out.append(line)
            continue

        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and cells[0] in {
            "Tool",
            "Source",
            "Service",
            "Directory",
            "Region",
            "Icon",
            "Abbreviation",
            "Tag",
        }:
            # normalize activity header name
            cells = [
                "Activity" if c in {"Updated", "Last update", "Activity"} else c
                for c in cells
            ]
            header_cols = cells
            lines_out.append("| " + " | ".join(cells) + " |")
            continue

        if not header_cols or "Activity" not in header_cols:
            lines_out.append(line)
            continue

        activity_idx = header_cols.index("Activity")
        # find first github repo mentioned in the row (usually Tool cell)
        matches = GITHUB_URL_RE.findall(line)
        if not matches:
            # keep em-dash for non-github
            if activity_idx < len(cells):
                cells[activity_idx] = "—"
            while len(cells) < len(header_cols):
                cells.append("")
            lines_out.append("| " + " | ".join(cells[: len(header_cols)]) + " |")
            continue

        owner, repo = matches[0]
        info = activity.get((owner, repo))
        if info is None:
            info = {"owner": owner, "repo": repo, "kind": "unknown", "date": None}

        while len(cells) < len(header_cols):
            cells.append("")
        cells[activity_idx] = activity_cell(info)
        lines_out.append("| " + " | ".join(cells[: len(header_cols)]) + " |")

    return "\n".join(lines_out) + "\n"


def replace_activity_legend(readme: str) -> str:
    legend = """In tables, the **name** is on the first line and the **link** on the next (`<br>`).

**Activity** shows a full ISO date (`YYYY-MM-DD`), preferred signal first:

| Marker | Meaning |
|---|---|
| `release` | Latest **GitHub Release** publish date |
| `tag` | Latest git **tag** date (no GitHub Release) |
| `commit` | Latest git **commit** date (fallback; may include bots) |
| `—` | No public GitHub repo |

Refresh dates:

```bash
python3 scripts/update-activity.py
```

Or let GitHub Actions refresh them on a schedule (see `.github/workflows/update-activity.yml`).
"""

    readme = re.sub(
        r"In tables, the \*\*name\*\*.*?(?=\n## Table of Contents)",
        legend + "\n",
        readme,
        count=1,
        flags=re.S,
    )
    # backward-compatible if old "Activity badges" block exists without the intro sentence
    if "**Activity** shows a full ISO date" not in readme:
        readme = re.sub(
            r"\*\*Activity badges\*\*.*?(?=\n## Table of Contents)",
            legend.split("\n", 2)[-1],
            readme,
            count=1,
            flags=re.S,
        )
    return readme


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    parser.add_argument("--data", type=Path, default=Path("data/activity.json"))
    parser.add_argument("--workers", type=int, default=12)
    args = parser.parse_args()

    # ensure gh works
    probe = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True)
    if probe.returncode != 0:
        print("gh is not authenticated. Run: gh auth login", file=sys.stderr)
        return 1

    readme = args.readme.read_text()
    repos = collect_repos(readme)
    print(f"Fetching activity for {len(repos)} repos...")

    results: list[dict] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        for i, row in enumerate(pool.map(lambda p: fetch_activity(*p), repos), 1):
            results.append(row)
            if i % 40 == 0:
                print(f"  progress {i}/{len(repos)}")

    print("kinds:", dict(Counter(r["kind"] for r in results)))
    missing = [r for r in results if not r.get("date")]
    if missing:
        print(f"warning: {len(missing)} repos without dates")

    args.data.parent.mkdir(parents=True, exist_ok=True)
    args.data.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(f"wrote {args.data}")

    activity = {(r["owner"], r["repo"]): r for r in results}
    updated = patch_readme(readme, activity)
    updated = replace_activity_legend(updated)
    args.readme.write_text(updated)
    print(f"updated {args.readme}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
