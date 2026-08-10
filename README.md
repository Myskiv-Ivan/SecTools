# SecTools

A curated collection of open-source and public tools for OSINT, vulnerability analysis, AppSec (SAST / DAST / SCA), recon, cloud security, and related security workflows.

Most tools are UNIX-compatible. The **License** column uses icons (see legend below). Tool cells use `Name` + link on a new line so columns stay readable.

### License legend

| Icon | Meaning |
|---|---|
| 🟢 | **Open source** — Apache, MIT, GPL, BSD, AGPL, etc. |
| 🟡 | **Freemium** — free / community edition + paid enterprise tiers |
| 🔴 | **Enterprise** — commercial proprietary license |
| ☁️ | **Service** — hosted SaaS / online platform |
| 🌐 | **Public** — free public resource or dataset |

In tables, the **name** is on the first line and the **link** on the next (`<br>`).

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


## Table of Contents

- [OSINT](#-osint)
- [Vulnerability Management Platforms](#-vulnerability-management-platforms)
- [Analysis & Exploit Frameworks](#-analysis--exploit-frameworks)
- [Web Proxies & Manual Testing](#-web-proxies--manual-testing)
- [SAST](#-sast--static-analysis)
- [DAST / IAST](#-dast--iast)
- [SCA / IaC](#-sca--iac)
- [SBOM](#-sbom)
- [Secret Detection](#-secret-detection)
- [Scanners](#-scanners)
- [Recon & Enumeration](#-recon--enumeration)
- [Active Directory & Internal](#-active-directory--internal)
- [Password Cracking](#-password-cracking)
- [Cloud & Container Security](#-cloud--container-security)
- [Network Analysis & IDS](#-network-analysis--ids)
- [Forensics & Incident Response](#-forensics--incident-response)
- [Threat Intelligence](#-threat-intelligence)
- [Breach & Leak Lookup](#-breach--leak-lookup)
- [Binary Analysis & Reverse Engineering](#-binary-analysis--reverse-engineering)
- [Wordlists & Payloads](#-wordlists--payloads)
- [Vulnerability Databases](#-vulnerability-databases)
- [External directories](#-external-directories)

---

## 🔭 OSINT

Open-source intelligence: accounts, DNS, infrastructure, and public metadata.

| Tool | Description | License | Activity |
|---|---|---|---|
| **Sherlock**<br>[GitHub](https://github.com/sherlock-project/sherlock) | Hunt usernames across hundreds of social networks | 🟢 | [2025-09-16](https://github.com/sherlock-project/sherlock/releases)<br>`release` |
| **theHarvester**<br>[GitHub](https://github.com/laramies/theHarvester) | Gather emails, subdomains, hosts, and people from public sources | 🟢 | [2026-06-03](https://github.com/laramies/theHarvester/releases)<br>`release` |
| **SpiderFoot**<br>[GitHub](https://github.com/smicallef/spiderfoot) | Automated OSINT with hundreds of modules and a web UI | 🟢 | [2022-04-07](https://github.com/smicallef/spiderfoot/releases)<br>`release` |
| **Recon-ng**<br>[GitHub](https://github.com/lanmaster53/recon-ng) | Modular reconnaissance framework (Metasploit-style) | 🟢 | [2021-08-25](https://github.com/lanmaster53/recon-ng/tags)<br>`tag` |
| **Photon**<br>[GitHub](https://github.com/s0md3v/Photon) | Fast crawler for OSINT data extraction from websites | 🟢 | [2019-04-05](https://github.com/s0md3v/Photon/releases)<br>`release` |
| **Maltego**<br>[maltego.com](https://www.maltego.com/) | Graph visualization of people, domains, and infrastructure | 🟡 | — |
| **R3CON1Z3R**<br>[GitHub](https://github.com/abdulgaphy/r3con1z3r) | Lightweight OSINT script for target footprinting | 🟢 | [2019-07-24](https://github.com/abdulgaphy/r3con1z3r/commits)<br>`commit` |
| **Shodan**<br>[shodan.io](https://www.shodan.io/) | Search engine for Internet-connected devices and services | ☁️ | — |
| **Censys**<br>[censys.io](https://search.censys.io/) | Host, certificate, and service indexing | ☁️ | — |
| **ZoomEye**<br>[zoomeye.ai](https://www.zoomeye.ai/) | Network asset and device search (Shodan-like) | ☁️ | — |
| **FOFA**<br>[fofa.info](https://fofa.info/) | Cyberspace search engine for assets and fingerprints | ☁️ | — |
| **urlscan.io**<br>[urlscan.io](https://urlscan.io/) | URL / page analysis and snapshots | ☁️ | — |
| **ONYPHE**<br>[onyphe.io](https://www.onyphe.io/) | Cyber threat intelligence aggregator for IPs, domains, services | ☁️ | — |
| **BuiltWith**<br>[builtwith.com](https://builtwith.com/) | Detect a site’s technology stack | ☁️ | — |
| **Hunter.io**<br>[hunter.io](https://hunter.io/) | Find and verify professional email addresses | ☁️ | — |
| **crt.sh**<br>[crt.sh](https://crt.sh/) | Certificate Transparency log search (subdomain discovery) | 🌐 | — |
| **SecurityTrails**<br>[securitytrails.com](https://securitytrails.com/) | Historical DNS, WHOIS, and domain intelligence | ☁️ | — |
| **who.is**<br>[who.is](https://who.is/) | WHOIS / DNS lookup | 🌐 | — |
| **DNSstuff**<br>[dnsstuff.com](https://www.dnsstuff.com) | DNS diagnostics and lookup utilities | ☁️ | — |
| **InfoSniper**<br>[infosniper.net](https://www.infosniper.net/) | IP geolocation | 🌐 | — |
| **scans.io**<br>[scans.io](https://scans.io/) | Internet-wide scan data archive | 🌐 | — |
| **Wayback Machine**<br>[archive.org](https://web.archive.org/) | Historical snapshots of web pages | 🌐 | — |
| **IntelX**<br>[intelx.io](https://intelx.io/) | Search engine for leaked / archived data and IDs | ☁️ | — |

### Localized search engines

| Region | Link |
|---|---|
| Slovenia | Najdi.si<br>[najdi.si](http://www.najdi.si/) |
| Israel | Walla<br>[walla.co.il](http://www.walla.co.il/) |
| Japan | Goo<br>[goo.ne.jp](http://www.goo.ne.jp/) |
| South Korea | Naver<br>[naver.com](http://www.naver.com/) |
| China | Baidu<br>[baidu.com](http://www.baidu.com/) |
| Russia | Yandex<br>[yandex.com](http://www.yandex.com/) |

### File search

| Service | Description | License |
|---|---|---|
| **FileChef**<br>[filechef.com](https://www.filechef.com/) | Search publicly exposed files | ☁️ |
| **File Search Engine**<br>[filesearch.link](https://www.filesearch.link/) | Index of publicly available files | ☁️ |
| **SearchFiles.de**<br>[searchfiles.de](https://searchfiles.de/) | Search files by name / type | ☁️ |
| **FileListing**<br>[filelisting.com](https://filelisting.com/) | Catalog of open file listings | ☁️ |

---

## 🛡️ Vulnerability Management Platforms

Orchestrate scanner findings, triage, and reporting.

| Tool | Description | License | Activity |
|---|---|---|---|
| **DefectDojo**<br>[GitHub](https://github.com/DefectDojo/django-DefectDojo) | DevSecOps platform: report import, triage, metrics, SLA | 🟢 | [2026-08-03](https://github.com/DefectDojo/django-DefectDojo/releases)<br>`release` |
| **Faraday**<br>[GitHub](https://github.com/infobyte/faraday) | Collaborative pentest IDE / vulnerability management | 🟢 | [2026-07-23](https://github.com/infobyte/faraday/releases)<br>`release` |
| **ArcherySec**<br>[GitHub](https://github.com/archerysec/archerysec) | Vulnerability assessment & management with scanner integrations | 🟢 | [2024-05-31](https://github.com/archerysec/archerysec/releases)<br>`release` |
| **reNgine**<br>[GitHub](https://github.com/yogeshojha/rengine) | Automated recon + vulnerability management with web UI | 🟢 | [2024-09-07](https://github.com/yogeshojha/rengine/releases)<br>`release` |
| **Vuls**<br>[GitHub](https://github.com/future-architect/vuls) | Agentless vulnerability scanner for Linux / FreeBSD | 🟢 | [2026-07-30](https://github.com/future-architect/vuls/releases)<br>`release` |
| **OWASP Threat Dragon**<br>[GitHub](https://github.com/OWASP/threat-dragon) | Threat modeling tool for STRIDE-style diagrams | 🟢 | [2026-05-10](https://github.com/OWASP/threat-dragon/releases)<br>`release` |

---

## ⚒️ Analysis & Exploit Frameworks

| Tool | Category | Description | License | Activity |
|---|---|---|---|---|
| **Metasploit**<br>[GitHub](https://github.com/rapid7/metasploit-framework) | Exploit Framework | Classic exploit, payload, and post-exploitation framework | 🟡 | [2016-01-07](https://github.com/rapid7/metasploit-framework/tags)<br>`tag` |
| **RouterSploit**<br>[GitHub](https://github.com/threat9/routersploit) | Exploit Framework | Exploits and checks for embedded / network devices | 🟢 | [2018-10-17](https://github.com/threat9/routersploit/releases)<br>`release` |
| **BeEF**<br>[GitHub](https://github.com/beefproject/beef) | Exploit Framework | Browser Exploitation Framework | 🟢 | [2025-10-24](https://github.com/beefproject/beef/releases)<br>`release` |
| **Sliver**<br>[GitHub](https://github.com/BishopFox/sliver) | C2 | Open-source adversary emulation / C2 framework | 🟢 | [2026-02-24](https://github.com/BishopFox/sliver/releases)<br>`release` |
| **Havoc**<br>[GitHub](https://github.com/HavocFramework/Havoc) | C2 | Modern post-exploitation command and control | 🟢 | [2025-12-18](https://github.com/HavocFramework/Havoc/commits)<br>`commit` |
| **MobSF**<br>[GitHub](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | Mobile | Static and dynamic analysis for Android / iOS | 🟢 | [2026-08-10](https://github.com/MobSF/Mobile-Security-Framework-MobSF/releases)<br>`release` |
| **Frida**<br>[GitHub](https://github.com/frida/frida) | Dynamic Instrumentation | Dynamic instrumentation toolkit for apps | 🟢 | [2026-08-05](https://github.com/frida/frida/releases)<br>`release` |
| **Objection**<br>[GitHub](https://github.com/sensepost/objection) | Mobile | Runtime mobile exploration powered by Frida | 🟢 | [2026-06-02](https://github.com/sensepost/objection/releases)<br>`release` |
| **RedTeam C# Scripts**<br>[GitHub](https://github.com/Mr-Un1k0d3r/RedTeamCSharpScripts) | Red Team | Collection of C# scripts for red team operations | 🟢 | [2021-11-16](https://github.com/Mr-Un1k0d3r/RedTeamCSharpScripts/commits)<br>`commit` |
| **Atomic Red Team**<br>[GitHub](https://github.com/redcanaryco/atomic-red-team) | Adversary Emulation | Small, focused tests mapped to ATT&CK techniques | 🟢 | [2026-07-20](https://github.com/redcanaryco/atomic-red-team/commits)<br>`commit` |
| **CALDERA**<br>[GitHub](https://github.com/mitre/caldera) | Adversary Emulation | Automated adversary emulation platform by MITRE | 🟢 | [2025-04-24](https://github.com/mitre/caldera/releases)<br>`release` |

---

## 🧰 Web Proxies & Manual Testing

Intercept, replay, and mutate HTTP(S) traffic during web assessments.

| Tool | Description | License | Activity |
|---|---|---|---|
| **Burp Suite**<br>[portswigger.net](https://portswigger.net/burp) | Industry-standard web security testing platform (Community / Pro) | 🟡 | — |
| **Caido**<br>[caido.io](https://caido.io/) | Modern lightweight web proxy for bug bounty and pentest | 🟡 | [2026-07-10](https://github.com/caido/caido/releases)<br>`release` |
| **mitmproxy**<br>[GitHub](https://github.com/mitmproxy/mitmproxy) | Interactive TLS-capable intercepting HTTP proxy (CLI + web) | 🟢 | [2026-05-12](https://github.com/mitmproxy/mitmproxy/releases)<br>`release` |
| **OWASP ZAP**<br>[GitHub](https://github.com/zaproxy/zaproxy) | Free proxy + automated scanner | 🟢 | [2025-12-15](https://github.com/zaproxy/zaproxy/releases)<br>`release` |
| **WATOBO**<br>[GitHub](https://github.com/siberas/watobo) | Intercepting proxy + scanner for pentests | 🟢 | [2020-05-27](https://github.com/siberas/watobo/releases)<br>`release` |

---

## 🔎 SAST — Static Analysis

Find vulnerabilities in source code without running the application.

| Tool | Languages / scope | Description | License | Activity |
|---|---|---|---|---|
| **Semgrep**<br>[GitHub](https://github.com/semgrep/semgrep) | 30+ languages | Fast pattern-based SAST with YAML rules; CI-friendly | 🟡 | [2026-07-28](https://github.com/semgrep/semgrep/releases)<br>`release` |
| **CodeQL**<br>[codeql.github.com](https://codeql.github.com/) | Multilang | Semantic code analysis from GitHub (query-as-code) | 🟡 | — |
| **Bearer**<br>[GitHub](https://github.com/Bearer/bearer) | JS/TS, Ruby, PHP, Java, Go, Python | SAST focused on data flows and privacy | 🟢 | [2026-08-03](https://github.com/Bearer/bearer/releases)<br>`release` |
| **Bandit**<br>[GitHub](https://github.com/PyCQA/bandit) | Python | Common security issues in Python | 🟢 | [2026-02-25](https://github.com/PyCQA/bandit/releases)<br>`release` |
| **Brakeman**<br>[GitHub](https://github.com/presidentbeef/brakeman) | Ruby on Rails | Rails-focused static security scanner | 🟢 | [2026-06-12](https://github.com/presidentbeef/brakeman/releases)<br>`release` |
| **Find Security Bugs**<br>[GitHub](https://github.com/find-sec-bugs/find-sec-bugs) | Java, Android, Scala, Kotlin, Groovy | SpotBugs plugin for web / Android security | 🟢 | [2025-06-17](https://github.com/find-sec-bugs/find-sec-bugs/releases)<br>`release` |
| **SpotBugs**<br>[GitHub](https://github.com/spotbugs/spotbugs) | Java | Static analysis of Java bytecode | 🟢 | [2026-07-12](https://github.com/spotbugs/spotbugs/releases)<br>`release` |
| **PMD**<br>[GitHub](https://github.com/pmd/pmd) | Multilang | Static analysis for quality and security rules | 🟢 | [2026-06-29](https://github.com/pmd/pmd/releases)<br>`release` |
| **Security Code Scan**<br>[GitHub](https://github.com/security-code-scan/security-code-scan) | C#, VB.NET | Roslyn analyzer for .NET vulnerabilities | 🟢 | [2022-09-05](https://github.com/security-code-scan/security-code-scan/releases)<br>`release` |
| **Infer#**<br>[GitHub](https://github.com/microsoft/infersharp) | C# | Interprocedural .NET analysis based on Facebook Infer | 🟢 | [2023-05-31](https://github.com/microsoft/infersharp/releases)<br>`release` |
| **Insider**<br>[GitHub](https://github.com/insidersec/insider) | Java, Kotlin, Swift, .NET, JS | CLI SAST for multiple stacks | 🟢 | [2021-01-26](https://github.com/insidersec/insider/releases)<br>`release` |
| **Codechecker**<br>[GitHub](https://github.com/Ericsson/codechecker) | C/C++ | Wrapper around Clang Static Analyzer / Clang-Tidy | 🟢 | [2026-06-25](https://github.com/Ericsson/codechecker/releases)<br>`release` |
| **Cppcheck**<br>[GitHub](https://github.com/danmar/cppcheck) | C/C++ | Static analysis focused on undefined behavior | 🟢 | [2026-06-04](https://github.com/danmar/cppcheck/releases)<br>`release` |
| **LLVM Clang SA**<br>[GitHub](https://github.com/llvm/llvm-project) | C, C++, Obj-C | Clang Static Analyzer | 🟢 | [2026-06-16](https://github.com/llvm/llvm-project/releases)<br>`release` |
| **PVS-Studio**<br>[pvs-studio.com](https://pvs-studio.com/) | Multilang | Commercial static analyzer (trial available) | 🔴 | — |
| **Codemodder**<br>[GitHub](https://github.com/pixee/codemodder-python) | Java, Python | Auto-fix for security and quality issues | 🟢 | [2025-10-21](https://github.com/pixee/codemodder-python/releases)<br>`release` |
| **gosec**<br>[GitHub](https://github.com/securego/gosec) | Go | Inspector for security problems in Go code | 🟢 | [2026-07-14](https://github.com/securego/gosec/releases)<br>`release` |
| **PHP Vulnerability Hunter**<br>[GitHub](https://github.com/OneSourceCat/phpvulhunter) | PHP | PHP vulnerability finder (legacy) | 🟢 | [2015-06-10](https://github.com/OneSourceCat/phpvulhunter/commits)<br>`commit` |
| **Cobra**<br>[GitHub](https://github.com/wufeifei/cobra) | PHP, Java | Source code security audit (legacy) | 🟢 | [2018-04-02](https://github.com/wufeifei/cobra/releases)<br>`release` |

---

## 🎯 DAST / IAST

Dynamic and interactive analysis of running applications.

| Tool | Type | Description | License | Activity |
|---|---|---|---|---|
| **OWASP ZAP**<br>[GitHub](https://github.com/zaproxy/zaproxy) | DAST | Free web proxy and automated scanner from OWASP | 🟢 | [2025-12-15](https://github.com/zaproxy/zaproxy/releases)<br>`release` |
| **Nuclei**<br>[GitHub](https://github.com/projectdiscovery/nuclei) | DAST | Fast YAML-template scanner for CVE / misconfig (HTTP, DNS, TCP…) | 🟢 | [2026-08-08](https://github.com/projectdiscovery/nuclei/releases)<br>`release` |
| **Nikto**<br>[GitHub](https://github.com/sullo/nikto) | DAST | Classic web scanner for dangerous files and misconfigurations | 🟢 | [2026-07-31](https://github.com/sullo/nikto/releases)<br>`release` |
| **Wapiti**<br>[GitHub](https://github.com/wapiti-scanner/wapiti) | DAST | Black-box web scanner (XSS, SQLi, and more) | 🟢 | [2026-07-27](https://github.com/wapiti-scanner/wapiti/releases)<br>`release` |
| **w3af**<br>[GitHub](https://github.com/andresriancho/w3af) | DAST | Web Application Attack and Audit Framework | 🟢 | [2015-04-07](https://github.com/andresriancho/w3af/releases)<br>`release` |
| **Dalfox**<br>[GitHub](https://github.com/hahwul/dalfox) | XSS | Parameter analysis and XSS scanning / exploitation helper | 🟢 | [2026-08-02](https://github.com/hahwul/dalfox/releases)<br>`release` |
| **Commix**<br>[GitHub](https://github.com/commixproject/commix) | Command Injection | Automated OS command injection detection and exploitation | 🟢 | [2025-12-20](https://github.com/commixproject/commix/releases)<br>`release` |
| **jwt_tool**<br>[GitHub](https://github.com/ticarpi/jwt_tool) | API / Auth | Toolkit for testing, forging, and attacking JWTs | 🟢 | [2025-05-01](https://github.com/ticarpi/jwt_tool/releases)<br>`release` |
| **Snyk**<br>[GitHub](https://github.com/snyk/cli) | DAST / SCA | Scan code, dependencies, containers, and IaC | 🟡 | [2026-08-06](https://github.com/snyk/cli/releases)<br>`release` |
| **SonarQube**<br>[GitHub](https://github.com/SonarSource/sonarqube) | SAST / Quality | Code quality + security hotspots | 🟡 | [2026-08-05](https://github.com/SonarSource/sonarqube/releases)<br>`release` |
| **Contrast Security**<br>[contrastsecurity.com](https://www.contrastsecurity.com/) | IAST | Agent-based interactive analysis at runtime | 🔴 | — |
| **PT Application Inspector**<br>[ptsecurity.com](https://www.ptsecurity.com/ww-en/products/ai/) | SAST/DAST | Commercial application analyzer (Positive Technologies) | 🔴 | — |
| **CloudSploit**<br>[GitHub](https://github.com/aquasecurity/cloudsploit) | Cloud | Misconfiguration checks for AWS / Azure / GCP / Oracle | 🟢 | [2024-09-24](https://github.com/aquasecurity/cloudsploit/releases)<br>`release` |
| **Mend (WhiteSource)**<br>[mend.io](https://www.mend.io/) | SCA / AppSec | Commercial open-source risk platform | 🔴 | — |

---

## 📦 SCA / IaC

Dependency and infrastructure-as-code analysis.

| Tool | Focus | Description | License | Activity |
|---|---|---|---|---|
| **Trivy**<br>[GitHub](https://github.com/aquasecurity/trivy) | SCA + IaC + Containers | All-in-one: deps, images, IaC, secrets | 🟢 | [2026-08-03](https://github.com/aquasecurity/trivy/releases)<br>`release` |
| **Grype**<br>[GitHub](https://github.com/anchore/grype) | SCA / Containers | Vulnerability scanner for images and filesystems | 🟢 | [2026-07-28](https://github.com/anchore/grype/releases)<br>`release` |
| **OSV-Scanner**<br>[GitHub](https://github.com/google/osv-scanner) | SCA | Scanner powered by [OSV.dev](https://osv.dev) (Google) | 🟢 | [2026-08-07](https://github.com/google/osv-scanner/releases)<br>`release` |
| **Dependency-Track**<br>[GitHub](https://github.com/DependencyTrack/dependency-track) | SCA Platform | Continuous analysis platform for SBOM / dependencies | 🟢 | [2026-07-30](https://github.com/DependencyTrack/dependency-track/releases)<br>`release` |
| **OWASP Dependency-Check**<br>[GitHub](https://github.com/jeremylong/DependencyCheck) | SCA | Match dependencies against known CVE | 🟢 | [2025-02-17](https://github.com/jeremylong/DependencyCheck/releases)<br>`release` |
| **Checkov**<br>[GitHub](https://github.com/bridgecrewio/checkov) | IaC | Policy-as-code for Terraform, K8s, CloudFormation, Docker | 🟢 | [2026-08-02](https://github.com/bridgecrewio/checkov/releases)<br>`release` |
| **KICS**<br>[GitHub](https://github.com/Checkmarx/kics) | IaC | Keeping Infrastructure as Code Secure — multi-IaC scanner | 🟢 | [2026-07-30](https://github.com/Checkmarx/kics/releases)<br>`release` |
| **tfsec**<br>[GitHub](https://github.com/aquasecurity/tfsec) | IaC | Terraform security scanner (Trivy lineage) | 🟢 | [2025-05-02](https://github.com/aquasecurity/tfsec/releases)<br>`release` |
| **Terrascan**<br>[GitHub](https://github.com/tenable/terrascan) | IaC | Compliance / security scanning for IaC | 🟢 | [2024-09-18](https://github.com/tenable/terrascan/releases)<br>`release` |

---

## 📋 SBOM

Software Bill of Materials generation.

| Tool | Format | Description | License | Activity |
|---|---|---|---|---|
| **Syft**<br>[GitHub](https://github.com/anchore/syft) | SPDX, CycloneDX | Generate SBOM from images, directories, and manifests | 🟢 | [2026-07-28](https://github.com/anchore/syft/releases)<br>`release` |
| **cdxgen**<br>[GitHub](https://github.com/CycloneDX/cdxgen) | CycloneDX | Universal CycloneDX SBOM generator | 🟢 | [2026-07-23](https://github.com/CycloneDX/cdxgen/releases)<br>`release` |
| **Trivy**<br>[GitHub](https://github.com/aquasecurity/trivy) | SPDX, CycloneDX | SBOM as part of scanning | 🟢 | [2026-08-03](https://github.com/aquasecurity/trivy/releases)<br>`release` |

---

## 🔐 Secret Detection

| Tool | Description | License | Activity |
|---|---|---|---|
| **Gitleaks**<br>[GitHub](https://github.com/gitleaks/gitleaks) | Fast secret detection in git history and filesystem | 🟢 | [2026-03-21](https://github.com/gitleaks/gitleaks/releases)<br>`release` |
| **TruffleHog**<br>[GitHub](https://github.com/trufflesecurity/trufflehog) | Secret detection with live verification (API keys, etc.) | 🟢 | [2026-07-24](https://github.com/trufflesecurity/trufflehog/releases)<br>`release` |
| **git-secret**<br>[GitHub](https://github.com/sobolevn/git-secret) | Encrypt secrets in git via GPG | 🟢 | [2022-06-05](https://github.com/sobolevn/git-secret/releases)<br>`release` |
| **detect-secrets**<br>[GitHub](https://github.com/Yelp/detect-secrets) | Enterprise-friendly baseline secret scanner (Yelp) | 🟢 | [2024-05-06](https://github.com/Yelp/detect-secrets/releases)<br>`release` |

---

## 🛰️ Scanners

Network, web, and general-purpose vulnerability scanners.

| Tool | Type | Description | License | Activity |
|---|---|---|---|---|
| **Nmap**<br>[GitHub](https://github.com/nmap/nmap) | Network | Reference network discovery / port scanner | 🟢 | [2026-08-05](https://github.com/nmap/nmap/tags)<br>`tag` |
| **Masscan**<br>[GitHub](https://github.com/robertdavidgraham/masscan) | Network | Asynchronous ultra-fast port scanner | 🟢 | [2021-01-31](https://github.com/robertdavidgraham/masscan/releases)<br>`release` |
| **RustScan**<br>[GitHub](https://github.com/RustScan/RustScan) | Network | Extremely fast port scanner that pipes into Nmap | 🟢 | [2025-02-23](https://github.com/RustScan/RustScan/releases)<br>`release` |
| **OpenVAS / Greenbone**<br>[GitHub](https://github.com/greenbone/openvas-scanner) | Network VA | Full vulnerability assessment stack | 🟢 | [2026-08-05](https://github.com/greenbone/openvas-scanner/releases)<br>`release` |
| **Nessus**<br>[tenable.com](https://www.tenable.com/products/nessus) | Network VA | Commercial VA scanner by Tenable | 🔴 | — |
| **InsightVM (Nexpose)**<br>[rapid7.com](https://www.rapid7.com/products/insightvm/) | Network VA | Vulnerability management by Rapid7 | 🔴 | — |
| **Tsunami**<br>[GitHub](https://github.com/google/tsunami-security-scanner) | Network | Modular high-severity scanner by Google | 🟢 | [2026-02-19](https://github.com/google/tsunami-security-scanner/releases)<br>`release` |
| **testssl.sh**<br>[GitHub](https://github.com/drwetter/testssl.sh) | TLS / SSL | CLI checker for TLS/SSL ciphers, protocols, and vulns | 🟢 | [2026-07-12](https://github.com/drwetter/testssl.sh/releases)<br>`release` |
| **SSLyze**<br>[GitHub](https://github.com/nabla-c0d3/sslyze) | TLS / SSL | Fast and powerful SSL/TLS scanning library | 🟢 | [2026-03-29](https://github.com/nabla-c0d3/sslyze/releases)<br>`release` |
| **Sqlmap**<br>[GitHub](https://github.com/sqlmapproject/sqlmap) | Web / SQLi | Automated SQL Injection detection and exploitation | 🟢 | [2026-01-01](https://github.com/sqlmapproject/sqlmap/releases)<br>`release` |
| **NoSQLMap**<br>[GitHub](https://github.com/codingo/NoSQLMap) | NoSQL | Audit and exploit NoSQL injection | 🟢 | [2016-01-11](https://github.com/codingo/NoSQLMap/releases)<br>`release` |
| **WhatWeb**<br>[GitHub](https://github.com/urbanadventurer/WhatWeb) | Fingerprint | Identify CMS, frameworks, and site tech | 🟢 | [2026-04-02](https://github.com/urbanadventurer/WhatWeb/releases)<br>`release` |
| **Wappalyzer**<br>[wappalyzer.com](https://www.wappalyzer.com/) | Fingerprint | Identify technologies used on websites | 🟡 | — |
| **wappalyzergo**<br>[GitHub](https://github.com/projectdiscovery/wappalyzergo) | Fingerprint | Go port of Wappalyzer fingerprinting for CLI / pipelines | 🟢 | [2026-08-09](https://github.com/projectdiscovery/wappalyzergo/releases)<br>`release` |
| **Xray**<br>[GitHub](https://github.com/chaitin/xray) | Web | Passive / active web scanner (Chaitin) | 🟢 | [2024-07-19](https://github.com/chaitin/xray/releases)<br>`release` |
| **Osmedeus**<br>[GitHub](https://github.com/j3ssie/Osmedeus) | Orchestration | Workflow engine for automated recon / scan | 🟢 | [2026-08-08](https://github.com/j3ssie/Osmedeus/releases)<br>`release` |
| **OneForAll**<br>[GitHub](https://github.com/shmilylty/OneForAll) | Subdomain / Recon | Powerful subdomain collection | 🟢 | [2022-07-10](https://github.com/shmilylty/OneForAll/releases)<br>`release` |
| **Sn1per**<br>[GitHub](https://github.com/1N3/Sn1per) | Pentest Automation | Automated pentest framework | 🟡 | [2023-07-29](https://github.com/1N3/Sn1per/releases)<br>`release` |
| **AutoRecon**<br>[GitHub](https://github.com/Tib3rius/AutoRecon) | Recon | Multi-threaded network recon for CTF / pentest | 🟢 | [2025-11-16](https://github.com/Tib3rius/AutoRecon/commits)<br>`commit` |
| **Legion**<br>[GitHub](https://github.com/GoVanguard/legion) | Network GUI | GUI wrapper around Nmap and other scanners | 🟢 | [2023-11-21](https://github.com/GoVanguard/legion/releases)<br>`release` |
| **Raccoon**<br>[GitHub](https://github.com/evyatarmeged/Raccoon) | Recon | Asynchronous recon / offensive reconnaissance | 🟢 | [2025-06-10](https://github.com/evyatarmeged/Raccoon/commits)<br>`commit` |
| **Scanless**<br>[GitHub](https://github.com/vesche/scanless) | Network | Port scan via public online scanners (opsec) | 🟢 | [2023-03-23](https://github.com/vesche/scanless/releases)<br>`release` |
| **Golismero**<br>[GitHub](https://github.com/golismero/golismero) | Framework | Security framework with plugins | 🟢 | [2020-04-16](https://github.com/golismero/golismero/commits)<br>`commit` |
| **Arachni**<br>[GitHub](https://github.com/Arachni/arachni) | Web | Modular web scanner (maintenance mode) | 🟢 | [2022-05-29](https://github.com/Arachni/arachni/tags)<br>`tag` |
| **Acunetix**<br>[acunetix.com](https://www.acunetix.com/) | Web | Commercial DAST | 🔴 | — |
| **Invicti (Netsparker)**<br>[invicti.com](https://www.invicti.com/) | Web | Commercial DAST with proof-based scanning | 🔴 | — |
| **ScanOval**<br>[bdu.fstec.ru](https://bdu.fstec.ru/site/scanoval) | OVAL / BDU | OVAL-based vulnerability checks (FSTEC BDU) | 🌐 | — |
| **Puma Scan**<br>[GitHub](https://github.com/pumasecurity/puma-scan) | .NET SAST | Roslyn analyzer for .NET security | 🟡 | [2022-02-01](https://github.com/pumasecurity/puma-scan/releases)<br>`release` |

---

## 🧭 Recon & Enumeration

| Tool | Description | License | Activity |
|---|---|---|---|
| **Amass**<br>[GitHub](https://github.com/owasp-amass/amass) | OWASP: deep subdomain enumeration and attack-surface mapping | 🟢 | [2026-04-07](https://github.com/owasp-amass/amass/releases)<br>`release` |
| **subfinder**<br>[GitHub](https://github.com/projectdiscovery/subfinder) | Passive subdomain discovery (ProjectDiscovery) | 🟢 | [2026-08-05](https://github.com/projectdiscovery/subfinder/releases)<br>`release` |
| **httpx**<br>[GitHub](https://github.com/projectdiscovery/httpx) | Fast HTTP probing / tech detection | 🟢 | [2026-07-09](https://github.com/projectdiscovery/httpx/releases)<br>`release` |
| **dnsx**<br>[GitHub](https://github.com/projectdiscovery/dnsx) | DNS toolkit for resolve and enumeration | 🟢 | [2026-07-16](https://github.com/projectdiscovery/dnsx/releases)<br>`release` |
| **Chaos**<br>[GitHub](https://github.com/projectdiscovery/chaos-client) | ProjectDiscovery DNS dataset client for passive recon | 🟢 | [2024-04-22](https://github.com/projectdiscovery/chaos-client/releases)<br>`release` |
| **ffuf**<br>[GitHub](https://github.com/ffuf/ffuf) | Fast web fuzzer (dirs, vhosts, params) | 🟢 | [2026-07-13](https://github.com/ffuf/ffuf/releases)<br>`release` |
| **gobuster**<br>[GitHub](https://github.com/OJ/gobuster) | Directory, DNS, and vhost brute-forcing | 🟢 | [2025-09-04](https://github.com/OJ/gobuster/releases)<br>`release` |
| **feroxbuster**<br>[GitHub](https://github.com/epi052/feroxbuster) | Fast, recursive content discovery written in Rust | 🟢 | [2025-12-13](https://github.com/epi052/feroxbuster/releases)<br>`release` |
| **Arjun**<br>[GitHub](https://github.com/s0md3v/Arjun) | HTTP parameter discovery suite | 🟢 | [2024-11-03](https://github.com/s0md3v/Arjun/releases)<br>`release` |
| **knock**<br>[GitHub](https://github.com/guelfoweb/knock) | Subdomain enumeration via wordlist + DNS | 🟢 | [2026-02-14](https://github.com/guelfoweb/knock/releases)<br>`release` |
| **subDomainsBrute**<br>[GitHub](https://github.com/lijiejie/subDomainsBrute) | Multi-threaded subdomain brute-force | 🟢 | [2022-06-05](https://github.com/lijiejie/subDomainsBrute/releases)<br>`release` |
| **SubDomain3**<br>[GitHub](https://github.com/yanxiu0614/subdomain3) | High-speed subdomain scanner | 🟢 | [2020-01-20](https://github.com/yanxiu0614/subdomain3/releases)<br>`release` |
| **domained**<br>[GitHub](https://github.com/TypeError/domained) | Wrapper around multiple subdomain tools | 🟢 | [2021-04-11](https://github.com/TypeError/domained/commits)<br>`commit` |
| **katana**<br>[GitHub](https://github.com/projectdiscovery/katana) | Next-gen crawling / spidering | 🟢 | [2026-08-05](https://github.com/projectdiscovery/katana/releases)<br>`release` |
| **gau**<br>[GitHub](https://github.com/lc/gau) | Fetch known URLs from public sources | 🟢 | [2024-10-28](https://github.com/lc/gau/releases)<br>`release` |
| **waybackurls**<br>[GitHub](https://github.com/tomnomnom/waybackurls) | Fetch URLs from the Wayback Machine for a domain | 🟢 | [2022-04-05](https://github.com/tomnomnom/waybackurls/releases)<br>`release` |
| **hakrawler**<br>[GitHub](https://github.com/hakluke/hakrawler) | Simple, fast web crawler for gathering URLs / endpoints | 🟢 | [2022-05-23](https://github.com/hakluke/hakrawler/releases)<br>`release` |

---

## 🏢 Active Directory & Internal

Identity attack-path mapping and Windows / AD assessment tooling.

| Tool | Description | License | Activity |
|---|---|---|---|
| **BloodHound**<br>[GitHub](https://github.com/SpecterOps/BloodHound) | Graph analysis of AD / Entra ID attack paths | 🟡 | [2026-07-29](https://github.com/SpecterOps/BloodHound/releases)<br>`release` |
| **SharpHound**<br>[GitHub](https://github.com/SpecterOps/SharpHound) | BloodHound data collector for Active Directory | 🟢 | [2026-07-24](https://github.com/SpecterOps/SharpHound/releases)<br>`release` |
| **Impacket**<br>[GitHub](https://github.com/fortra/impacket) | Python collection of Windows network protocol tools | 🟢 | [2026-05-19](https://github.com/fortra/impacket/releases)<br>`release` |
| **NetExec**<br>[GitHub](https://github.com/Pennyw0rth/NetExec) | Network authentication / assessment (CrackMapExec successor) | 🟢 | [2026-02-23](https://github.com/Pennyw0rth/NetExec/releases)<br>`release` |
| **Responder**<br>[GitHub](https://github.com/lgandx/Responder) | LLMNR / NBT-NS / mDNS poisoner for credential capture | 🟢 | [2026-01-26](https://github.com/lgandx/Responder/tags)<br>`tag` |
| **Certipy**<br>[GitHub](https://github.com/ly4k/Certipy) | Active Directory Certificate Services enumeration & abuse | 🟢 | [2026-06-23](https://github.com/ly4k/Certipy/releases)<br>`release` |
| **Rubeus**<br>[GitHub](https://github.com/GhostPack/Rubeus) | Kerberos abuse toolkit for offensive AD ops | 🟢 | [2021-08-03](https://github.com/GhostPack/Rubeus/releases)<br>`release` |
| **PowerView**<br>[GitHub](https://github.com/PowerShellMafia/PowerSploit) | PowerShell AD situational awareness (PowerSploit) | 🟢 | [2015-12-19](https://github.com/PowerShellMafia/PowerSploit/releases)<br>`release` |

---

## 🔑 Password Cracking

| Tool | Description | License | Activity |
|---|---|---|---|
| **Hashcat**<br>[GitHub](https://github.com/hashcat/hashcat) | Advanced GPU password recovery | 🟢 | [2025-08-23](https://github.com/hashcat/hashcat/releases)<br>`release` |
| **John the Ripper**<br>[GitHub](https://github.com/openwall/john) | Fast password cracker (CPU + many formats) | 🟢 | [2013-07-08](https://github.com/openwall/john/tags)<br>`tag` |
| **Hydra**<br>[GitHub](https://github.com/vanhauser-thc/thc-hydra) | Parallel online brute-force for network services | 🟢 | [2026-05-03](https://github.com/vanhauser-thc/thc-hydra/releases)<br>`release` |
| **Medusa**<br>[GitHub](https://github.com/jmk-foofus/medusa) | Speedy, parallel, modular login brute-forcer | 🟢 | [2025-05-14](https://github.com/jmk-foofus/medusa/releases)<br>`release` |

---

## ☁️ Cloud & Container Security

CSPM, CNAPP-adjacent OSS, and Kubernetes hardening.

| Tool | Focus | Description | License | Activity |
|---|---|---|---|---|
| **Prowler**<br>[GitHub](https://github.com/prowler-cloud/prowler) | CSPM | Multi-cloud security assessment (AWS, Azure, GCP, …) | 🟢 | [2026-08-06](https://github.com/prowler-cloud/prowler/releases)<br>`release` |
| **ScoutSuite**<br>[GitHub](https://github.com/nccgroup/ScoutSuite) | CSPM | Multi-cloud security auditing tool | 🟢 | [2024-05-10](https://github.com/nccgroup/ScoutSuite/releases)<br>`release` |
| **CloudMapper**<br>[GitHub](https://github.com/duo-labs/cloudmapper) | AWS | Network visualization and inventory for AWS accounts | 🟢 | [2021-11-04](https://github.com/duo-labs/cloudmapper/releases)<br>`release` |
| **kube-bench**<br>[GitHub](https://github.com/aquasecurity/kube-bench) | Kubernetes | CIS Kubernetes Benchmark checks | 🟢 | [2026-08-05](https://github.com/aquasecurity/kube-bench/releases)<br>`release` |
| **kube-hunter**<br>[GitHub](https://github.com/aquasecurity/kube-hunter) | Kubernetes | Hunt for security weaknesses in K8s clusters | 🟢 | [2022-05-18](https://github.com/aquasecurity/kube-hunter/releases)<br>`release` |
| **Falco**<br>[GitHub](https://github.com/falcosecurity/falco) | Runtime | Cloud-native runtime security / threat detection | 🟢 | [2026-06-11](https://github.com/falcosecurity/falco/releases)<br>`release` |
| **Trivy**<br>[GitHub](https://github.com/aquasecurity/trivy) | Containers / IaC | Image, filesystem, and IaC vulnerability scanner | 🟢 | [2026-08-03](https://github.com/aquasecurity/trivy/releases)<br>`release` |
| **Docker Bench**<br>[GitHub](https://github.com/docker/docker-bench-security) | Containers | CIS Docker Benchmark script | 🟢 | [2023-12-20](https://github.com/docker/docker-bench-security/releases)<br>`release` |
| **Orca Security**<br>[orca.security](https://orca.security/) | CNAPP | Commercial agentless cloud security platform | 🔴 | — |
| **Wiz**<br>[wiz.io](https://www.wiz.io/) | CNAPP | Commercial cloud security platform | 🔴 | — |
| **Prisma Cloud**<br>[paloaltonetworks.com](https://www.paloaltonetworks.com/prisma/cloud) | CNAPP | Commercial CNAPP by Palo Alto Networks | 🔴 | — |

---

## 📡 Network Analysis & IDS

| Tool | Description | License | Activity |
|---|---|---|---|
| **Wireshark**<br>[GitHub](https://github.com/wireshark/wireshark) | Network protocol analyzer | 🟢 | [2025-08-28](https://github.com/wireshark/wireshark/tags)<br>`tag` |
| **tcpdump**<br>[GitHub](https://github.com/the-tcpdump-group/tcpdump) | Classic command-line packet analyzer | 🟢 | [2025-12-30](https://github.com/the-tcpdump-group/tcpdump/tags)<br>`tag` |
| **Zeek**<br>[GitHub](https://github.com/zeek/zeek) | Network security monitoring framework (formerly Bro) | 🟢 | [2026-07-10](https://github.com/zeek/zeek/releases)<br>`release` |
| **Suricata**<br>[GitHub](https://github.com/OISF/suricata) | High-performance IDS / IPS / NSM engine | 🟢 | [2026-07-07](https://github.com/OISF/suricata/releases)<br>`release` |
| **Snort**<br>[GitHub](https://github.com/snort3/snort3) | Network intrusion detection and prevention | 🟢 | [2026-04-23](https://github.com/snort3/snort3/releases)<br>`release` |
| **Wazuh**<br>[GitHub](https://github.com/wazuh/wazuh) | Open-source XDR / SIEM platform | 🟢 | [2026-07-30](https://github.com/wazuh/wazuh/releases)<br>`release` |
| **OSSEC**<br>[GitHub](https://github.com/ossec/ossec-hids) | Host-based intrusion detection system | 🟢 | [2026-08-02](https://github.com/ossec/ossec-hids/releases)<br>`release` |
| **ModSecurity**<br>[GitHub](https://github.com/owasp-modsecurity/ModSecurity) | Open-source web application firewall engine | 🟢 | [2026-06-29](https://github.com/owasp-modsecurity/ModSecurity/releases)<br>`release` |

---

## 🔬 Forensics & Incident Response

| Tool | Description | License | Activity |
|---|---|---|---|
| **Volatility 3**<br>[GitHub](https://github.com/volatilityfoundation/volatility3) | Advanced memory forensics framework | 🟢 | [2026-04-30](https://github.com/volatilityfoundation/volatility3/releases)<br>`release` |
| **Velociraptor**<br>[GitHub](https://github.com/Velocidex/velociraptor) | Endpoint visibility and digital forensics / IR | 🟢 | [2026-06-23](https://github.com/Velocidex/velociraptor/releases)<br>`release` |
| **Autopsy**<br>[GitHub](https://github.com/sleuthkit/autopsy) | Digital forensics platform (GUI on The Sleuth Kit) | 🟢 | [2026-05-07](https://github.com/sleuthkit/autopsy/releases)<br>`release` |
| **The Sleuth Kit**<br>[GitHub](https://github.com/sleuthkit/sleuthkit) | Library and tools for disk image forensics | 🟢 | [2026-04-15](https://github.com/sleuthkit/sleuthkit/releases)<br>`release` |
| **Plaso**<br>[GitHub](https://github.com/log2timeline/plaso) | Super timeline engine for digital forensics | 🟢 | [2026-05-12](https://github.com/log2timeline/plaso/releases)<br>`release` |
| **osquery**<br>[GitHub](https://github.com/osquery/osquery) | SQL-powered operating system instrumentation | 🟢 | [2026-06-24](https://github.com/osquery/osquery/releases)<br>`release` |
| **TheHive**<br>[GitHub](https://github.com/TheHive-Project/TheHive) | Scalable Security Incident Response Platform | 🟢 | [2022-09-13](https://github.com/TheHive-Project/TheHive/releases)<br>`release` |
| **Cortex**<br>[GitHub](https://github.com/TheHive-Project/Cortex) | Observable analysis & active response engine | 🟢 | [2026-06-30](https://github.com/TheHive-Project/Cortex/releases)<br>`release` |

---

## 🧠 Threat Intelligence

| Tool | Description | License | Activity |
|---|---|---|---|
| **MISP**<br>[GitHub](https://github.com/MISP/MISP) | Open-source threat intelligence sharing platform | 🟢 | [2026-07-13](https://github.com/MISP/MISP/releases)<br>`release` |
| **OpenCTI**<br>[GitHub](https://github.com/OpenCTI-Platform/opencti) | Open Cyber Threat Intelligence platform | 🟢 | [2026-08-07](https://github.com/OpenCTI-Platform/opencti/releases)<br>`release` |
| **OpenTAXII**<br>[GitHub](https://github.com/eclecticiq/OpenTAXII) | TAXII server implementation for CTI exchange | 🟢 | [2026-01-05](https://github.com/eclecticiq/OpenTAXII/releases)<br>`release` |
| **YARA**<br>[GitHub](https://github.com/VirusTotal/yara) | Pattern-matching for malware researchers | 🟢 | [2026-07-28](https://github.com/VirusTotal/yara/releases)<br>`release` |
| **Sigma**<br>[GitHub](https://github.com/SigmaHQ/sigma) | Generic signature format for SIEM systems | 🟢 | [2026-07-09](https://github.com/SigmaHQ/sigma/releases)<br>`release` |
| **AbuseIPDB**<br>[abuseipdb.com](https://www.abuseipdb.com/) | IP abuse reporting and reputation database | ☁️ | — |
| **VirusTotal**<br>[virustotal.com](https://www.virustotal.com/) | Multi-engine file / URL malware analysis | ☁️ | — |
| **AlienVault OTX**<br>[otx.alienvault.com](https://otx.alienvault.com/) | Open Threat Exchange community intel | ☁️ | — |
| **Hudson Rock**<br>[hudsonrock.com](https://www.hudsonrock.com/) | Infostealer / cybercrime intelligence | ☁️ | — |

---

## 🕳️ Breach & Leak Lookup

Credential and leak monitoring / digital risk protection lookups.

| Tool | Description | License | Activity |
|---|---|---|---|
| **Have I Been Pwned**<br>[haveibeenpwned.com](https://haveibeenpwned.com/) | Check if emails / passwords appear in known breaches | ☁️ | — |
| **DeHashed**<br>[dehashed.com](https://dehashed.com/) | Breach data search for credentials, WHOIS, and monitoring | ☁️ | — |
| **Intelligence X**<br>[intelx.io](https://intelx.io/) | Search leaked and historical data | ☁️ | — |
| **LeakIX**<br>[leakix.net](https://leakix.net/) | Search engine for publicly exposed services and leaks | ☁️ | — |
| **Hudson Rock**<br>[hudsonrock.com](https://cavalier.hudsonrock.com/) | Free / paid infostealer compromise checks | ☁️ | — |

---

## 🧬 Binary Analysis & Reverse Engineering

| Tool | Description | License | Activity |
|---|---|---|---|
| **Ghidra**<br>[GitHub](https://github.com/NationalSecurityAgency/ghidra) | NSA open-source software reverse engineering suite | 🟢 | [2026-06-05](https://github.com/NationalSecurityAgency/ghidra/releases)<br>`release` |
| **radare2**<br>[GitHub](https://github.com/radareorg/radare2) | UNIX-like reverse engineering framework | 🟢 | [2026-08-07](https://github.com/radareorg/radare2/releases)<br>`release` |
| **Cutter**<br>[GitHub](https://github.com/rizinorg/cutter) | Free GUI for Rizin / reverse engineering | 🟢 | [2026-06-30](https://github.com/rizinorg/cutter/releases)<br>`release` |
| **Binary Ninja**<br>[binary.ninja](https://binary.ninja/) | Commercial reverse engineering platform | 🔴 | — |
| **IDA**<br>[hex-rays.com](https://hex-rays.com/ida-pro/) | Commercial industry-standard disassembler / debugger | 🔴 | — |
| **Binwalk**<br>[GitHub](https://github.com/ReFirmLabs/binwalk) | Firmware analysis and extraction tool | 🟢 | [2024-10-31](https://github.com/ReFirmLabs/binwalk/releases)<br>`release` |
| **PE-bear**<br>[GitHub](https://github.com/hasherezade/pe-bear) | PE file reversing toolkit | 🟢 | [2026-06-05](https://github.com/hasherezade/pe-bear/releases)<br>`release` |
| **Detect It Easy**<br>[GitHub](https://github.com/horsicq/Detect-It-Easy) | Packer / compiler / crypto detection for binaries | 🟢 | [2026-04-16](https://github.com/horsicq/Detect-It-Easy/tags)<br>`tag` |

---

## 📚 Wordlists & Payloads

| Tool | Description | License | Activity |
|---|---|---|---|
| **SecLists**<br>[GitHub](https://github.com/danielmiessler/SecLists) | Collection of security wordlists and payloads | 🟢 | [2026-03-23](https://github.com/danielmiessler/SecLists/releases)<br>`release` |
| **PayloadsAllTheThings**<br>[GitHub](https://github.com/swisskyrepo/PayloadsAllTheThings) | Useful payloads and bypasses for Web AppSec | 🟢 | [2025-07-26](https://github.com/swisskyrepo/PayloadsAllTheThings/releases)<br>`release` |
| **FuzzDB**<br>[GitHub](https://github.com/fuzzdb-project/fuzzdb) | Attack patterns, discovery dictionaries, and injectables | 🟢 | [2020-02-26](https://github.com/fuzzdb-project/fuzzdb/commits)<br>`commit` |
| **Assetnote Wordlists**<br>[assetnote.io](https://wordlists.assetnote.io/) | High-quality discovery wordlists | 🌐 | — |

---

## 📚 Vulnerability Databases

| Source | Description | License |
|---|---|---|
| **CVE**<br>[cve.org](https://www.cve.org/) | Common catalog of public vulnerability identifiers | 🌐 |
| **NVD (NIST)**<br>[nvd.nist.gov](https://nvd.nist.gov/) | U.S. SCAP / CVE repository with CVSS, CPE, and references | 🌐 |
| **Exploit-DB**<br>[exploit-db.com](https://www.exploit-db.com/) | Archive of exploits, shellcode, and advisories | 🌐 |
| **0day.today**<br>[0day.today](http://0day.today/) | Exploit and 0day database for researchers | ☁️ |
| **VulDB**<br>[vuldb.com](https://vuldb.com/) | Documented vulnerabilities and exploits | ☁️ |
| **Snyk Vuln DB**<br>[snyk.io](https://security.snyk.io/) | OSS vulnerability DB with remediation guidance | ☁️ |
| **OSV**<br>[osv.dev](https://osv.dev/) | Distributed open-source vulnerability database | 🌐 |
| **GitHub Advisory**<br>[GitHub](https://github.com/advisories) | Security advisories for package ecosystems | 🌐 |
| **FSTEC BDU**<br>[bdu.fstec.ru](https://bdu.fstec.ru/) | Russian threat / vulnerability data bank | 🌐 |

---

## 🔗 External directories

Broader catalogs for discovering additional commercial and free products:

| Directory | Focus | License |
|---|---|---|
| **OWASP**<br>[owasp.org](https://owasp.org/) | Projects, cheat sheets, and Top 10 lists | 🌐 |
| **awesome-security**<br>[GitHub](https://github.com/sbilly/awesome-security) | Curated awesome-list of security resources | 🟢 |

---

## Category legend

| Abbreviation | Meaning |
|---|---|
| **OSINT** | Open Source Intelligence |
| **SAST** | Static Application Security Testing |
| **DAST** | Dynamic Application Security Testing |
| **IAST** | Interactive Application Security Testing |
| **SCA** | Software Composition Analysis |
| **IaC** | Infrastructure as Code |
| **SBOM** | Software Bill of Materials |
| **CSPM** | Cloud Security Posture Management |
| **CNAPP** | Cloud-Native Application Protection Platform |
| **C2** | Command and Control |
| **VA** | Vulnerability Assessment |
| **DRP** | Digital Risk Protection |

---

> **Disclaimer:** These tools are intended for authorized security testing, education, and research. Use them only on systems you own or have explicit permission to assess.
