# SecTools

A curated collection of open-source and public tools for OSINT, vulnerability analysis, AppSec (SAST / DAST / SCA), recon, cloud security, and related security workflows.

Most tools are UNIX-compatible. The **License** column uses icons (see legend below).

### License legend

| Icon | Meaning |
|---|---|
| 🟢 | **Open source** — Apache, MIT, GPL, BSD, AGPL, etc. |
| 🟡 | **Freemium** — free / community edition + paid enterprise tiers |
| 🔴 | **Enterprise** — commercial proprietary license |
| ☁️ | **Service** — hosted SaaS / online platform |
| 🌐 | **Public** — free public resource or dataset |

Last-update badges use [shields.io](https://shields.io) `github/last-commit` (`flat-square`). Non-GitHub products show `—`.

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

| Tool | Description | License | Last update |
|---|---|---|---|
| [Sherlock](https://github.com/sherlock-project/sherlock) | Hunt usernames across hundreds of social networks | 🟢 | [![last commit](https://img.shields.io/github/last-commit/sherlock-project/sherlock?style=flat-square&label=updated)](https://github.com/sherlock-project/sherlock)(https://github.com/sherlock-project/sherlock) |
| [theHarvester](https://github.com/laramies/theHarvester) | Gather emails, subdomains, hosts, and people from public sources | 🟢 | [![last commit](https://img.shields.io/github/last-commit/laramies/theHarvester?style=flat-square&label=updated)](https://github.com/laramies/theHarvester)(https://github.com/laramies/theHarvester) |
| [SpiderFoot](https://github.com/smicallef/spiderfoot) | Automated OSINT with hundreds of modules and a web UI | 🟢 | [![last commit](https://img.shields.io/github/last-commit/smicallef/spiderfoot?style=flat-square&label=updated)](https://github.com/smicallef/spiderfoot)(https://github.com/smicallef/spiderfoot) |
| [Recon-ng](https://github.com/lanmaster53/recon-ng) | Modular reconnaissance framework (Metasploit-style) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/lanmaster53/recon-ng?style=flat-square&label=updated)](https://github.com/lanmaster53/recon-ng)(https://github.com/lanmaster53/recon-ng) |
| [Photon](https://github.com/s0md3v/Photon) | Fast crawler for OSINT data extraction from websites | 🟢 | [![last commit](https://img.shields.io/github/last-commit/s0md3v/Photon?style=flat-square&label=updated)](https://github.com/s0md3v/Photon)(https://github.com/s0md3v/Photon) |
| [Maltego](https://www.maltego.com/) | Graph visualization of people, domains, and infrastructure | 🟡 | — |
| [R3CON1Z3R](https://github.com/abdulgaphy/r3con1z3r) | Lightweight OSINT script for target footprinting | 🟢 | [![last commit](https://img.shields.io/github/last-commit/abdulgaphy/r3con1z3r?style=flat-square&label=updated)](https://github.com/abdulgaphy/r3con1z3r)(https://github.com/abdulgaphy/r3con1z3r) |
| [Shodan](https://www.shodan.io/) | Search engine for Internet-connected devices and services | ☁️ | — |
| [Censys](https://search.censys.io/) | Host, certificate, and service indexing | ☁️ | — |
| [ZoomEye](https://www.zoomeye.ai/) | Network asset and device search (Shodan-like) | ☁️ | — |
| [FOFA](https://fofa.info/) | Cyberspace search engine for assets and fingerprints | ☁️ | — |
| [urlscan.io](https://urlscan.io/) | URL / page analysis and snapshots | ☁️ | — |
| [ONYPHE](https://www.onyphe.io/) | Cyber threat intelligence aggregator for IPs, domains, services | ☁️ | — |
| [BuiltWith](https://builtwith.com/) | Detect a site’s technology stack | ☁️ | — |
| [Hunter.io](https://hunter.io/) | Find and verify professional email addresses | ☁️ | — |
| [crt.sh](https://crt.sh/) | Certificate Transparency log search (subdomain discovery) | 🌐 | — |
| [SecurityTrails](https://securitytrails.com/) | Historical DNS, WHOIS, and domain intelligence | ☁️ | — |
| [who.is](https://who.is/) | WHOIS / DNS lookup | 🌐 | — |
| [DNSstuff](https://www.dnsstuff.com) | DNS diagnostics and lookup utilities | ☁️ | — |
| [InfoSniper](https://www.infosniper.net/) | IP geolocation | 🌐 | — |
| [scans.io](https://scans.io/) | Internet-wide scan data archive | 🌐 | — |
| [Wayback Machine](https://web.archive.org/) | Historical snapshots of web pages | 🌐 | — |
| [IntelX](https://intelx.io/) | Search engine for leaked / archived data and IDs | ☁️ | — |

### Localized search engines

| Region | Link |
|---|---|
| Slovenia | [Najdi.si](http://www.najdi.si/) |
| Israel | [Walla](http://www.walla.co.il/) |
| Japan | [Goo](http://www.goo.ne.jp/) |
| South Korea | [Naver](http://www.naver.com/) |
| China | [Baidu](http://www.baidu.com/) |
| Russia | [Yandex](http://www.yandex.com/) |

### File search

| ☁️ | Description | License |
|---|---|---|
| [FileChef](https://www.filechef.com/) | Search publicly exposed files | ☁️ |
| [File Search Engine](https://www.filesearch.link/) | Index of publicly available files | ☁️ |
| [SearchFiles.de](https://searchfiles.de/) | Search files by name / type | ☁️ |
| [FileListing](https://filelisting.com/) | Catalog of open file listings | ☁️ |

---

## 🛡️ Vulnerability Management Platforms

Orchestrate scanner findings, triage, and reporting.

| Tool | Description | License | Last update |
|---|---|---|---|
| [DefectDojo](https://github.com/DefectDojo/django-DefectDojo) | DevSecOps platform: report import, triage, metrics, SLA | 🟢 | [![last commit](https://img.shields.io/github/last-commit/DefectDojo/django-DefectDojo?style=flat-square&label=updated)](https://github.com/DefectDojo/django-DefectDojo)(https://github.com/DefectDojo/django-DefectDojo) |
| [Faraday](https://github.com/infobyte/faraday) | Collaborative pentest IDE / vulnerability management | 🟢 | [![last commit](https://img.shields.io/github/last-commit/infobyte/faraday?style=flat-square&label=updated)](https://github.com/infobyte/faraday)(https://github.com/infobyte/faraday) |
| [ArcherySec](https://github.com/archerysec/archerysec) | Vulnerability assessment & management with scanner integrations | 🟢 | [![last commit](https://img.shields.io/github/last-commit/archerysec/archerysec?style=flat-square&label=updated)](https://github.com/archerysec/archerysec)(https://github.com/archerysec/archerysec) |
| [reNgine](https://github.com/yogeshojha/rengine) | Automated recon + vulnerability management with web UI | 🟢 | [![last commit](https://img.shields.io/github/last-commit/yogeshojha/rengine?style=flat-square&label=updated)](https://github.com/yogeshojha/rengine)(https://github.com/yogeshojha/rengine) |
| [Vuls](https://github.com/future-architect/vuls) | Agentless vulnerability scanner for Linux / FreeBSD | 🟢 | [![last commit](https://img.shields.io/github/last-commit/future-architect/vuls?style=flat-square&label=updated)](https://github.com/future-architect/vuls)(https://github.com/future-architect/vuls) |
| [OWASP Threat Dragon](https://github.com/OWASP/threat-dragon) | Threat modeling tool for STRIDE-style diagrams | 🟢 | [![last commit](https://img.shields.io/github/last-commit/OWASP/threat-dragon?style=flat-square&label=updated)](https://github.com/OWASP/threat-dragon)(https://github.com/OWASP/threat-dragon) |

---

## ⚒️ Analysis & Exploit Frameworks

| Tool | Category | Description | License | Last update |
|---|---|---|---|---|
| [Metasploit](https://github.com/rapid7/metasploit-framework) | Exploit Framework | Classic exploit, payload, and post-exploitation framework | 🟡 | [![last commit](https://img.shields.io/github/last-commit/rapid7/metasploit-framework?style=flat-square&label=updated)](https://github.com/rapid7/metasploit-framework)(https://github.com/rapid7/metasploit-framework) |
| [RouterSploit](https://github.com/threat9/routersploit) | Exploit Framework | Exploits and checks for embedded / network devices | 🟢 | [![last commit](https://img.shields.io/github/last-commit/threat9/routersploit?style=flat-square&label=updated)](https://github.com/threat9/routersploit)(https://github.com/threat9/routersploit) |
| [BeEF](https://github.com/beefproject/beef) | Exploit Framework | Browser Exploitation Framework | 🟢 | [![last commit](https://img.shields.io/github/last-commit/beefproject/beef?style=flat-square&label=updated)](https://github.com/beefproject/beef)(https://github.com/beefproject/beef) |
| [Sliver](https://github.com/BishopFox/sliver) | C2 | Open-source adversary emulation / C2 framework | 🟢 | [![last commit](https://img.shields.io/github/last-commit/BishopFox/sliver?style=flat-square&label=updated)](https://github.com/BishopFox/sliver)(https://github.com/BishopFox/sliver) |
| [Havoc](https://github.com/HavocFramework/Havoc) | C2 | Modern post-exploitation command and control | 🟢 | [![last commit](https://img.shields.io/github/last-commit/HavocFramework/Havoc?style=flat-square&label=updated)](https://github.com/HavocFramework/Havoc)(https://github.com/HavocFramework/Havoc) |
| [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | Mobile | Static and dynamic analysis for Android / iOS | 🟢 | [![last commit](https://img.shields.io/github/last-commit/MobSF/Mobile-Security-Framework-MobSF?style=flat-square&label=updated)](https://github.com/MobSF/Mobile-Security-Framework-MobSF)(https://github.com/MobSF/Mobile-Security-Framework-MobSF) |
| [Frida](https://github.com/frida/frida) | Dynamic Instrumentation | Dynamic instrumentation toolkit for apps | 🟢 | [![last commit](https://img.shields.io/github/last-commit/frida/frida?style=flat-square&label=updated)](https://github.com/frida/frida)(https://github.com/frida/frida) |
| [Objection](https://github.com/sensepost/objection) | Mobile | Runtime mobile exploration powered by Frida | 🟢 | [![last commit](https://img.shields.io/github/last-commit/sensepost/objection?style=flat-square&label=updated)](https://github.com/sensepost/objection)(https://github.com/sensepost/objection) |
| [RedTeam C# Scripts](https://github.com/Mr-Un1k0d3r/RedTeamCSharpScripts) | Red Team | Collection of C# scripts for red team operations | 🟢 | [![last commit](https://img.shields.io/github/last-commit/Mr-Un1k0d3r/RedTeamCSharpScripts?style=flat-square&label=updated)](https://github.com/Mr-Un1k0d3r/RedTeamCSharpScripts)(https://github.com/Mr-Un1k0d3r/RedTeamCSharpScripts) |
| [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) | Adversary Emulation | Small, focused tests mapped to ATT&CK techniques | 🟢 | [![last commit](https://img.shields.io/github/last-commit/redcanaryco/atomic-red-team?style=flat-square&label=updated)](https://github.com/redcanaryco/atomic-red-team)(https://github.com/redcanaryco/atomic-red-team) |
| [CALDERA](https://github.com/mitre/caldera) | Adversary Emulation | Automated adversary emulation platform by MITRE | 🟢 | [![last commit](https://img.shields.io/github/last-commit/mitre/caldera?style=flat-square&label=updated)](https://github.com/mitre/caldera)(https://github.com/mitre/caldera) |

---

## 🧰 Web Proxies & Manual Testing

Intercept, replay, and mutate HTTP(S) traffic during web assessments.

| Tool | Description | License | Last update |
|---|---|---|---|
| [Burp Suite](https://portswigger.net/burp) | Industry-standard web security testing platform (Community / Pro) | 🟡 | — |
| [Caido](https://caido.io/) | Modern lightweight web proxy for bug bounty and pentest | 🟡 | [![last commit](https://img.shields.io/github/last-commit/caido/caido?style=flat-square&label=updated)](https://github.com/caido/caido)(https://github.com/caido/caido) |
| [mitmproxy](https://github.com/mitmproxy/mitmproxy) | Interactive TLS-capable intercepting HTTP proxy (CLI + web) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/mitmproxy/mitmproxy?style=flat-square&label=updated)](https://github.com/mitmproxy/mitmproxy)(https://github.com/mitmproxy/mitmproxy) |
| [OWASP ZAP](https://github.com/zaproxy/zaproxy) | Free proxy + automated scanner | 🟢 | [![last commit](https://img.shields.io/github/last-commit/zaproxy/zaproxy?style=flat-square&label=updated)](https://github.com/zaproxy/zaproxy)(https://github.com/zaproxy/zaproxy) |
| [WATOBO](https://github.com/siberas/watobo) | Intercepting proxy + scanner for pentests | 🟢 | [![last commit](https://img.shields.io/github/last-commit/siberas/watobo?style=flat-square&label=updated)](https://github.com/siberas/watobo)(https://github.com/siberas/watobo) |

---

## 🔎 SAST — Static Analysis

Find vulnerabilities in source code without running the application.

| Tool | Languages / scope | Description | License | Last update |
|---|---|---|---|---|
| [Semgrep](https://github.com/semgrep/semgrep) | 30+ languages | Fast pattern-based SAST with YAML rules; CI-friendly | 🟡 | [![last commit](https://img.shields.io/github/last-commit/semgrep/semgrep?style=flat-square&label=updated)](https://github.com/semgrep/semgrep)(https://github.com/semgrep/semgrep) |
| [CodeQL](https://codeql.github.com/) | Multilang | Semantic code analysis from GitHub (query-as-code) | 🟡 | — |
| [Bearer](https://github.com/Bearer/bearer) | JS/TS, Ruby, PHP, Java, Go, Python | SAST focused on data flows and privacy | 🟢 | [![last commit](https://img.shields.io/github/last-commit/Bearer/bearer?style=flat-square&label=updated)](https://github.com/Bearer/bearer)(https://github.com/Bearer/bearer) |
| [Bandit](https://github.com/PyCQA/bandit) | Python | Common security issues in Python | 🟢 | [![last commit](https://img.shields.io/github/last-commit/PyCQA/bandit?style=flat-square&label=updated)](https://github.com/PyCQA/bandit)(https://github.com/PyCQA/bandit) |
| [Brakeman](https://github.com/presidentbeef/brakeman) | Ruby on Rails | Rails-focused static security scanner | 🟢 | [![last commit](https://img.shields.io/github/last-commit/presidentbeef/brakeman?style=flat-square&label=updated)](https://github.com/presidentbeef/brakeman)(https://github.com/presidentbeef/brakeman) |
| [Find Security Bugs](https://github.com/find-sec-bugs/find-sec-bugs) | Java, Android, Scala, Kotlin, Groovy | SpotBugs plugin for web / Android security | 🟢 | [![last commit](https://img.shields.io/github/last-commit/find-sec-bugs/find-sec-bugs?style=flat-square&label=updated)](https://github.com/find-sec-bugs/find-sec-bugs)(https://github.com/find-sec-bugs/find-sec-bugs) |
| [SpotBugs](https://github.com/spotbugs/spotbugs) | Java | Static analysis of Java bytecode | 🟢 | [![last commit](https://img.shields.io/github/last-commit/spotbugs/spotbugs?style=flat-square&label=updated)](https://github.com/spotbugs/spotbugs)(https://github.com/spotbugs/spotbugs) |
| [PMD](https://github.com/pmd/pmd) | Multilang | Static analysis for quality and security rules | 🟢 | [![last commit](https://img.shields.io/github/last-commit/pmd/pmd?style=flat-square&label=updated)](https://github.com/pmd/pmd)(https://github.com/pmd/pmd) |
| [Security Code Scan](https://github.com/security-code-scan/security-code-scan) | C#, VB.NET | Roslyn analyzer for .NET vulnerabilities | 🟢 | [![last commit](https://img.shields.io/github/last-commit/security-code-scan/security-code-scan?style=flat-square&label=updated)](https://github.com/security-code-scan/security-code-scan)(https://github.com/security-code-scan/security-code-scan) |
| [Infer#](https://github.com/microsoft/infersharp) | C# | Interprocedural .NET analysis based on Facebook Infer | 🟢 | [![last commit](https://img.shields.io/github/last-commit/microsoft/infersharp?style=flat-square&label=updated)](https://github.com/microsoft/infersharp)(https://github.com/microsoft/infersharp) |
| [Insider](https://github.com/insidersec/insider) | Java, Kotlin, Swift, .NET, JS | CLI SAST for multiple stacks | 🟢 | [![last commit](https://img.shields.io/github/last-commit/insidersec/insider?style=flat-square&label=updated)](https://github.com/insidersec/insider)(https://github.com/insidersec/insider) |
| [Codechecker](https://github.com/Ericsson/codechecker) | C/C++ | Wrapper around Clang Static Analyzer / Clang-Tidy | 🟢 | [![last commit](https://img.shields.io/github/last-commit/Ericsson/codechecker?style=flat-square&label=updated)](https://github.com/Ericsson/codechecker)(https://github.com/Ericsson/codechecker) |
| [Cppcheck](https://github.com/danmar/cppcheck) | C/C++ | Static analysis focused on undefined behavior | 🟢 | [![last commit](https://img.shields.io/github/last-commit/danmar/cppcheck?style=flat-square&label=updated)](https://github.com/danmar/cppcheck)(https://github.com/danmar/cppcheck) |
| [LLVM Clang SA](https://github.com/llvm/llvm-project) | C, C++, Obj-C | Clang Static Analyzer | 🟢 | [![last commit](https://img.shields.io/github/last-commit/llvm/llvm-project?style=flat-square&label=updated)](https://github.com/llvm/llvm-project)(https://github.com/llvm/llvm-project) |
| [PVS-Studio](https://pvs-studio.com/) | Multilang | Commercial static analyzer (trial available) | 🔴 | — |
| [Codemodder](https://github.com/pixee/codemodder-python) | Java, Python | Auto-fix for security and quality issues | 🟢 | [![last commit](https://img.shields.io/github/last-commit/pixee/codemodder-python?style=flat-square&label=updated)](https://github.com/pixee/codemodder-python)(https://github.com/pixee/codemodder-python) |
| [gosec](https://github.com/securego/gosec) | Go | Inspector for security problems in Go code | 🟢 | [![last commit](https://img.shields.io/github/last-commit/securego/gosec?style=flat-square&label=updated)](https://github.com/securego/gosec)(https://github.com/securego/gosec) |
| [PHP Vulnerability Hunter](https://github.com/OneSourceCat/phpvulhunter) | PHP | PHP vulnerability finder (legacy) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/OneSourceCat/phpvulhunter?style=flat-square&label=updated)](https://github.com/OneSourceCat/phpvulhunter)(https://github.com/OneSourceCat/phpvulhunter) |
| [Cobra](https://github.com/wufeifei/cobra) | PHP, Java | Source code security audit (legacy) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/wufeifei/cobra?style=flat-square&label=updated)](https://github.com/wufeifei/cobra)(https://github.com/wufeifei/cobra) |

---

## 🎯 DAST / IAST

Dynamic and interactive analysis of running applications.

| Tool | Type | Description | License | Last update |
|---|---|---|---|---|
| [OWASP ZAP](https://github.com/zaproxy/zaproxy) | DAST | Free web proxy and automated scanner from OWASP | 🟢 | [![last commit](https://img.shields.io/github/last-commit/zaproxy/zaproxy?style=flat-square&label=updated)](https://github.com/zaproxy/zaproxy)(https://github.com/zaproxy/zaproxy) |
| [Nuclei](https://github.com/projectdiscovery/nuclei) | DAST | Fast YAML-template scanner for CVE / misconfig (HTTP, DNS, TCP…) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/projectdiscovery/nuclei?style=flat-square&label=updated)](https://github.com/projectdiscovery/nuclei)(https://github.com/projectdiscovery/nuclei) |
| [Nikto](https://github.com/sullo/nikto) | DAST | Classic web scanner for dangerous files and misconfigurations | 🟢 | [![last commit](https://img.shields.io/github/last-commit/sullo/nikto?style=flat-square&label=updated)](https://github.com/sullo/nikto)(https://github.com/sullo/nikto) |
| [Wapiti](https://github.com/wapiti-scanner/wapiti) | DAST | Black-box web scanner (XSS, SQLi, and more) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/wapiti-scanner/wapiti?style=flat-square&label=updated)](https://github.com/wapiti-scanner/wapiti)(https://github.com/wapiti-scanner/wapiti) |
| [w3af](https://github.com/andresriancho/w3af) | DAST | Web Application Attack and Audit Framework | 🟢 | [![last commit](https://img.shields.io/github/last-commit/andresriancho/w3af?style=flat-square&label=updated)](https://github.com/andresriancho/w3af)(https://github.com/andresriancho/w3af) |
| [Dalfox](https://github.com/hahwul/dalfox) | XSS | Parameter analysis and XSS scanning / exploitation helper | 🟢 | [![last commit](https://img.shields.io/github/last-commit/hahwul/dalfox?style=flat-square&label=updated)](https://github.com/hahwul/dalfox)(https://github.com/hahwul/dalfox) |
| [Commix](https://github.com/commixproject/commix) | Command Injection | Automated OS command injection detection and exploitation | 🟢 | [![last commit](https://img.shields.io/github/last-commit/commixproject/commix?style=flat-square&label=updated)](https://github.com/commixproject/commix)(https://github.com/commixproject/commix) |
| [jwt_tool](https://github.com/ticarpi/jwt_tool) | API / Auth | Toolkit for testing, forging, and attacking JWTs | 🟢 | [![last commit](https://img.shields.io/github/last-commit/ticarpi/jwt_tool?style=flat-square&label=updated)](https://github.com/ticarpi/jwt_tool)(https://github.com/ticarpi/jwt_tool) |
| [Snyk](https://github.com/snyk/cli) | DAST / SCA | Scan code, dependencies, containers, and IaC | 🟡 | [![last commit](https://img.shields.io/github/last-commit/snyk/cli?style=flat-square&label=updated)](https://github.com/snyk/cli)(https://github.com/snyk/cli) |
| [SonarQube](https://github.com/SonarSource/sonarqube) | SAST / Quality | Code quality + security hotspots | 🟡 | [![last commit](https://img.shields.io/github/last-commit/SonarSource/sonarqube?style=flat-square&label=updated)](https://github.com/SonarSource/sonarqube)(https://github.com/SonarSource/sonarqube) |
| [Contrast Security](https://www.contrastsecurity.com/) | IAST | Agent-based interactive analysis at runtime | 🔴 | — |
| [PT Application Inspector](https://www.ptsecurity.com/ww-en/products/ai/) | SAST/DAST | Commercial application analyzer (Positive Technologies) | 🔴 | — |
| [CloudSploit](https://github.com/aquasecurity/cloudsploit) | Cloud | Misconfiguration checks for AWS / Azure / GCP / Oracle | 🟢 | [![last commit](https://img.shields.io/github/last-commit/aquasecurity/cloudsploit?style=flat-square&label=updated)](https://github.com/aquasecurity/cloudsploit)(https://github.com/aquasecurity/cloudsploit) |
| [Mend (WhiteSource)](https://www.mend.io/) | SCA / AppSec | Commercial open-source risk platform | 🔴 | — |

---

## 📦 SCA / IaC

Dependency and infrastructure-as-code analysis.

| Tool | Focus | Description | License | Last update |
|---|---|---|---|---|
| [Trivy](https://github.com/aquasecurity/trivy) | SCA + IaC + Containers | All-in-one: deps, images, IaC, secrets | 🟢 | [![last commit](https://img.shields.io/github/last-commit/aquasecurity/trivy?style=flat-square&label=updated)](https://github.com/aquasecurity/trivy)(https://github.com/aquasecurity/trivy) |
| [Grype](https://github.com/anchore/grype) | SCA / Containers | Vulnerability scanner for images and filesystems | 🟢 | [![last commit](https://img.shields.io/github/last-commit/anchore/grype?style=flat-square&label=updated)](https://github.com/anchore/grype)(https://github.com/anchore/grype) |
| [OSV-Scanner](https://github.com/google/osv-scanner) | SCA | Scanner powered by [OSV.dev](https://osv.dev) (Google) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/google/osv-scanner?style=flat-square&label=updated)](https://github.com/google/osv-scanner)(https://github.com/google/osv-scanner) |
| [Dependency-Track](https://github.com/DependencyTrack/dependency-track) | SCA Platform | Continuous analysis platform for SBOM / dependencies | 🟢 | [![last commit](https://img.shields.io/github/last-commit/DependencyTrack/dependency-track?style=flat-square&label=updated)](https://github.com/DependencyTrack/dependency-track)(https://github.com/DependencyTrack/dependency-track) |
| [OWASP Dependency-Check](https://github.com/jeremylong/DependencyCheck) | SCA | Match dependencies against known CVE | 🟢 | [![last commit](https://img.shields.io/github/last-commit/jeremylong/DependencyCheck?style=flat-square&label=updated)](https://github.com/jeremylong/DependencyCheck)(https://github.com/jeremylong/DependencyCheck) |
| [Checkov](https://github.com/bridgecrewio/checkov) | IaC | Policy-as-code for Terraform, K8s, CloudFormation, Docker | 🟢 | [![last commit](https://img.shields.io/github/last-commit/bridgecrewio/checkov?style=flat-square&label=updated)](https://github.com/bridgecrewio/checkov)(https://github.com/bridgecrewio/checkov) |
| [KICS](https://github.com/Checkmarx/kics) | IaC | Keeping Infrastructure as Code Secure — multi-IaC scanner | 🟢 | [![last commit](https://img.shields.io/github/last-commit/Checkmarx/kics?style=flat-square&label=updated)](https://github.com/Checkmarx/kics)(https://github.com/Checkmarx/kics) |
| [tfsec](https://github.com/aquasecurity/tfsec) | IaC | Terraform security scanner (Trivy lineage) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/aquasecurity/tfsec?style=flat-square&label=updated)](https://github.com/aquasecurity/tfsec)(https://github.com/aquasecurity/tfsec) |
| [Terrascan](https://github.com/tenable/terrascan) | IaC | Compliance / security scanning for IaC | 🟢 | [![last commit](https://img.shields.io/github/last-commit/tenable/terrascan?style=flat-square&label=updated)](https://github.com/tenable/terrascan)(https://github.com/tenable/terrascan) |

---

## 📋 SBOM

Software Bill of Materials generation.

| Tool | Format | Description | License | Last update |
|---|---|---|---|---|
| [Syft](https://github.com/anchore/syft) | SPDX, CycloneDX | Generate SBOM from images, directories, and manifests | 🟢 | [![last commit](https://img.shields.io/github/last-commit/anchore/syft?style=flat-square&label=updated)](https://github.com/anchore/syft)(https://github.com/anchore/syft) |
| [cdxgen](https://github.com/CycloneDX/cdxgen) | CycloneDX | Universal CycloneDX SBOM generator | 🟢 | [![last commit](https://img.shields.io/github/last-commit/CycloneDX/cdxgen?style=flat-square&label=updated)](https://github.com/CycloneDX/cdxgen)(https://github.com/CycloneDX/cdxgen) |
| [Trivy](https://github.com/aquasecurity/trivy) | SPDX, CycloneDX | SBOM as part of scanning | 🟢 | [![last commit](https://img.shields.io/github/last-commit/aquasecurity/trivy?style=flat-square&label=updated)](https://github.com/aquasecurity/trivy)(https://github.com/aquasecurity/trivy) |

---

## 🔐 Secret Detection

| Tool | Description | License | Last update |
|---|---|---|---|
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Fast secret detection in git history and filesystem | 🟢 | [![last commit](https://img.shields.io/github/last-commit/gitleaks/gitleaks?style=flat-square&label=updated)](https://github.com/gitleaks/gitleaks)(https://github.com/gitleaks/gitleaks) |
| [TruffleHog](https://github.com/trufflesecurity/trufflehog) | Secret detection with live verification (API keys, etc.) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/trufflesecurity/trufflehog?style=flat-square&label=updated)](https://github.com/trufflesecurity/trufflehog)(https://github.com/trufflesecurity/trufflehog) |
| [git-secret](https://github.com/sobolevn/git-secret) | Encrypt secrets in git via GPG | 🟢 | [![last commit](https://img.shields.io/github/last-commit/sobolevn/git-secret?style=flat-square&label=updated)](https://github.com/sobolevn/git-secret)(https://github.com/sobolevn/git-secret) |
| [detect-secrets](https://github.com/Yelp/detect-secrets) | Enterprise-friendly baseline secret scanner (Yelp) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/Yelp/detect-secrets?style=flat-square&label=updated)](https://github.com/Yelp/detect-secrets)(https://github.com/Yelp/detect-secrets) |

---

## 🛰️ Scanners

Network, web, and general-purpose vulnerability scanners.

| Tool | Type | Description | License | Last update |
|---|---|---|---|---|
| [Nmap](https://github.com/nmap/nmap) | Network | Reference network discovery / port scanner | 🟢 | [![last commit](https://img.shields.io/github/last-commit/nmap/nmap?style=flat-square&label=updated)](https://github.com/nmap/nmap)(https://github.com/nmap/nmap) |
| [Masscan](https://github.com/robertdavidgraham/masscan) | Network | Asynchronous ultra-fast port scanner | 🟢 | [![last commit](https://img.shields.io/github/last-commit/robertdavidgraham/masscan?style=flat-square&label=updated)](https://github.com/robertdavidgraham/masscan)(https://github.com/robertdavidgraham/masscan) |
| [RustScan](https://github.com/RustScan/RustScan) | Network | Extremely fast port scanner that pipes into Nmap | 🟢 | [![last commit](https://img.shields.io/github/last-commit/RustScan/RustScan?style=flat-square&label=updated)](https://github.com/RustScan/RustScan)(https://github.com/RustScan/RustScan) |
| [OpenVAS / Greenbone](https://github.com/greenbone/openvas-scanner) | Network VA | Full vulnerability assessment stack | 🟢 | [![last commit](https://img.shields.io/github/last-commit/greenbone/openvas-scanner?style=flat-square&label=updated)](https://github.com/greenbone/openvas-scanner)(https://github.com/greenbone/openvas-scanner) |
| [Nessus](https://www.tenable.com/products/nessus) | Network VA | Commercial VA scanner by Tenable | 🔴 | — |
| [InsightVM (Nexpose)](https://www.rapid7.com/products/insightvm/) | Network VA | Vulnerability management by Rapid7 | 🔴 | — |
| [Tsunami](https://github.com/google/tsunami-security-scanner) | Network | Modular high-severity scanner by Google | 🟢 | [![last commit](https://img.shields.io/github/last-commit/google/tsunami-security-scanner?style=flat-square&label=updated)](https://github.com/google/tsunami-security-scanner)(https://github.com/google/tsunami-security-scanner) |
| [testssl.sh](https://github.com/drwetter/testssl.sh) | TLS / SSL | CLI checker for TLS/SSL ciphers, protocols, and vulns | 🟢 | [![last commit](https://img.shields.io/github/last-commit/drwetter/testssl.sh?style=flat-square&label=updated)](https://github.com/drwetter/testssl.sh)(https://github.com/drwetter/testssl.sh) |
| [SSLyze](https://github.com/nabla-c0d3/sslyze) | TLS / SSL | Fast and powerful SSL/TLS scanning library | 🟢 | [![last commit](https://img.shields.io/github/last-commit/nabla-c0d3/sslyze?style=flat-square&label=updated)](https://github.com/nabla-c0d3/sslyze)(https://github.com/nabla-c0d3/sslyze) |
| [Sqlmap](https://github.com/sqlmapproject/sqlmap) | Web / SQLi | Automated SQL Injection detection and exploitation | 🟢 | [![last commit](https://img.shields.io/github/last-commit/sqlmapproject/sqlmap?style=flat-square&label=updated)](https://github.com/sqlmapproject/sqlmap)(https://github.com/sqlmapproject/sqlmap) |
| [NoSQLMap](https://github.com/codingo/NoSQLMap) | NoSQL | Audit and exploit NoSQL injection | 🟢 | [![last commit](https://img.shields.io/github/last-commit/codingo/NoSQLMap?style=flat-square&label=updated)](https://github.com/codingo/NoSQLMap)(https://github.com/codingo/NoSQLMap) |
| [WhatWeb](https://github.com/urbanadventurer/WhatWeb) | Fingerprint | Identify CMS, frameworks, and site tech | 🟢 | [![last commit](https://img.shields.io/github/last-commit/urbanadventurer/WhatWeb?style=flat-square&label=updated)](https://github.com/urbanadventurer/WhatWeb)(https://github.com/urbanadventurer/WhatWeb) |
| [Wappalyzer](https://www.wappalyzer.com/) | Fingerprint | Identify technologies used on websites | 🟡 | — |
| [wappalyzergo](https://github.com/projectdiscovery/wappalyzergo) | Fingerprint | Go port of Wappalyzer fingerprinting for CLI / pipelines | 🟢 | [![last commit](https://img.shields.io/github/last-commit/projectdiscovery/wappalyzergo?style=flat-square&label=updated)](https://github.com/projectdiscovery/wappalyzergo) |
| [Xray](https://github.com/chaitin/xray) | Web | Passive / active web scanner (Chaitin) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/chaitin/xray?style=flat-square&label=updated)](https://github.com/chaitin/xray)(https://github.com/chaitin/xray) |
| [Osmedeus](https://github.com/j3ssie/Osmedeus) | Orchestration | Workflow engine for automated recon / scan | 🟢 | [![last commit](https://img.shields.io/github/last-commit/j3ssie/Osmedeus?style=flat-square&label=updated)](https://github.com/j3ssie/Osmedeus)(https://github.com/j3ssie/Osmedeus) |
| [OneForAll](https://github.com/shmilylty/OneForAll) | Subdomain / Recon | Powerful subdomain collection | 🟢 | [![last commit](https://img.shields.io/github/last-commit/shmilylty/OneForAll?style=flat-square&label=updated)](https://github.com/shmilylty/OneForAll)(https://github.com/shmilylty/OneForAll) |
| [Sn1per](https://github.com/1N3/Sn1per) | Pentest Automation | Automated pentest framework | 🟡 | [![last commit](https://img.shields.io/github/last-commit/1N3/Sn1per?style=flat-square&label=updated)](https://github.com/1N3/Sn1per)(https://github.com/1N3/Sn1per) |
| [AutoRecon](https://github.com/Tib3rius/AutoRecon) | Recon | Multi-threaded network recon for CTF / pentest | 🟢 | [![last commit](https://img.shields.io/github/last-commit/Tib3rius/AutoRecon?style=flat-square&label=updated)](https://github.com/Tib3rius/AutoRecon)(https://github.com/Tib3rius/AutoRecon) |
| [Legion](https://github.com/GoVanguard/legion) | Network GUI | GUI wrapper around Nmap and other scanners | 🟢 | [![last commit](https://img.shields.io/github/last-commit/GoVanguard/legion?style=flat-square&label=updated)](https://github.com/GoVanguard/legion)(https://github.com/GoVanguard/legion) |
| [Raccoon](https://github.com/evyatarmeged/Raccoon) | Recon | Asynchronous recon / offensive reconnaissance | 🟢 | [![last commit](https://img.shields.io/github/last-commit/evyatarmeged/Raccoon?style=flat-square&label=updated)](https://github.com/evyatarmeged/Raccoon)(https://github.com/evyatarmeged/Raccoon) |
| [Scanless](https://github.com/vesche/scanless) | Network | Port scan via public online scanners (opsec) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/vesche/scanless?style=flat-square&label=updated)](https://github.com/vesche/scanless)(https://github.com/vesche/scanless) |
| [Golismero](https://github.com/golismero/golismero) | Framework | Security framework with plugins | 🟢 | [![last commit](https://img.shields.io/github/last-commit/golismero/golismero?style=flat-square&label=updated)](https://github.com/golismero/golismero)(https://github.com/golismero/golismero) |
| [Arachni](https://github.com/Arachni/arachni) | Web | Modular web scanner (maintenance mode) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/Arachni/arachni?style=flat-square&label=updated)](https://github.com/Arachni/arachni)(https://github.com/Arachni/arachni) |
| [Acunetix](https://www.acunetix.com/) | Web | Commercial DAST | 🔴 | — |
| [Invicti (Netsparker)](https://www.invicti.com/) | Web | Commercial DAST with proof-based scanning | 🔴 | — |
| [ScanOval](https://bdu.fstec.ru/site/scanoval) | OVAL / BDU | OVAL-based vulnerability checks (FSTEC BDU) | 🌐 | — |
| [Puma Scan](https://github.com/pumasecurity/puma-scan) | .NET SAST | Roslyn analyzer for .NET security | 🟡 | [![last commit](https://img.shields.io/github/last-commit/pumasecurity/puma-scan?style=flat-square&label=updated)](https://github.com/pumasecurity/puma-scan)(https://github.com/pumasecurity/puma-scan) |

---

## 🧭 Recon & Enumeration

| Tool | Description | License | Last update |
|---|---|---|---|
| [Amass](https://github.com/owasp-amass/amass) | OWASP: deep subdomain enumeration and attack-surface mapping | 🟢 | [![last commit](https://img.shields.io/github/last-commit/owasp-amass/amass?style=flat-square&label=updated)](https://github.com/owasp-amass/amass)(https://github.com/owasp-amass/amass) |
| [subfinder](https://github.com/projectdiscovery/subfinder) | Passive subdomain discovery (ProjectDiscovery) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/projectdiscovery/subfinder?style=flat-square&label=updated)](https://github.com/projectdiscovery/subfinder)(https://github.com/projectdiscovery/subfinder) |
| [httpx](https://github.com/projectdiscovery/httpx) | Fast HTTP probing / tech detection | 🟢 | [![last commit](https://img.shields.io/github/last-commit/projectdiscovery/httpx?style=flat-square&label=updated)](https://github.com/projectdiscovery/httpx)(https://github.com/projectdiscovery/httpx) |
| [dnsx](https://github.com/projectdiscovery/dnsx) | DNS toolkit for resolve and enumeration | 🟢 | [![last commit](https://img.shields.io/github/last-commit/projectdiscovery/dnsx?style=flat-square&label=updated)](https://github.com/projectdiscovery/dnsx)(https://github.com/projectdiscovery/dnsx) |
| [Chaos](https://github.com/projectdiscovery/chaos-client) | ProjectDiscovery DNS dataset client for passive recon | 🟢 | [![last commit](https://img.shields.io/github/last-commit/projectdiscovery/chaos-client?style=flat-square&label=updated)](https://github.com/projectdiscovery/chaos-client)(https://github.com/projectdiscovery/chaos-client) |
| [ffuf](https://github.com/ffuf/ffuf) | Fast web fuzzer (dirs, vhosts, params) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/ffuf/ffuf?style=flat-square&label=updated)](https://github.com/ffuf/ffuf)(https://github.com/ffuf/ffuf) |
| [gobuster](https://github.com/OJ/gobuster) | Directory, DNS, and vhost brute-forcing | 🟢 | [![last commit](https://img.shields.io/github/last-commit/OJ/gobuster?style=flat-square&label=updated)](https://github.com/OJ/gobuster)(https://github.com/OJ/gobuster) |
| [feroxbuster](https://github.com/epi052/feroxbuster) | Fast, recursive content discovery written in Rust | 🟢 | [![last commit](https://img.shields.io/github/last-commit/epi052/feroxbuster?style=flat-square&label=updated)](https://github.com/epi052/feroxbuster)(https://github.com/epi052/feroxbuster) |
| [Arjun](https://github.com/s0md3v/Arjun) | HTTP parameter discovery suite | 🟢 | [![last commit](https://img.shields.io/github/last-commit/s0md3v/Arjun?style=flat-square&label=updated)](https://github.com/s0md3v/Arjun)(https://github.com/s0md3v/Arjun) |
| [knock](https://github.com/guelfoweb/knock) | Subdomain enumeration via wordlist + DNS | 🟢 | [![last commit](https://img.shields.io/github/last-commit/guelfoweb/knock?style=flat-square&label=updated)](https://github.com/guelfoweb/knock)(https://github.com/guelfoweb/knock) |
| [subDomainsBrute](https://github.com/lijiejie/subDomainsBrute) | Multi-threaded subdomain brute-force | 🟢 | [![last commit](https://img.shields.io/github/last-commit/lijiejie/subDomainsBrute?style=flat-square&label=updated)](https://github.com/lijiejie/subDomainsBrute)(https://github.com/lijiejie/subDomainsBrute) |
| [SubDomain3](https://github.com/yanxiu0614/subdomain3) | High-speed subdomain scanner | 🟢 | [![last commit](https://img.shields.io/github/last-commit/yanxiu0614/subdomain3?style=flat-square&label=updated)](https://github.com/yanxiu0614/subdomain3)(https://github.com/yanxiu0614/subdomain3) |
| [domained](https://github.com/TypeError/domained) | Wrapper around multiple subdomain tools | 🟢 | [![last commit](https://img.shields.io/github/last-commit/TypeError/domained?style=flat-square&label=updated)](https://github.com/TypeError/domained)(https://github.com/TypeError/domained) |
| [katana](https://github.com/projectdiscovery/katana) | Next-gen crawling / spidering | 🟢 | [![last commit](https://img.shields.io/github/last-commit/projectdiscovery/katana?style=flat-square&label=updated)](https://github.com/projectdiscovery/katana)(https://github.com/projectdiscovery/katana) |
| [gau](https://github.com/lc/gau) | Fetch known URLs from public sources | 🟢 | [![last commit](https://img.shields.io/github/last-commit/lc/gau?style=flat-square&label=updated)](https://github.com/lc/gau)(https://github.com/lc/gau) |
| [waybackurls](https://github.com/tomnomnom/waybackurls) | Fetch URLs from the Wayback Machine for a domain | 🟢 | [![last commit](https://img.shields.io/github/last-commit/tomnomnom/waybackurls?style=flat-square&label=updated)](https://github.com/tomnomnom/waybackurls)(https://github.com/tomnomnom/waybackurls) |
| [hakrawler](https://github.com/hakluke/hakrawler) | Simple, fast web crawler for gathering URLs / endpoints | 🟢 | [![last commit](https://img.shields.io/github/last-commit/hakluke/hakrawler?style=flat-square&label=updated)](https://github.com/hakluke/hakrawler)(https://github.com/hakluke/hakrawler) |

---

## 🏢 Active Directory & Internal

Identity attack-path mapping and Windows / AD assessment tooling.

| Tool | Description | License | Last update |
|---|---|---|---|
| [BloodHound](https://github.com/SpecterOps/BloodHound) | Graph analysis of AD / Entra ID attack paths | 🟡 | [![last commit](https://img.shields.io/github/last-commit/SpecterOps/BloodHound?style=flat-square&label=updated)](https://github.com/SpecterOps/BloodHound)(https://github.com/SpecterOps/BloodHound) |
| [SharpHound](https://github.com/SpecterOps/SharpHound) | BloodHound data collector for Active Directory | 🟢 | [![last commit](https://img.shields.io/github/last-commit/SpecterOps/SharpHound?style=flat-square&label=updated)](https://github.com/SpecterOps/SharpHound)(https://github.com/SpecterOps/SharpHound) |
| [Impacket](https://github.com/fortra/impacket) | Python collection of Windows network protocol tools | 🟢 | [![last commit](https://img.shields.io/github/last-commit/fortra/impacket?style=flat-square&label=updated)](https://github.com/fortra/impacket)(https://github.com/fortra/impacket) |
| [NetExec](https://github.com/Pennyw0rth/NetExec) | Network authentication / assessment (CrackMapExec successor) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/Pennyw0rth/NetExec?style=flat-square&label=updated)](https://github.com/Pennyw0rth/NetExec)(https://github.com/Pennyw0rth/NetExec) |
| [Responder](https://github.com/lgandx/Responder) | LLMNR / NBT-NS / mDNS poisoner for credential capture | 🟢 | [![last commit](https://img.shields.io/github/last-commit/lgandx/Responder?style=flat-square&label=updated)](https://github.com/lgandx/Responder)(https://github.com/lgandx/Responder) |
| [Certipy](https://github.com/ly4k/Certipy) | Active Directory Certificate Services enumeration & abuse | 🟢 | [![last commit](https://img.shields.io/github/last-commit/ly4k/Certipy?style=flat-square&label=updated)](https://github.com/ly4k/Certipy)(https://github.com/ly4k/Certipy) |
| [Rubeus](https://github.com/GhostPack/Rubeus) | Kerberos abuse toolkit for offensive AD ops | 🟢 | [![last commit](https://img.shields.io/github/last-commit/GhostPack/Rubeus?style=flat-square&label=updated)](https://github.com/GhostPack/Rubeus)(https://github.com/GhostPack/Rubeus) |
| [PowerView](https://github.com/PowerShellMafia/PowerSploit) | PowerShell AD situational awareness (PowerSploit) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/PowerShellMafia/PowerSploit?style=flat-square&label=updated)](https://github.com/PowerShellMafia/PowerSploit)(https://github.com/PowerShellMafia/PowerSploit) |

---

## 🔑 Password Cracking

| Tool | Description | License | Last update |
|---|---|---|---|
| [Hashcat](https://github.com/hashcat/hashcat) | Advanced GPU password recovery | 🟢 | [![last commit](https://img.shields.io/github/last-commit/hashcat/hashcat?style=flat-square&label=updated)](https://github.com/hashcat/hashcat)(https://github.com/hashcat/hashcat) |
| [John the Ripper](https://github.com/openwall/john) | Fast password cracker (CPU + many formats) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/openwall/john?style=flat-square&label=updated)](https://github.com/openwall/john)(https://github.com/openwall/john) |
| [Hydra](https://github.com/vanhauser-thc/thc-hydra) | Parallel online brute-force for network services | 🟢 | [![last commit](https://img.shields.io/github/last-commit/vanhauser-thc/thc-hydra?style=flat-square&label=updated)](https://github.com/vanhauser-thc/thc-hydra)(https://github.com/vanhauser-thc/thc-hydra) |
| [Medusa](https://github.com/jmk-foofus/medusa) | Speedy, parallel, modular login brute-forcer | 🟢 | [![last commit](https://img.shields.io/github/last-commit/jmk-foofus/medusa?style=flat-square&label=updated)](https://github.com/jmk-foofus/medusa)(https://github.com/jmk-foofus/medusa) |

---

## ☁️ Cloud & Container Security

CSPM, CNAPP-adjacent OSS, and Kubernetes hardening.

| Tool | Focus | Description | License | Last update |
|---|---|---|---|---|
| [Prowler](https://github.com/prowler-cloud/prowler) | CSPM | Multi-cloud security assessment (AWS, Azure, GCP, …) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/prowler-cloud/prowler?style=flat-square&label=updated)](https://github.com/prowler-cloud/prowler)(https://github.com/prowler-cloud/prowler) |
| [ScoutSuite](https://github.com/nccgroup/ScoutSuite) | CSPM | Multi-cloud security auditing tool | 🟢 | [![last commit](https://img.shields.io/github/last-commit/nccgroup/ScoutSuite?style=flat-square&label=updated)](https://github.com/nccgroup/ScoutSuite)(https://github.com/nccgroup/ScoutSuite) |
| [CloudMapper](https://github.com/duo-labs/cloudmapper) | AWS | Network visualization and inventory for AWS accounts | 🟢 | [![last commit](https://img.shields.io/github/last-commit/duo-labs/cloudmapper?style=flat-square&label=updated)](https://github.com/duo-labs/cloudmapper)(https://github.com/duo-labs/cloudmapper) |
| [kube-bench](https://github.com/aquasecurity/kube-bench) | Kubernetes | CIS Kubernetes Benchmark checks | 🟢 | [![last commit](https://img.shields.io/github/last-commit/aquasecurity/kube-bench?style=flat-square&label=updated)](https://github.com/aquasecurity/kube-bench)(https://github.com/aquasecurity/kube-bench) |
| [kube-hunter](https://github.com/aquasecurity/kube-hunter) | Kubernetes | Hunt for security weaknesses in K8s clusters | 🟢 | [![last commit](https://img.shields.io/github/last-commit/aquasecurity/kube-hunter?style=flat-square&label=updated)](https://github.com/aquasecurity/kube-hunter)(https://github.com/aquasecurity/kube-hunter) |
| [Falco](https://github.com/falcosecurity/falco) | Runtime | Cloud-native runtime security / threat detection | 🟢 | [![last commit](https://img.shields.io/github/last-commit/falcosecurity/falco?style=flat-square&label=updated)](https://github.com/falcosecurity/falco)(https://github.com/falcosecurity/falco) |
| [Trivy](https://github.com/aquasecurity/trivy) | Containers / IaC | Image, filesystem, and IaC vulnerability scanner | 🟢 | [![last commit](https://img.shields.io/github/last-commit/aquasecurity/trivy?style=flat-square&label=updated)](https://github.com/aquasecurity/trivy)(https://github.com/aquasecurity/trivy) |
| [Docker Bench](https://github.com/docker/docker-bench-security) | Containers | CIS Docker Benchmark script | 🟢 | [![last commit](https://img.shields.io/github/last-commit/docker/docker-bench-security?style=flat-square&label=updated)](https://github.com/docker/docker-bench-security)(https://github.com/docker/docker-bench-security) |
| [Orca Security](https://orca.security/) | CNAPP | Commercial agentless cloud security platform | 🔴 | — |
| [Wiz](https://www.wiz.io/) | CNAPP | Commercial cloud security platform | 🔴 | — |
| [Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud) | CNAPP | Commercial CNAPP by Palo Alto Networks | 🔴 | — |

---

## 📡 Network Analysis & IDS

| Tool | Description | License | Last update |
|---|---|---|---|
| [Wireshark](https://github.com/wireshark/wireshark) | Network protocol analyzer | 🟢 | [![last commit](https://img.shields.io/github/last-commit/wireshark/wireshark?style=flat-square&label=updated)](https://github.com/wireshark/wireshark)(https://github.com/wireshark/wireshark) |
| [tcpdump](https://github.com/the-tcpdump-group/tcpdump) | Classic command-line packet analyzer | 🟢 | [![last commit](https://img.shields.io/github/last-commit/the-tcpdump-group/tcpdump?style=flat-square&label=updated)](https://github.com/the-tcpdump-group/tcpdump)(https://github.com/the-tcpdump-group/tcpdump) |
| [Zeek](https://github.com/zeek/zeek) | Network security monitoring framework (formerly Bro) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/zeek/zeek?style=flat-square&label=updated)](https://github.com/zeek/zeek)(https://github.com/zeek/zeek) |
| [Suricata](https://github.com/OISF/suricata) | High-performance IDS / IPS / NSM engine | 🟢 | [![last commit](https://img.shields.io/github/last-commit/OISF/suricata?style=flat-square&label=updated)](https://github.com/OISF/suricata)(https://github.com/OISF/suricata) |
| [Snort](https://github.com/snort3/snort3) | Network intrusion detection and prevention | 🟢 | [![last commit](https://img.shields.io/github/last-commit/snort3/snort3?style=flat-square&label=updated)](https://github.com/snort3/snort3)(https://github.com/snort3/snort3) |
| [Wazuh](https://github.com/wazuh/wazuh) | Open-source XDR / SIEM platform | 🟢 | [![last commit](https://img.shields.io/github/last-commit/wazuh/wazuh?style=flat-square&label=updated)](https://github.com/wazuh/wazuh)(https://github.com/wazuh/wazuh) |
| [OSSEC](https://github.com/ossec/ossec-hids) | Host-based intrusion detection system | 🟢 | [![last commit](https://img.shields.io/github/last-commit/ossec/ossec-hids?style=flat-square&label=updated)](https://github.com/ossec/ossec-hids)(https://github.com/ossec/ossec-hids) |
| [ModSecurity](https://github.com/owasp-modsecurity/ModSecurity) | Open-source web application firewall engine | 🟢 | [![last commit](https://img.shields.io/github/last-commit/owasp-modsecurity/ModSecurity?style=flat-square&label=updated)](https://github.com/owasp-modsecurity/ModSecurity)(https://github.com/owasp-modsecurity/ModSecurity) |

---

## 🔬 Forensics & Incident Response

| Tool | Description | License | Last update |
|---|---|---|---|
| [Volatility 3](https://github.com/volatilityfoundation/volatility3) | Advanced memory forensics framework | 🟢 | [![last commit](https://img.shields.io/github/last-commit/volatilityfoundation/volatility3?style=flat-square&label=updated)](https://github.com/volatilityfoundation/volatility3)(https://github.com/volatilityfoundation/volatility3) |
| [Velociraptor](https://github.com/Velocidex/velociraptor) | Endpoint visibility and digital forensics / IR | 🟢 | [![last commit](https://img.shields.io/github/last-commit/Velocidex/velociraptor?style=flat-square&label=updated)](https://github.com/Velocidex/velociraptor)(https://github.com/Velocidex/velociraptor) |
| [Autopsy](https://github.com/sleuthkit/autopsy) | Digital forensics platform (GUI on The Sleuth Kit) | 🟢 | [![last commit](https://img.shields.io/github/last-commit/sleuthkit/autopsy?style=flat-square&label=updated)](https://github.com/sleuthkit/autopsy)(https://github.com/sleuthkit/autopsy) |
| [The Sleuth Kit](https://github.com/sleuthkit/sleuthkit) | Library and tools for disk image forensics | 🟢 | [![last commit](https://img.shields.io/github/last-commit/sleuthkit/sleuthkit?style=flat-square&label=updated)](https://github.com/sleuthkit/sleuthkit)(https://github.com/sleuthkit/sleuthkit) |
| [Plaso](https://github.com/log2timeline/plaso) | Super timeline engine for digital forensics | 🟢 | [![last commit](https://img.shields.io/github/last-commit/log2timeline/plaso?style=flat-square&label=updated)](https://github.com/log2timeline/plaso)(https://github.com/log2timeline/plaso) |
| [osquery](https://github.com/osquery/osquery) | SQL-powered operating system instrumentation | 🟢 | [![last commit](https://img.shields.io/github/last-commit/osquery/osquery?style=flat-square&label=updated)](https://github.com/osquery/osquery)(https://github.com/osquery/osquery) |
| [TheHive](https://github.com/TheHive-Project/TheHive) | Scalable Security Incident Response Platform | 🟢 | [![last commit](https://img.shields.io/github/last-commit/TheHive-Project/TheHive?style=flat-square&label=updated)](https://github.com/TheHive-Project/TheHive)(https://github.com/TheHive-Project/TheHive) |
| [Cortex](https://github.com/TheHive-Project/Cortex) | Observable analysis & active response engine | 🟢 | [![last commit](https://img.shields.io/github/last-commit/TheHive-Project/Cortex?style=flat-square&label=updated)](https://github.com/TheHive-Project/Cortex)(https://github.com/TheHive-Project/Cortex) |

---

## 🧠 Threat Intelligence

| Tool | Description | License | Last update |
|---|---|---|---|
| [MISP](https://github.com/MISP/MISP) | Open-source threat intelligence sharing platform | 🟢 | [![last commit](https://img.shields.io/github/last-commit/MISP/MISP?style=flat-square&label=updated)](https://github.com/MISP/MISP)(https://github.com/MISP/MISP) |
| [OpenCTI](https://github.com/OpenCTI-Platform/opencti) | Open Cyber Threat Intelligence platform | 🟢 | [![last commit](https://img.shields.io/github/last-commit/OpenCTI-Platform/opencti?style=flat-square&label=updated)](https://github.com/OpenCTI-Platform/opencti)(https://github.com/OpenCTI-Platform/opencti) |
| [OpenTAXII](https://github.com/eclecticiq/OpenTAXII) | TAXII server implementation for CTI exchange | 🟢 | [![last commit](https://img.shields.io/github/last-commit/eclecticiq/OpenTAXII?style=flat-square&label=updated)](https://github.com/eclecticiq/OpenTAXII)(https://github.com/eclecticiq/OpenTAXII) |
| [YARA](https://github.com/VirusTotal/yara) | Pattern-matching for malware researchers | 🟢 | [![last commit](https://img.shields.io/github/last-commit/VirusTotal/yara?style=flat-square&label=updated)](https://github.com/VirusTotal/yara)(https://github.com/VirusTotal/yara) |
| [Sigma](https://github.com/SigmaHQ/sigma) | Generic signature format for SIEM systems | 🟢 | [![last commit](https://img.shields.io/github/last-commit/SigmaHQ/sigma?style=flat-square&label=updated)](https://github.com/SigmaHQ/sigma)(https://github.com/SigmaHQ/sigma) |
| [AbuseIPDB](https://www.abuseipdb.com/) | IP abuse reporting and reputation database | ☁️ | — |
| [VirusTotal](https://www.virustotal.com/) | Multi-engine file / URL malware analysis | ☁️ | — |
| [AlienVault OTX](https://otx.alienvault.com/) | Open Threat Exchange community intel | ☁️ | — |
| [Hudson Rock](https://www.hudsonrock.com/) | Infostealer / cybercrime intelligence | ☁️ | — |

---

## 🕳️ Breach & Leak Lookup

Credential and leak monitoring / digital risk protection lookups.

| Tool | Description | License | Last update |
|---|---|---|---|
| [Have I Been Pwned](https://haveibeenpwned.com/) | Check if emails / passwords appear in known breaches | ☁️ | — |
| [DeHashed](https://dehashed.com/) | Breach data search for credentials, WHOIS, and monitoring | ☁️ | — |
| [Intelligence X](https://intelx.io/) | Search leaked and historical data | ☁️ | — |
| [LeakIX](https://leakix.net/) | Search engine for publicly exposed services and leaks | ☁️ | — |
| [Hudson Rock](https://cavalier.hudsonrock.com/) | Free / paid infostealer compromise checks | ☁️ | — |

---

## 🧬 Binary Analysis & Reverse Engineering

| Tool | Description | License | Last update |
|---|---|---|---|
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | NSA open-source software reverse engineering suite | 🟢 | [![last commit](https://img.shields.io/github/last-commit/NationalSecurityAgency/ghidra?style=flat-square&label=updated)](https://github.com/NationalSecurityAgency/ghidra)(https://github.com/NationalSecurityAgency/ghidra) |
| [radare2](https://github.com/radareorg/radare2) | UNIX-like reverse engineering framework | 🟢 | [![last commit](https://img.shields.io/github/last-commit/radareorg/radare2?style=flat-square&label=updated)](https://github.com/radareorg/radare2)(https://github.com/radareorg/radare2) |
| [Cutter](https://github.com/rizinorg/cutter) | Free GUI for Rizin / reverse engineering | 🟢 | [![last commit](https://img.shields.io/github/last-commit/rizinorg/cutter?style=flat-square&label=updated)](https://github.com/rizinorg/cutter)(https://github.com/rizinorg/cutter) |
| [Binary Ninja](https://binary.ninja/) | Commercial reverse engineering platform | 🔴 | — |
| [IDA](https://hex-rays.com/ida-pro/) | Commercial industry-standard disassembler / debugger | 🔴 | — |
| [Binwalk](https://github.com/ReFirmLabs/binwalk) | Firmware analysis and extraction tool | 🟢 | [![last commit](https://img.shields.io/github/last-commit/ReFirmLabs/binwalk?style=flat-square&label=updated)](https://github.com/ReFirmLabs/binwalk)(https://github.com/ReFirmLabs/binwalk) |
| [PE-bear](https://github.com/hasherezade/pe-bear) | PE file reversing toolkit | 🟢 | [![last commit](https://img.shields.io/github/last-commit/hasherezade/pe-bear?style=flat-square&label=updated)](https://github.com/hasherezade/pe-bear)(https://github.com/hasherezade/pe-bear) |
| [Detect It Easy](https://github.com/horsicq/Detect-It-Easy) | Packer / compiler / crypto detection for binaries | 🟢 | [![last commit](https://img.shields.io/github/last-commit/horsicq/Detect-It-Easy?style=flat-square&label=updated)](https://github.com/horsicq/Detect-It-Easy)(https://github.com/horsicq/Detect-It-Easy) |

---

## 📚 Wordlists & Payloads

| Tool | Description | License | Last update |
|---|---|---|---|
| [SecLists](https://github.com/danielmiessler/SecLists) | Collection of security wordlists and payloads | 🟢 | [![last commit](https://img.shields.io/github/last-commit/danielmiessler/SecLists?style=flat-square&label=updated)](https://github.com/danielmiessler/SecLists)(https://github.com/danielmiessler/SecLists) |
| [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | Useful payloads and bypasses for Web AppSec | 🟢 | [![last commit](https://img.shields.io/github/last-commit/swisskyrepo/PayloadsAllTheThings?style=flat-square&label=updated)](https://github.com/swisskyrepo/PayloadsAllTheThings)(https://github.com/swisskyrepo/PayloadsAllTheThings) |
| [FuzzDB](https://github.com/fuzzdb-project/fuzzdb) | Attack patterns, discovery dictionaries, and injectables | 🟢 | [![last commit](https://img.shields.io/github/last-commit/fuzzdb-project/fuzzdb?style=flat-square&label=updated)](https://github.com/fuzzdb-project/fuzzdb)(https://github.com/fuzzdb-project/fuzzdb) |
| [Assetnote Wordlists](https://wordlists.assetnote.io/) | High-quality discovery wordlists | 🌐 | — |

---

## 📚 Vulnerability Databases

| Source | Description | License |
|---|---|---|
| [CVE](https://www.cve.org/) | Common catalog of public vulnerability identifiers | 🌐 |
| [NVD (NIST)](https://nvd.nist.gov/) | U.S. SCAP / CVE repository with CVSS, CPE, and references | 🌐 |
| [Exploit-DB](https://www.exploit-db.com/) | Archive of exploits, shellcode, and advisories | 🌐 |
| [0day.today](http://0day.today/) | Exploit and 0day database for researchers | ☁️ |
| [VulDB](https://vuldb.com/) | Documented vulnerabilities and exploits | ☁️ |
| [Snyk Vuln DB](https://security.snyk.io/) | OSS vulnerability DB with remediation guidance | ☁️ |
| [OSV](https://osv.dev/) | Distributed open-source vulnerability database | 🌐 |
| [GitHub Advisory](https://github.com/advisories) | Security advisories for package ecosystems | 🌐 |
| [FSTEC BDU](https://bdu.fstec.ru/) | Russian threat / vulnerability data bank | 🌐 |

---

## 🔗 External directories

Broader catalogs for discovering additional commercial and free products:

| Directory | Focus | License |
|---|---|---|
| [OWASP](https://owasp.org/) | Projects, cheat sheets, and Top 10 lists | 🌐 |
| [awesome-security](https://github.com/sbilly/awesome-security) | Curated awesome-list of security resources | 🟢 |

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
