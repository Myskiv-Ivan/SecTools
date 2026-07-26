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

**Activity badges** (prefer release signal over raw commits — Dependabot/CI noise):

| Badge | Meaning |
|---|---|
| `release` | Date of the latest **GitHub Release** |
| `tag` | Latest git **tag** (no GitHub Release published) |
| `commit` | Latest git **commit** (fallback; may include bots) |
| `—` | No public GitHub repo |


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
| **Sherlock**<br>[GitHub](https://github.com/sherlock-project/sherlock) | Hunt usernames across hundreds of social networks | 🟢 | [![release](https://img.shields.io/github/release-date/sherlock-project/sherlock?style=flat-square&label=release)](https://github.com/sherlock-project/sherlock/releases) |
| **theHarvester**<br>[GitHub](https://github.com/laramies/theHarvester) | Gather emails, subdomains, hosts, and people from public sources | 🟢 | [![release](https://img.shields.io/github/release-date/laramies/theHarvester?style=flat-square&label=release)](https://github.com/laramies/theHarvester/releases) |
| **SpiderFoot**<br>[GitHub](https://github.com/smicallef/spiderfoot) | Automated OSINT with hundreds of modules and a web UI | 🟢 | [![release](https://img.shields.io/github/release-date/smicallef/spiderfoot?style=flat-square&label=release)](https://github.com/smicallef/spiderfoot/releases) |
| **Recon-ng**<br>[GitHub](https://github.com/lanmaster53/recon-ng) | Modular reconnaissance framework (Metasploit-style) | 🟢 | [![tag](https://img.shields.io/github/v/tag/lanmaster53/recon-ng?style=flat-square&label=tag)](https://github.com/lanmaster53/recon-ng/tags) |
| **Photon**<br>[GitHub](https://github.com/s0md3v/Photon) | Fast crawler for OSINT data extraction from websites | 🟢 | [![release](https://img.shields.io/github/release-date/s0md3v/Photon?style=flat-square&label=release)](https://github.com/s0md3v/Photon/releases) |
| **Maltego**<br>[maltego.com](https://www.maltego.com/) | Graph visualization of people, domains, and infrastructure | 🟡 | — |
| **R3CON1Z3R**<br>[GitHub](https://github.com/abdulgaphy/r3con1z3r) | Lightweight OSINT script for target footprinting | 🟢 | [![commit](https://img.shields.io/github/last-commit/abdulgaphy/r3con1z3r?style=flat-square&label=commit)](https://github.com/abdulgaphy/r3con1z3r/commits) |
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
| **DefectDojo**<br>[GitHub](https://github.com/DefectDojo/django-DefectDojo) | DevSecOps platform: report import, triage, metrics, SLA | 🟢 | [![release](https://img.shields.io/github/release-date/DefectDojo/django-DefectDojo?style=flat-square&label=release)](https://github.com/DefectDojo/django-DefectDojo/releases) |
| **Faraday**<br>[GitHub](https://github.com/infobyte/faraday) | Collaborative pentest IDE / vulnerability management | 🟢 | [![release](https://img.shields.io/github/release-date/infobyte/faraday?style=flat-square&label=release)](https://github.com/infobyte/faraday/releases) |
| **ArcherySec**<br>[GitHub](https://github.com/archerysec/archerysec) | Vulnerability assessment & management with scanner integrations | 🟢 | [![release](https://img.shields.io/github/release-date/archerysec/archerysec?style=flat-square&label=release)](https://github.com/archerysec/archerysec/releases) |
| **reNgine**<br>[GitHub](https://github.com/yogeshojha/rengine) | Automated recon + vulnerability management with web UI | 🟢 | [![release](https://img.shields.io/github/release-date/yogeshojha/rengine?style=flat-square&label=release)](https://github.com/yogeshojha/rengine/releases) |
| **Vuls**<br>[GitHub](https://github.com/future-architect/vuls) | Agentless vulnerability scanner for Linux / FreeBSD | 🟢 | [![release](https://img.shields.io/github/release-date/future-architect/vuls?style=flat-square&label=release)](https://github.com/future-architect/vuls/releases) |
| **OWASP Threat Dragon**<br>[GitHub](https://github.com/OWASP/threat-dragon) | Threat modeling tool for STRIDE-style diagrams | 🟢 | [![release](https://img.shields.io/github/release-date/OWASP/threat-dragon?style=flat-square&label=release)](https://github.com/OWASP/threat-dragon/releases) |

---

## ⚒️ Analysis & Exploit Frameworks

| Tool | Category | Description | License | Activity |
|---|---|---|---|---|
| **Metasploit**<br>[GitHub](https://github.com/rapid7/metasploit-framework) | Exploit Framework | Classic exploit, payload, and post-exploitation framework | 🟡 | [![tag](https://img.shields.io/github/v/tag/rapid7/metasploit-framework?style=flat-square&label=tag)](https://github.com/rapid7/metasploit-framework/tags) |
| **RouterSploit**<br>[GitHub](https://github.com/threat9/routersploit) | Exploit Framework | Exploits and checks for embedded / network devices | 🟢 | [![release](https://img.shields.io/github/release-date/threat9/routersploit?style=flat-square&label=release)](https://github.com/threat9/routersploit/releases) |
| **BeEF**<br>[GitHub](https://github.com/beefproject/beef) | Exploit Framework | Browser Exploitation Framework | 🟢 | [![release](https://img.shields.io/github/release-date/beefproject/beef?style=flat-square&label=release)](https://github.com/beefproject/beef/releases) |
| **Sliver**<br>[GitHub](https://github.com/BishopFox/sliver) | C2 | Open-source adversary emulation / C2 framework | 🟢 | [![release](https://img.shields.io/github/release-date/BishopFox/sliver?style=flat-square&label=release)](https://github.com/BishopFox/sliver/releases) |
| **Havoc**<br>[GitHub](https://github.com/HavocFramework/Havoc) | C2 | Modern post-exploitation command and control | 🟢 | [![commit](https://img.shields.io/github/last-commit/HavocFramework/Havoc?style=flat-square&label=commit)](https://github.com/HavocFramework/Havoc/commits) |
| **MobSF**<br>[GitHub](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | Mobile | Static and dynamic analysis for Android / iOS | 🟢 | [![release](https://img.shields.io/github/release-date/MobSF/Mobile-Security-Framework-MobSF?style=flat-square&label=release)](https://github.com/MobSF/Mobile-Security-Framework-MobSF/releases) |
| **Frida**<br>[GitHub](https://github.com/frida/frida) | Dynamic Instrumentation | Dynamic instrumentation toolkit for apps | 🟢 | [![release](https://img.shields.io/github/release-date/frida/frida?style=flat-square&label=release)](https://github.com/frida/frida/releases) |
| **Objection**<br>[GitHub](https://github.com/sensepost/objection) | Mobile | Runtime mobile exploration powered by Frida | 🟢 | [![release](https://img.shields.io/github/release-date/sensepost/objection?style=flat-square&label=release)](https://github.com/sensepost/objection/releases) |
| **RedTeam C# Scripts**<br>[GitHub](https://github.com/Mr-Un1k0d3r/RedTeamCSharpScripts) | Red Team | Collection of C# scripts for red team operations | 🟢 | [![commit](https://img.shields.io/github/last-commit/Mr-Un1k0d3r/RedTeamCSharpScripts?style=flat-square&label=commit)](https://github.com/Mr-Un1k0d3r/RedTeamCSharpScripts/commits) |
| **Atomic Red Team**<br>[GitHub](https://github.com/redcanaryco/atomic-red-team) | Adversary Emulation | Small, focused tests mapped to ATT&CK techniques | 🟢 | [![commit](https://img.shields.io/github/last-commit/redcanaryco/atomic-red-team?style=flat-square&label=commit)](https://github.com/redcanaryco/atomic-red-team/commits) |
| **CALDERA**<br>[GitHub](https://github.com/mitre/caldera) | Adversary Emulation | Automated adversary emulation platform by MITRE | 🟢 | [![release](https://img.shields.io/github/release-date/mitre/caldera?style=flat-square&label=release)](https://github.com/mitre/caldera/releases) |

---

## 🧰 Web Proxies & Manual Testing

Intercept, replay, and mutate HTTP(S) traffic during web assessments.

| Tool | Description | License | Activity |
|---|---|---|---|
| **Burp Suite**<br>[portswigger.net](https://portswigger.net/burp) | Industry-standard web security testing platform (Community / Pro) | 🟡 | — |
| **Caido**<br>[caido.io](https://caido.io/) | Modern lightweight web proxy for bug bounty and pentest | 🟡 | [![release](https://img.shields.io/github/release-date/caido/caido?style=flat-square&label=release)](https://github.com/caido/caido/releases) |
| **mitmproxy**<br>[GitHub](https://github.com/mitmproxy/mitmproxy) | Interactive TLS-capable intercepting HTTP proxy (CLI + web) | 🟢 | [![release](https://img.shields.io/github/release-date/mitmproxy/mitmproxy?style=flat-square&label=release)](https://github.com/mitmproxy/mitmproxy/releases) |
| **OWASP ZAP**<br>[GitHub](https://github.com/zaproxy/zaproxy) | Free proxy + automated scanner | 🟢 | [![release](https://img.shields.io/github/release-date/zaproxy/zaproxy?style=flat-square&label=release)](https://github.com/zaproxy/zaproxy/releases) |
| **WATOBO**<br>[GitHub](https://github.com/siberas/watobo) | Intercepting proxy + scanner for pentests | 🟢 | [![release](https://img.shields.io/github/release-date/siberas/watobo?style=flat-square&label=release)](https://github.com/siberas/watobo/releases) |

---

## 🔎 SAST — Static Analysis

Find vulnerabilities in source code without running the application.

| Tool | Languages / scope | Description | License | Activity |
|---|---|---|---|---|
| **Semgrep**<br>[GitHub](https://github.com/semgrep/semgrep) | 30+ languages | Fast pattern-based SAST with YAML rules; CI-friendly | 🟡 | [![release](https://img.shields.io/github/release-date/semgrep/semgrep?style=flat-square&label=release)](https://github.com/semgrep/semgrep/releases) |
| **CodeQL**<br>[codeql.github.com](https://codeql.github.com/) | Multilang | Semantic code analysis from GitHub (query-as-code) | 🟡 | — |
| **Bearer**<br>[GitHub](https://github.com/Bearer/bearer) | JS/TS, Ruby, PHP, Java, Go, Python | SAST focused on data flows and privacy | 🟢 | [![release](https://img.shields.io/github/release-date/Bearer/bearer?style=flat-square&label=release)](https://github.com/Bearer/bearer/releases) |
| **Bandit**<br>[GitHub](https://github.com/PyCQA/bandit) | Python | Common security issues in Python | 🟢 | [![release](https://img.shields.io/github/release-date/PyCQA/bandit?style=flat-square&label=release)](https://github.com/PyCQA/bandit/releases) |
| **Brakeman**<br>[GitHub](https://github.com/presidentbeef/brakeman) | Ruby on Rails | Rails-focused static security scanner | 🟢 | [![release](https://img.shields.io/github/release-date/presidentbeef/brakeman?style=flat-square&label=release)](https://github.com/presidentbeef/brakeman/releases) |
| **Find Security Bugs**<br>[GitHub](https://github.com/find-sec-bugs/find-sec-bugs) | Java, Android, Scala, Kotlin, Groovy | SpotBugs plugin for web / Android security | 🟢 | [![release](https://img.shields.io/github/release-date/find-sec-bugs/find-sec-bugs?style=flat-square&label=release)](https://github.com/find-sec-bugs/find-sec-bugs/releases) |
| **SpotBugs**<br>[GitHub](https://github.com/spotbugs/spotbugs) | Java | Static analysis of Java bytecode | 🟢 | [![release](https://img.shields.io/github/release-date/spotbugs/spotbugs?style=flat-square&label=release)](https://github.com/spotbugs/spotbugs/releases) |
| **PMD**<br>[GitHub](https://github.com/pmd/pmd) | Multilang | Static analysis for quality and security rules | 🟢 | [![release](https://img.shields.io/github/release-date/pmd/pmd?style=flat-square&label=release)](https://github.com/pmd/pmd/releases) |
| **Security Code Scan**<br>[GitHub](https://github.com/security-code-scan/security-code-scan) | C#, VB.NET | Roslyn analyzer for .NET vulnerabilities | 🟢 | [![release](https://img.shields.io/github/release-date/security-code-scan/security-code-scan?style=flat-square&label=release)](https://github.com/security-code-scan/security-code-scan/releases) |
| **Infer#**<br>[GitHub](https://github.com/microsoft/infersharp) | C# | Interprocedural .NET analysis based on Facebook Infer | 🟢 | [![release](https://img.shields.io/github/release-date/microsoft/infersharp?style=flat-square&label=release)](https://github.com/microsoft/infersharp/releases) |
| **Insider**<br>[GitHub](https://github.com/insidersec/insider) | Java, Kotlin, Swift, .NET, JS | CLI SAST for multiple stacks | 🟢 | [![release](https://img.shields.io/github/release-date/insidersec/insider?style=flat-square&label=release)](https://github.com/insidersec/insider/releases) |
| **Codechecker**<br>[GitHub](https://github.com/Ericsson/codechecker) | C/C++ | Wrapper around Clang Static Analyzer / Clang-Tidy | 🟢 | [![release](https://img.shields.io/github/release-date/Ericsson/codechecker?style=flat-square&label=release)](https://github.com/Ericsson/codechecker/releases) |
| **Cppcheck**<br>[GitHub](https://github.com/danmar/cppcheck) | C/C++ | Static analysis focused on undefined behavior | 🟢 | [![release](https://img.shields.io/github/release-date/danmar/cppcheck?style=flat-square&label=release)](https://github.com/danmar/cppcheck/releases) |
| **LLVM Clang SA**<br>[GitHub](https://github.com/llvm/llvm-project) | C, C++, Obj-C | Clang Static Analyzer | 🟢 | [![release](https://img.shields.io/github/release-date/llvm/llvm-project?style=flat-square&label=release)](https://github.com/llvm/llvm-project/releases) |
| **PVS-Studio**<br>[pvs-studio.com](https://pvs-studio.com/) | Multilang | Commercial static analyzer (trial available) | 🔴 | — |
| **Codemodder**<br>[GitHub](https://github.com/pixee/codemodder-python) | Java, Python | Auto-fix for security and quality issues | 🟢 | [![release](https://img.shields.io/github/release-date/pixee/codemodder-python?style=flat-square&label=release)](https://github.com/pixee/codemodder-python/releases) |
| **gosec**<br>[GitHub](https://github.com/securego/gosec) | Go | Inspector for security problems in Go code | 🟢 | [![release](https://img.shields.io/github/release-date/securego/gosec?style=flat-square&label=release)](https://github.com/securego/gosec/releases) |
| **PHP Vulnerability Hunter**<br>[GitHub](https://github.com/OneSourceCat/phpvulhunter) | PHP | PHP vulnerability finder (legacy) | 🟢 | [![commit](https://img.shields.io/github/last-commit/OneSourceCat/phpvulhunter?style=flat-square&label=commit)](https://github.com/OneSourceCat/phpvulhunter/commits) |
| **Cobra**<br>[GitHub](https://github.com/wufeifei/cobra) | PHP, Java | Source code security audit (legacy) | 🟢 | [![release](https://img.shields.io/github/release-date/wufeifei/cobra?style=flat-square&label=release)](https://github.com/wufeifei/cobra/releases) |

---

## 🎯 DAST / IAST

Dynamic and interactive analysis of running applications.

| Tool | Type | Description | License | Activity |
|---|---|---|---|---|
| **OWASP ZAP**<br>[GitHub](https://github.com/zaproxy/zaproxy) | DAST | Free web proxy and automated scanner from OWASP | 🟢 | [![release](https://img.shields.io/github/release-date/zaproxy/zaproxy?style=flat-square&label=release)](https://github.com/zaproxy/zaproxy/releases) |
| **Nuclei**<br>[GitHub](https://github.com/projectdiscovery/nuclei) | DAST | Fast YAML-template scanner for CVE / misconfig (HTTP, DNS, TCP…) | 🟢 | [![release](https://img.shields.io/github/release-date/projectdiscovery/nuclei?style=flat-square&label=release)](https://github.com/projectdiscovery/nuclei/releases) |
| **Nikto**<br>[GitHub](https://github.com/sullo/nikto) | DAST | Classic web scanner for dangerous files and misconfigurations | 🟢 | [![release](https://img.shields.io/github/release-date/sullo/nikto?style=flat-square&label=release)](https://github.com/sullo/nikto/releases) |
| **Wapiti**<br>[GitHub](https://github.com/wapiti-scanner/wapiti) | DAST | Black-box web scanner (XSS, SQLi, and more) | 🟢 | [![release](https://img.shields.io/github/release-date/wapiti-scanner/wapiti?style=flat-square&label=release)](https://github.com/wapiti-scanner/wapiti/releases) |
| **w3af**<br>[GitHub](https://github.com/andresriancho/w3af) | DAST | Web Application Attack and Audit Framework | 🟢 | [![release](https://img.shields.io/github/release-date/andresriancho/w3af?style=flat-square&label=release)](https://github.com/andresriancho/w3af/releases) |
| **Dalfox**<br>[GitHub](https://github.com/hahwul/dalfox) | XSS | Parameter analysis and XSS scanning / exploitation helper | 🟢 | [![release](https://img.shields.io/github/release-date/hahwul/dalfox?style=flat-square&label=release)](https://github.com/hahwul/dalfox/releases) |
| **Commix**<br>[GitHub](https://github.com/commixproject/commix) | Command Injection | Automated OS command injection detection and exploitation | 🟢 | [![release](https://img.shields.io/github/release-date/commixproject/commix?style=flat-square&label=release)](https://github.com/commixproject/commix/releases) |
| **jwt_tool**<br>[GitHub](https://github.com/ticarpi/jwt_tool) | API / Auth | Toolkit for testing, forging, and attacking JWTs | 🟢 | [![release](https://img.shields.io/github/release-date/ticarpi/jwt_tool?style=flat-square&label=release)](https://github.com/ticarpi/jwt_tool/releases) |
| **Snyk**<br>[GitHub](https://github.com/snyk/cli) | DAST / SCA | Scan code, dependencies, containers, and IaC | 🟡 | [![release](https://img.shields.io/github/release-date/snyk/cli?style=flat-square&label=release)](https://github.com/snyk/cli/releases) |
| **SonarQube**<br>[GitHub](https://github.com/SonarSource/sonarqube) | SAST / Quality | Code quality + security hotspots | 🟡 | [![release](https://img.shields.io/github/release-date/SonarSource/sonarqube?style=flat-square&label=release)](https://github.com/SonarSource/sonarqube/releases) |
| **Contrast Security**<br>[contrastsecurity.com](https://www.contrastsecurity.com/) | IAST | Agent-based interactive analysis at runtime | 🔴 | — |
| **PT Application Inspector**<br>[ptsecurity.com](https://www.ptsecurity.com/ww-en/products/ai/) | SAST/DAST | Commercial application analyzer (Positive Technologies) | 🔴 | — |
| **CloudSploit**<br>[GitHub](https://github.com/aquasecurity/cloudsploit) | Cloud | Misconfiguration checks for AWS / Azure / GCP / Oracle | 🟢 | [![release](https://img.shields.io/github/release-date/aquasecurity/cloudsploit?style=flat-square&label=release)](https://github.com/aquasecurity/cloudsploit/releases) |
| **Mend (WhiteSource)**<br>[mend.io](https://www.mend.io/) | SCA / AppSec | Commercial open-source risk platform | 🔴 | — |

---

## 📦 SCA / IaC

Dependency and infrastructure-as-code analysis.

| Tool | Focus | Description | License | Activity |
|---|---|---|---|---|
| **Trivy**<br>[GitHub](https://github.com/aquasecurity/trivy) | SCA + IaC + Containers | All-in-one: deps, images, IaC, secrets | 🟢 | [![release](https://img.shields.io/github/release-date/aquasecurity/trivy?style=flat-square&label=release)](https://github.com/aquasecurity/trivy/releases) |
| **Grype**<br>[GitHub](https://github.com/anchore/grype) | SCA / Containers | Vulnerability scanner for images and filesystems | 🟢 | [![release](https://img.shields.io/github/release-date/anchore/grype?style=flat-square&label=release)](https://github.com/anchore/grype/releases) |
| **OSV-Scanner**<br>[GitHub](https://github.com/google/osv-scanner) | SCA | Scanner powered by [OSV.dev](https://osv.dev) (Google) | 🟢 | [![release](https://img.shields.io/github/release-date/google/osv-scanner?style=flat-square&label=release)](https://github.com/google/osv-scanner/releases) |
| **Dependency-Track**<br>[GitHub](https://github.com/DependencyTrack/dependency-track) | SCA Platform | Continuous analysis platform for SBOM / dependencies | 🟢 | [![release](https://img.shields.io/github/release-date/DependencyTrack/dependency-track?style=flat-square&label=release)](https://github.com/DependencyTrack/dependency-track/releases) |
| **OWASP Dependency-Check**<br>[GitHub](https://github.com/jeremylong/DependencyCheck) | SCA | Match dependencies against known CVE | 🟢 | [![release](https://img.shields.io/github/release-date/jeremylong/DependencyCheck?style=flat-square&label=release)](https://github.com/jeremylong/DependencyCheck/releases) |
| **Checkov**<br>[GitHub](https://github.com/bridgecrewio/checkov) | IaC | Policy-as-code for Terraform, K8s, CloudFormation, Docker | 🟢 | [![release](https://img.shields.io/github/release-date/bridgecrewio/checkov?style=flat-square&label=release)](https://github.com/bridgecrewio/checkov/releases) |
| **KICS**<br>[GitHub](https://github.com/Checkmarx/kics) | IaC | Keeping Infrastructure as Code Secure — multi-IaC scanner | 🟢 | [![release](https://img.shields.io/github/release-date/Checkmarx/kics?style=flat-square&label=release)](https://github.com/Checkmarx/kics/releases) |
| **tfsec**<br>[GitHub](https://github.com/aquasecurity/tfsec) | IaC | Terraform security scanner (Trivy lineage) | 🟢 | [![release](https://img.shields.io/github/release-date/aquasecurity/tfsec?style=flat-square&label=release)](https://github.com/aquasecurity/tfsec/releases) |
| **Terrascan**<br>[GitHub](https://github.com/tenable/terrascan) | IaC | Compliance / security scanning for IaC | 🟢 | [![release](https://img.shields.io/github/release-date/tenable/terrascan?style=flat-square&label=release)](https://github.com/tenable/terrascan/releases) |

---

## 📋 SBOM

Software Bill of Materials generation.

| Tool | Format | Description | License | Activity |
|---|---|---|---|---|
| **Syft**<br>[GitHub](https://github.com/anchore/syft) | SPDX, CycloneDX | Generate SBOM from images, directories, and manifests | 🟢 | [![release](https://img.shields.io/github/release-date/anchore/syft?style=flat-square&label=release)](https://github.com/anchore/syft/releases) |
| **cdxgen**<br>[GitHub](https://github.com/CycloneDX/cdxgen) | CycloneDX | Universal CycloneDX SBOM generator | 🟢 | [![release](https://img.shields.io/github/release-date/CycloneDX/cdxgen?style=flat-square&label=release)](https://github.com/CycloneDX/cdxgen/releases) |
| **Trivy**<br>[GitHub](https://github.com/aquasecurity/trivy) | SPDX, CycloneDX | SBOM as part of scanning | 🟢 | [![release](https://img.shields.io/github/release-date/aquasecurity/trivy?style=flat-square&label=release)](https://github.com/aquasecurity/trivy/releases) |

---

## 🔐 Secret Detection

| Tool | Description | License | Activity |
|---|---|---|---|
| **Gitleaks**<br>[GitHub](https://github.com/gitleaks/gitleaks) | Fast secret detection in git history and filesystem | 🟢 | [![release](https://img.shields.io/github/release-date/gitleaks/gitleaks?style=flat-square&label=release)](https://github.com/gitleaks/gitleaks/releases) |
| **TruffleHog**<br>[GitHub](https://github.com/trufflesecurity/trufflehog) | Secret detection with live verification (API keys, etc.) | 🟢 | [![release](https://img.shields.io/github/release-date/trufflesecurity/trufflehog?style=flat-square&label=release)](https://github.com/trufflesecurity/trufflehog/releases) |
| **git-secret**<br>[GitHub](https://github.com/sobolevn/git-secret) | Encrypt secrets in git via GPG | 🟢 | [![release](https://img.shields.io/github/release-date/sobolevn/git-secret?style=flat-square&label=release)](https://github.com/sobolevn/git-secret/releases) |
| **detect-secrets**<br>[GitHub](https://github.com/Yelp/detect-secrets) | Enterprise-friendly baseline secret scanner (Yelp) | 🟢 | [![release](https://img.shields.io/github/release-date/Yelp/detect-secrets?style=flat-square&label=release)](https://github.com/Yelp/detect-secrets/releases) |

---

## 🛰️ Scanners

Network, web, and general-purpose vulnerability scanners.

| Tool | Type | Description | License | Activity |
|---|---|---|---|---|
| **Nmap**<br>[GitHub](https://github.com/nmap/nmap) | Network | Reference network discovery / port scanner | 🟢 | [![commit](https://img.shields.io/github/last-commit/nmap/nmap?style=flat-square&label=commit)](https://github.com/nmap/nmap/commits) |
| **Masscan**<br>[GitHub](https://github.com/robertdavidgraham/masscan) | Network | Asynchronous ultra-fast port scanner | 🟢 | [![release](https://img.shields.io/github/release-date/robertdavidgraham/masscan?style=flat-square&label=release)](https://github.com/robertdavidgraham/masscan/releases) |
| **RustScan**<br>[GitHub](https://github.com/RustScan/RustScan) | Network | Extremely fast port scanner that pipes into Nmap | 🟢 | [![release](https://img.shields.io/github/release-date/RustScan/RustScan?style=flat-square&label=release)](https://github.com/RustScan/RustScan/releases) |
| **OpenVAS / Greenbone**<br>[GitHub](https://github.com/greenbone/openvas-scanner) | Network VA | Full vulnerability assessment stack | 🟢 | [![release](https://img.shields.io/github/release-date/greenbone/openvas-scanner?style=flat-square&label=release)](https://github.com/greenbone/openvas-scanner/releases) |
| **Nessus**<br>[tenable.com](https://www.tenable.com/products/nessus) | Network VA | Commercial VA scanner by Tenable | 🔴 | — |
| **InsightVM (Nexpose)**<br>[rapid7.com](https://www.rapid7.com/products/insightvm/) | Network VA | Vulnerability management by Rapid7 | 🔴 | — |
| **Tsunami**<br>[GitHub](https://github.com/google/tsunami-security-scanner) | Network | Modular high-severity scanner by Google | 🟢 | [![release](https://img.shields.io/github/release-date/google/tsunami-security-scanner?style=flat-square&label=release)](https://github.com/google/tsunami-security-scanner/releases) |
| **testssl.sh**<br>[GitHub](https://github.com/drwetter/testssl.sh) | TLS / SSL | CLI checker for TLS/SSL ciphers, protocols, and vulns | 🟢 | [![release](https://img.shields.io/github/release-date/drwetter/testssl.sh?style=flat-square&label=release)](https://github.com/drwetter/testssl.sh/releases) |
| **SSLyze**<br>[GitHub](https://github.com/nabla-c0d3/sslyze) | TLS / SSL | Fast and powerful SSL/TLS scanning library | 🟢 | [![release](https://img.shields.io/github/release-date/nabla-c0d3/sslyze?style=flat-square&label=release)](https://github.com/nabla-c0d3/sslyze/releases) |
| **Sqlmap**<br>[GitHub](https://github.com/sqlmapproject/sqlmap) | Web / SQLi | Automated SQL Injection detection and exploitation | 🟢 | [![release](https://img.shields.io/github/release-date/sqlmapproject/sqlmap?style=flat-square&label=release)](https://github.com/sqlmapproject/sqlmap/releases) |
| **NoSQLMap**<br>[GitHub](https://github.com/codingo/NoSQLMap) | NoSQL | Audit and exploit NoSQL injection | 🟢 | [![release](https://img.shields.io/github/release-date/codingo/NoSQLMap?style=flat-square&label=release)](https://github.com/codingo/NoSQLMap/releases) |
| **WhatWeb**<br>[GitHub](https://github.com/urbanadventurer/WhatWeb) | Fingerprint | Identify CMS, frameworks, and site tech | 🟢 | [![release](https://img.shields.io/github/release-date/urbanadventurer/WhatWeb?style=flat-square&label=release)](https://github.com/urbanadventurer/WhatWeb/releases) |
| **Wappalyzer**<br>[wappalyzer.com](https://www.wappalyzer.com/) | Fingerprint | Identify technologies used on websites | 🟡 | — |
| **wappalyzergo**<br>[GitHub](https://github.com/projectdiscovery/wappalyzergo) | Fingerprint | Go port of Wappalyzer fingerprinting for CLI / pipelines | 🟢 | [![release](https://img.shields.io/github/release-date/projectdiscovery/wappalyzergo?style=flat-square&label=release)](https://github.com/projectdiscovery/wappalyzergo/releases) |
| **Xray**<br>[GitHub](https://github.com/chaitin/xray) | Web | Passive / active web scanner (Chaitin) | 🟢 | [![release](https://img.shields.io/github/release-date/chaitin/xray?style=flat-square&label=release)](https://github.com/chaitin/xray/releases) |
| **Osmedeus**<br>[GitHub](https://github.com/j3ssie/Osmedeus) | Orchestration | Workflow engine for automated recon / scan | 🟢 | [![release](https://img.shields.io/github/release-date/j3ssie/Osmedeus?style=flat-square&label=release)](https://github.com/j3ssie/Osmedeus/releases) |
| **OneForAll**<br>[GitHub](https://github.com/shmilylty/OneForAll) | Subdomain / Recon | Powerful subdomain collection | 🟢 | [![release](https://img.shields.io/github/release-date/shmilylty/OneForAll?style=flat-square&label=release)](https://github.com/shmilylty/OneForAll/releases) |
| **Sn1per**<br>[GitHub](https://github.com/1N3/Sn1per) | Pentest Automation | Automated pentest framework | 🟡 | [![release](https://img.shields.io/github/release-date/1N3/Sn1per?style=flat-square&label=release)](https://github.com/1N3/Sn1per/releases) |
| **AutoRecon**<br>[GitHub](https://github.com/Tib3rius/AutoRecon) | Recon | Multi-threaded network recon for CTF / pentest | 🟢 | [![commit](https://img.shields.io/github/last-commit/Tib3rius/AutoRecon?style=flat-square&label=commit)](https://github.com/Tib3rius/AutoRecon/commits) |
| **Legion**<br>[GitHub](https://github.com/GoVanguard/legion) | Network GUI | GUI wrapper around Nmap and other scanners | 🟢 | [![release](https://img.shields.io/github/release-date/GoVanguard/legion?style=flat-square&label=release)](https://github.com/GoVanguard/legion/releases) |
| **Raccoon**<br>[GitHub](https://github.com/evyatarmeged/Raccoon) | Recon | Asynchronous recon / offensive reconnaissance | 🟢 | [![commit](https://img.shields.io/github/last-commit/evyatarmeged/Raccoon?style=flat-square&label=commit)](https://github.com/evyatarmeged/Raccoon/commits) |
| **Scanless**<br>[GitHub](https://github.com/vesche/scanless) | Network | Port scan via public online scanners (opsec) | 🟢 | [![release](https://img.shields.io/github/release-date/vesche/scanless?style=flat-square&label=release)](https://github.com/vesche/scanless/releases) |
| **Golismero**<br>[GitHub](https://github.com/golismero/golismero) | Framework | Security framework with plugins | 🟢 | [![commit](https://img.shields.io/github/last-commit/golismero/golismero?style=flat-square&label=commit)](https://github.com/golismero/golismero/commits) |
| **Arachni**<br>[GitHub](https://github.com/Arachni/arachni) | Web | Modular web scanner (maintenance mode) | 🟢 | [![tag](https://img.shields.io/github/v/tag/Arachni/arachni?style=flat-square&label=tag)](https://github.com/Arachni/arachni/tags) |
| **Acunetix**<br>[acunetix.com](https://www.acunetix.com/) | Web | Commercial DAST | 🔴 | — |
| **Invicti (Netsparker)**<br>[invicti.com](https://www.invicti.com/) | Web | Commercial DAST with proof-based scanning | 🔴 | — |
| **ScanOval**<br>[bdu.fstec.ru](https://bdu.fstec.ru/site/scanoval) | OVAL / BDU | OVAL-based vulnerability checks (FSTEC BDU) | 🌐 | — |
| **Puma Scan**<br>[GitHub](https://github.com/pumasecurity/puma-scan) | .NET SAST | Roslyn analyzer for .NET security | 🟡 | [![release](https://img.shields.io/github/release-date/pumasecurity/puma-scan?style=flat-square&label=release)](https://github.com/pumasecurity/puma-scan/releases) |

---

## 🧭 Recon & Enumeration

| Tool | Description | License | Activity |
|---|---|---|---|
| **Amass**<br>[GitHub](https://github.com/owasp-amass/amass) | OWASP: deep subdomain enumeration and attack-surface mapping | 🟢 | [![release](https://img.shields.io/github/release-date/owasp-amass/amass?style=flat-square&label=release)](https://github.com/owasp-amass/amass/releases) |
| **subfinder**<br>[GitHub](https://github.com/projectdiscovery/subfinder) | Passive subdomain discovery (ProjectDiscovery) | 🟢 | [![release](https://img.shields.io/github/release-date/projectdiscovery/subfinder?style=flat-square&label=release)](https://github.com/projectdiscovery/subfinder/releases) |
| **httpx**<br>[GitHub](https://github.com/projectdiscovery/httpx) | Fast HTTP probing / tech detection | 🟢 | [![release](https://img.shields.io/github/release-date/projectdiscovery/httpx?style=flat-square&label=release)](https://github.com/projectdiscovery/httpx/releases) |
| **dnsx**<br>[GitHub](https://github.com/projectdiscovery/dnsx) | DNS toolkit for resolve and enumeration | 🟢 | [![release](https://img.shields.io/github/release-date/projectdiscovery/dnsx?style=flat-square&label=release)](https://github.com/projectdiscovery/dnsx/releases) |
| **Chaos**<br>[GitHub](https://github.com/projectdiscovery/chaos-client) | ProjectDiscovery DNS dataset client for passive recon | 🟢 | [![release](https://img.shields.io/github/release-date/projectdiscovery/chaos-client?style=flat-square&label=release)](https://github.com/projectdiscovery/chaos-client/releases) |
| **ffuf**<br>[GitHub](https://github.com/ffuf/ffuf) | Fast web fuzzer (dirs, vhosts, params) | 🟢 | [![release](https://img.shields.io/github/release-date/ffuf/ffuf?style=flat-square&label=release)](https://github.com/ffuf/ffuf/releases) |
| **gobuster**<br>[GitHub](https://github.com/OJ/gobuster) | Directory, DNS, and vhost brute-forcing | 🟢 | [![release](https://img.shields.io/github/release-date/OJ/gobuster?style=flat-square&label=release)](https://github.com/OJ/gobuster/releases) |
| **feroxbuster**<br>[GitHub](https://github.com/epi052/feroxbuster) | Fast, recursive content discovery written in Rust | 🟢 | [![release](https://img.shields.io/github/release-date/epi052/feroxbuster?style=flat-square&label=release)](https://github.com/epi052/feroxbuster/releases) |
| **Arjun**<br>[GitHub](https://github.com/s0md3v/Arjun) | HTTP parameter discovery suite | 🟢 | [![release](https://img.shields.io/github/release-date/s0md3v/Arjun?style=flat-square&label=release)](https://github.com/s0md3v/Arjun/releases) |
| **knock**<br>[GitHub](https://github.com/guelfoweb/knock) | Subdomain enumeration via wordlist + DNS | 🟢 | [![release](https://img.shields.io/github/release-date/guelfoweb/knock?style=flat-square&label=release)](https://github.com/guelfoweb/knock/releases) |
| **subDomainsBrute**<br>[GitHub](https://github.com/lijiejie/subDomainsBrute) | Multi-threaded subdomain brute-force | 🟢 | [![release](https://img.shields.io/github/release-date/lijiejie/subDomainsBrute?style=flat-square&label=release)](https://github.com/lijiejie/subDomainsBrute/releases) |
| **SubDomain3**<br>[GitHub](https://github.com/yanxiu0614/subdomain3) | High-speed subdomain scanner | 🟢 | [![release](https://img.shields.io/github/release-date/yanxiu0614/subdomain3?style=flat-square&label=release)](https://github.com/yanxiu0614/subdomain3/releases) |
| **domained**<br>[GitHub](https://github.com/TypeError/domained) | Wrapper around multiple subdomain tools | 🟢 | [![commit](https://img.shields.io/github/last-commit/TypeError/domained?style=flat-square&label=commit)](https://github.com/TypeError/domained/commits) |
| **katana**<br>[GitHub](https://github.com/projectdiscovery/katana) | Next-gen crawling / spidering | 🟢 | [![release](https://img.shields.io/github/release-date/projectdiscovery/katana?style=flat-square&label=release)](https://github.com/projectdiscovery/katana/releases) |
| **gau**<br>[GitHub](https://github.com/lc/gau) | Fetch known URLs from public sources | 🟢 | [![release](https://img.shields.io/github/release-date/lc/gau?style=flat-square&label=release)](https://github.com/lc/gau/releases) |
| **waybackurls**<br>[GitHub](https://github.com/tomnomnom/waybackurls) | Fetch URLs from the Wayback Machine for a domain | 🟢 | [![release](https://img.shields.io/github/release-date/tomnomnom/waybackurls?style=flat-square&label=release)](https://github.com/tomnomnom/waybackurls/releases) |
| **hakrawler**<br>[GitHub](https://github.com/hakluke/hakrawler) | Simple, fast web crawler for gathering URLs / endpoints | 🟢 | [![release](https://img.shields.io/github/release-date/hakluke/hakrawler?style=flat-square&label=release)](https://github.com/hakluke/hakrawler/releases) |

---

## 🏢 Active Directory & Internal

Identity attack-path mapping and Windows / AD assessment tooling.

| Tool | Description | License | Activity |
|---|---|---|---|
| **BloodHound**<br>[GitHub](https://github.com/SpecterOps/BloodHound) | Graph analysis of AD / Entra ID attack paths | 🟡 | [![release](https://img.shields.io/github/release-date/SpecterOps/BloodHound?style=flat-square&label=release)](https://github.com/SpecterOps/BloodHound/releases) |
| **SharpHound**<br>[GitHub](https://github.com/SpecterOps/SharpHound) | BloodHound data collector for Active Directory | 🟢 | [![release](https://img.shields.io/github/release-date/SpecterOps/SharpHound?style=flat-square&label=release)](https://github.com/SpecterOps/SharpHound/releases) |
| **Impacket**<br>[GitHub](https://github.com/fortra/impacket) | Python collection of Windows network protocol tools | 🟢 | [![release](https://img.shields.io/github/release-date/fortra/impacket?style=flat-square&label=release)](https://github.com/fortra/impacket/releases) |
| **NetExec**<br>[GitHub](https://github.com/Pennyw0rth/NetExec) | Network authentication / assessment (CrackMapExec successor) | 🟢 | [![release](https://img.shields.io/github/release-date/Pennyw0rth/NetExec?style=flat-square&label=release)](https://github.com/Pennyw0rth/NetExec/releases) |
| **Responder**<br>[GitHub](https://github.com/lgandx/Responder) | LLMNR / NBT-NS / mDNS poisoner for credential capture | 🟢 | [![tag](https://img.shields.io/github/v/tag/lgandx/Responder?style=flat-square&label=tag)](https://github.com/lgandx/Responder/tags) |
| **Certipy**<br>[GitHub](https://github.com/ly4k/Certipy) | Active Directory Certificate Services enumeration & abuse | 🟢 | [![release](https://img.shields.io/github/release-date/ly4k/Certipy?style=flat-square&label=release)](https://github.com/ly4k/Certipy/releases) |
| **Rubeus**<br>[GitHub](https://github.com/GhostPack/Rubeus) | Kerberos abuse toolkit for offensive AD ops | 🟢 | [![release](https://img.shields.io/github/release-date/GhostPack/Rubeus?style=flat-square&label=release)](https://github.com/GhostPack/Rubeus/releases) |
| **PowerView**<br>[GitHub](https://github.com/PowerShellMafia/PowerSploit) | PowerShell AD situational awareness (PowerSploit) | 🟢 | [![release](https://img.shields.io/github/release-date/PowerShellMafia/PowerSploit?style=flat-square&label=release)](https://github.com/PowerShellMafia/PowerSploit/releases) |

---

## 🔑 Password Cracking

| Tool | Description | License | Activity |
|---|---|---|---|
| **Hashcat**<br>[GitHub](https://github.com/hashcat/hashcat) | Advanced GPU password recovery | 🟢 | [![release](https://img.shields.io/github/release-date/hashcat/hashcat?style=flat-square&label=release)](https://github.com/hashcat/hashcat/releases) |
| **John the Ripper**<br>[GitHub](https://github.com/openwall/john) | Fast password cracker (CPU + many formats) | 🟢 | [![tag](https://img.shields.io/github/v/tag/openwall/john?style=flat-square&label=tag)](https://github.com/openwall/john/tags) |
| **Hydra**<br>[GitHub](https://github.com/vanhauser-thc/thc-hydra) | Parallel online brute-force for network services | 🟢 | [![release](https://img.shields.io/github/release-date/vanhauser-thc/thc-hydra?style=flat-square&label=release)](https://github.com/vanhauser-thc/thc-hydra/releases) |
| **Medusa**<br>[GitHub](https://github.com/jmk-foofus/medusa) | Speedy, parallel, modular login brute-forcer | 🟢 | [![release](https://img.shields.io/github/release-date/jmk-foofus/medusa?style=flat-square&label=release)](https://github.com/jmk-foofus/medusa/releases) |

---

## ☁️ Cloud & Container Security

CSPM, CNAPP-adjacent OSS, and Kubernetes hardening.

| Tool | Focus | Description | License | Activity |
|---|---|---|---|---|
| **Prowler**<br>[GitHub](https://github.com/prowler-cloud/prowler) | CSPM | Multi-cloud security assessment (AWS, Azure, GCP, …) | 🟢 | [![release](https://img.shields.io/github/release-date/prowler-cloud/prowler?style=flat-square&label=release)](https://github.com/prowler-cloud/prowler/releases) |
| **ScoutSuite**<br>[GitHub](https://github.com/nccgroup/ScoutSuite) | CSPM | Multi-cloud security auditing tool | 🟢 | [![release](https://img.shields.io/github/release-date/nccgroup/ScoutSuite?style=flat-square&label=release)](https://github.com/nccgroup/ScoutSuite/releases) |
| **CloudMapper**<br>[GitHub](https://github.com/duo-labs/cloudmapper) | AWS | Network visualization and inventory for AWS accounts | 🟢 | [![release](https://img.shields.io/github/release-date/duo-labs/cloudmapper?style=flat-square&label=release)](https://github.com/duo-labs/cloudmapper/releases) |
| **kube-bench**<br>[GitHub](https://github.com/aquasecurity/kube-bench) | Kubernetes | CIS Kubernetes Benchmark checks | 🟢 | [![release](https://img.shields.io/github/release-date/aquasecurity/kube-bench?style=flat-square&label=release)](https://github.com/aquasecurity/kube-bench/releases) |
| **kube-hunter**<br>[GitHub](https://github.com/aquasecurity/kube-hunter) | Kubernetes | Hunt for security weaknesses in K8s clusters | 🟢 | [![release](https://img.shields.io/github/release-date/aquasecurity/kube-hunter?style=flat-square&label=release)](https://github.com/aquasecurity/kube-hunter/releases) |
| **Falco**<br>[GitHub](https://github.com/falcosecurity/falco) | Runtime | Cloud-native runtime security / threat detection | 🟢 | [![release](https://img.shields.io/github/release-date/falcosecurity/falco?style=flat-square&label=release)](https://github.com/falcosecurity/falco/releases) |
| **Trivy**<br>[GitHub](https://github.com/aquasecurity/trivy) | Containers / IaC | Image, filesystem, and IaC vulnerability scanner | 🟢 | [![release](https://img.shields.io/github/release-date/aquasecurity/trivy?style=flat-square&label=release)](https://github.com/aquasecurity/trivy/releases) |
| **Docker Bench**<br>[GitHub](https://github.com/docker/docker-bench-security) | Containers | CIS Docker Benchmark script | 🟢 | [![release](https://img.shields.io/github/release-date/docker/docker-bench-security?style=flat-square&label=release)](https://github.com/docker/docker-bench-security/releases) |
| **Orca Security**<br>[orca.security](https://orca.security/) | CNAPP | Commercial agentless cloud security platform | 🔴 | — |
| **Wiz**<br>[wiz.io](https://www.wiz.io/) | CNAPP | Commercial cloud security platform | 🔴 | — |
| **Prisma Cloud**<br>[paloaltonetworks.com](https://www.paloaltonetworks.com/prisma/cloud) | CNAPP | Commercial CNAPP by Palo Alto Networks | 🔴 | — |

---

## 📡 Network Analysis & IDS

| Tool | Description | License | Activity |
|---|---|---|---|
| **Wireshark**<br>[GitHub](https://github.com/wireshark/wireshark) | Network protocol analyzer | 🟢 | [![tag](https://img.shields.io/github/v/tag/wireshark/wireshark?style=flat-square&label=tag)](https://github.com/wireshark/wireshark/tags) |
| **tcpdump**<br>[GitHub](https://github.com/the-tcpdump-group/tcpdump) | Classic command-line packet analyzer | 🟢 | [![tag](https://img.shields.io/github/v/tag/the-tcpdump-group/tcpdump?style=flat-square&label=tag)](https://github.com/the-tcpdump-group/tcpdump/tags) |
| **Zeek**<br>[GitHub](https://github.com/zeek/zeek) | Network security monitoring framework (formerly Bro) | 🟢 | [![release](https://img.shields.io/github/release-date/zeek/zeek?style=flat-square&label=release)](https://github.com/zeek/zeek/releases) |
| **Suricata**<br>[GitHub](https://github.com/OISF/suricata) | High-performance IDS / IPS / NSM engine | 🟢 | [![release](https://img.shields.io/github/release-date/OISF/suricata?style=flat-square&label=release)](https://github.com/OISF/suricata/releases) |
| **Snort**<br>[GitHub](https://github.com/snort3/snort3) | Network intrusion detection and prevention | 🟢 | [![release](https://img.shields.io/github/release-date/snort3/snort3?style=flat-square&label=release)](https://github.com/snort3/snort3/releases) |
| **Wazuh**<br>[GitHub](https://github.com/wazuh/wazuh) | Open-source XDR / SIEM platform | 🟢 | [![release](https://img.shields.io/github/release-date/wazuh/wazuh?style=flat-square&label=release)](https://github.com/wazuh/wazuh/releases) |
| **OSSEC**<br>[GitHub](https://github.com/ossec/ossec-hids) | Host-based intrusion detection system | 🟢 | [![release](https://img.shields.io/github/release-date/ossec/ossec-hids?style=flat-square&label=release)](https://github.com/ossec/ossec-hids/releases) |
| **ModSecurity**<br>[GitHub](https://github.com/owasp-modsecurity/ModSecurity) | Open-source web application firewall engine | 🟢 | [![release](https://img.shields.io/github/release-date/owasp-modsecurity/ModSecurity?style=flat-square&label=release)](https://github.com/owasp-modsecurity/ModSecurity/releases) |

---

## 🔬 Forensics & Incident Response

| Tool | Description | License | Activity |
|---|---|---|---|
| **Volatility 3**<br>[GitHub](https://github.com/volatilityfoundation/volatility3) | Advanced memory forensics framework | 🟢 | [![release](https://img.shields.io/github/release-date/volatilityfoundation/volatility3?style=flat-square&label=release)](https://github.com/volatilityfoundation/volatility3/releases) |
| **Velociraptor**<br>[GitHub](https://github.com/Velocidex/velociraptor) | Endpoint visibility and digital forensics / IR | 🟢 | [![release](https://img.shields.io/github/release-date/Velocidex/velociraptor?style=flat-square&label=release)](https://github.com/Velocidex/velociraptor/releases) |
| **Autopsy**<br>[GitHub](https://github.com/sleuthkit/autopsy) | Digital forensics platform (GUI on The Sleuth Kit) | 🟢 | [![release](https://img.shields.io/github/release-date/sleuthkit/autopsy?style=flat-square&label=release)](https://github.com/sleuthkit/autopsy/releases) |
| **The Sleuth Kit**<br>[GitHub](https://github.com/sleuthkit/sleuthkit) | Library and tools for disk image forensics | 🟢 | [![release](https://img.shields.io/github/release-date/sleuthkit/sleuthkit?style=flat-square&label=release)](https://github.com/sleuthkit/sleuthkit/releases) |
| **Plaso**<br>[GitHub](https://github.com/log2timeline/plaso) | Super timeline engine for digital forensics | 🟢 | [![release](https://img.shields.io/github/release-date/log2timeline/plaso?style=flat-square&label=release)](https://github.com/log2timeline/plaso/releases) |
| **osquery**<br>[GitHub](https://github.com/osquery/osquery) | SQL-powered operating system instrumentation | 🟢 | [![release](https://img.shields.io/github/release-date/osquery/osquery?style=flat-square&label=release)](https://github.com/osquery/osquery/releases) |
| **TheHive**<br>[GitHub](https://github.com/TheHive-Project/TheHive) | Scalable Security Incident Response Platform | 🟢 | [![release](https://img.shields.io/github/release-date/TheHive-Project/TheHive?style=flat-square&label=release)](https://github.com/TheHive-Project/TheHive/releases) |
| **Cortex**<br>[GitHub](https://github.com/TheHive-Project/Cortex) | Observable analysis & active response engine | 🟢 | [![release](https://img.shields.io/github/release-date/TheHive-Project/Cortex?style=flat-square&label=release)](https://github.com/TheHive-Project/Cortex/releases) |

---

## 🧠 Threat Intelligence

| Tool | Description | License | Activity |
|---|---|---|---|
| **MISP**<br>[GitHub](https://github.com/MISP/MISP) | Open-source threat intelligence sharing platform | 🟢 | [![release](https://img.shields.io/github/release-date/MISP/MISP?style=flat-square&label=release)](https://github.com/MISP/MISP/releases) |
| **OpenCTI**<br>[GitHub](https://github.com/OpenCTI-Platform/opencti) | Open Cyber Threat Intelligence platform | 🟢 | [![release](https://img.shields.io/github/release-date/OpenCTI-Platform/opencti?style=flat-square&label=release)](https://github.com/OpenCTI-Platform/opencti/releases) |
| **OpenTAXII**<br>[GitHub](https://github.com/eclecticiq/OpenTAXII) | TAXII server implementation for CTI exchange | 🟢 | [![release](https://img.shields.io/github/release-date/eclecticiq/OpenTAXII?style=flat-square&label=release)](https://github.com/eclecticiq/OpenTAXII/releases) |
| **YARA**<br>[GitHub](https://github.com/VirusTotal/yara) | Pattern-matching for malware researchers | 🟢 | [![release](https://img.shields.io/github/release-date/VirusTotal/yara?style=flat-square&label=release)](https://github.com/VirusTotal/yara/releases) |
| **Sigma**<br>[GitHub](https://github.com/SigmaHQ/sigma) | Generic signature format for SIEM systems | 🟢 | [![release](https://img.shields.io/github/release-date/SigmaHQ/sigma?style=flat-square&label=release)](https://github.com/SigmaHQ/sigma/releases) |
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
| **Ghidra**<br>[GitHub](https://github.com/NationalSecurityAgency/ghidra) | NSA open-source software reverse engineering suite | 🟢 | [![release](https://img.shields.io/github/release-date/NationalSecurityAgency/ghidra?style=flat-square&label=release)](https://github.com/NationalSecurityAgency/ghidra/releases) |
| **radare2**<br>[GitHub](https://github.com/radareorg/radare2) | UNIX-like reverse engineering framework | 🟢 | [![release](https://img.shields.io/github/release-date/radareorg/radare2?style=flat-square&label=release)](https://github.com/radareorg/radare2/releases) |
| **Cutter**<br>[GitHub](https://github.com/rizinorg/cutter) | Free GUI for Rizin / reverse engineering | 🟢 | [![release](https://img.shields.io/github/release-date/rizinorg/cutter?style=flat-square&label=release)](https://github.com/rizinorg/cutter/releases) |
| **Binary Ninja**<br>[binary.ninja](https://binary.ninja/) | Commercial reverse engineering platform | 🔴 | — |
| **IDA**<br>[hex-rays.com](https://hex-rays.com/ida-pro/) | Commercial industry-standard disassembler / debugger | 🔴 | — |
| **Binwalk**<br>[GitHub](https://github.com/ReFirmLabs/binwalk) | Firmware analysis and extraction tool | 🟢 | [![release](https://img.shields.io/github/release-date/ReFirmLabs/binwalk?style=flat-square&label=release)](https://github.com/ReFirmLabs/binwalk/releases) |
| **PE-bear**<br>[GitHub](https://github.com/hasherezade/pe-bear) | PE file reversing toolkit | 🟢 | [![release](https://img.shields.io/github/release-date/hasherezade/pe-bear?style=flat-square&label=release)](https://github.com/hasherezade/pe-bear/releases) |
| **Detect It Easy**<br>[GitHub](https://github.com/horsicq/Detect-It-Easy) | Packer / compiler / crypto detection for binaries | 🟢 | [![tag](https://img.shields.io/github/v/tag/horsicq/Detect-It-Easy?style=flat-square&label=tag)](https://github.com/horsicq/Detect-It-Easy/tags) |

---

## 📚 Wordlists & Payloads

| Tool | Description | License | Activity |
|---|---|---|---|
| **SecLists**<br>[GitHub](https://github.com/danielmiessler/SecLists) | Collection of security wordlists and payloads | 🟢 | [![release](https://img.shields.io/github/release-date/danielmiessler/SecLists?style=flat-square&label=release)](https://github.com/danielmiessler/SecLists/releases) |
| **PayloadsAllTheThings**<br>[GitHub](https://github.com/swisskyrepo/PayloadsAllTheThings) | Useful payloads and bypasses for Web AppSec | 🟢 | [![release](https://img.shields.io/github/release-date/swisskyrepo/PayloadsAllTheThings?style=flat-square&label=release)](https://github.com/swisskyrepo/PayloadsAllTheThings/releases) |
| **FuzzDB**<br>[GitHub](https://github.com/fuzzdb-project/fuzzdb) | Attack patterns, discovery dictionaries, and injectables | 🟢 | [![commit](https://img.shields.io/github/last-commit/fuzzdb-project/fuzzdb?style=flat-square&label=commit)](https://github.com/fuzzdb-project/fuzzdb/commits) |
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
