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

In tables, the **name** is on the first line and the **link** on the next (`<br>`). Updated badges are [shields.io](https://shields.io) `github/last-commit` (compact). Non-GitHub products show `—`.

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

| Tool | Description | License | Updated |
|---|---|---|---|
| **Sherlock**<br>[GitHub](https://github.com/sherlock-project/sherlock) | Hunt usernames across hundreds of social networks | 🟢 | [![updated](https://img.shields.io/github/last-commit/sherlock-project/sherlock?style=flat-square&label=)](https://github.com/sherlock-project/sherlock) |
| **theHarvester**<br>[GitHub](https://github.com/laramies/theHarvester) | Gather emails, subdomains, hosts, and people from public sources | 🟢 | [![updated](https://img.shields.io/github/last-commit/laramies/theHarvester?style=flat-square&label=)](https://github.com/laramies/theHarvester) |
| **SpiderFoot**<br>[GitHub](https://github.com/smicallef/spiderfoot) | Automated OSINT with hundreds of modules and a web UI | 🟢 | [![updated](https://img.shields.io/github/last-commit/smicallef/spiderfoot?style=flat-square&label=)](https://github.com/smicallef/spiderfoot) |
| **Recon-ng**<br>[GitHub](https://github.com/lanmaster53/recon-ng) | Modular reconnaissance framework (Metasploit-style) | 🟢 | [![updated](https://img.shields.io/github/last-commit/lanmaster53/recon-ng?style=flat-square&label=)](https://github.com/lanmaster53/recon-ng) |
| **Photon**<br>[GitHub](https://github.com/s0md3v/Photon) | Fast crawler for OSINT data extraction from websites | 🟢 | [![updated](https://img.shields.io/github/last-commit/s0md3v/Photon?style=flat-square&label=)](https://github.com/s0md3v/Photon) |
| **Maltego**<br>[maltego.com](https://www.maltego.com/) | Graph visualization of people, domains, and infrastructure | 🟡 | — |
| **R3CON1Z3R**<br>[GitHub](https://github.com/abdulgaphy/r3con1z3r) | Lightweight OSINT script for target footprinting | 🟢 | [![updated](https://img.shields.io/github/last-commit/abdulgaphy/r3con1z3r?style=flat-square&label=)](https://github.com/abdulgaphy/r3con1z3r) |
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

| Tool | Description | License | Updated |
|---|---|---|---|
| **DefectDojo**<br>[GitHub](https://github.com/DefectDojo/django-DefectDojo) | DevSecOps platform: report import, triage, metrics, SLA | 🟢 | [![updated](https://img.shields.io/github/last-commit/DefectDojo/django-DefectDojo?style=flat-square&label=)](https://github.com/DefectDojo/django-DefectDojo) |
| **Faraday**<br>[GitHub](https://github.com/infobyte/faraday) | Collaborative pentest IDE / vulnerability management | 🟢 | [![updated](https://img.shields.io/github/last-commit/infobyte/faraday?style=flat-square&label=)](https://github.com/infobyte/faraday) |
| **ArcherySec**<br>[GitHub](https://github.com/archerysec/archerysec) | Vulnerability assessment & management with scanner integrations | 🟢 | [![updated](https://img.shields.io/github/last-commit/archerysec/archerysec?style=flat-square&label=)](https://github.com/archerysec/archerysec) |
| **reNgine**<br>[GitHub](https://github.com/yogeshojha/rengine) | Automated recon + vulnerability management with web UI | 🟢 | [![updated](https://img.shields.io/github/last-commit/yogeshojha/rengine?style=flat-square&label=)](https://github.com/yogeshojha/rengine) |
| **Vuls**<br>[GitHub](https://github.com/future-architect/vuls) | Agentless vulnerability scanner for Linux / FreeBSD | 🟢 | [![updated](https://img.shields.io/github/last-commit/future-architect/vuls?style=flat-square&label=)](https://github.com/future-architect/vuls) |
| **OWASP Threat Dragon**<br>[GitHub](https://github.com/OWASP/threat-dragon) | Threat modeling tool for STRIDE-style diagrams | 🟢 | [![updated](https://img.shields.io/github/last-commit/OWASP/threat-dragon?style=flat-square&label=)](https://github.com/OWASP/threat-dragon) |

---

## ⚒️ Analysis & Exploit Frameworks

| Tool | Category | Description | License | Updated |
|---|---|---|---|---|
| **Metasploit**<br>[GitHub](https://github.com/rapid7/metasploit-framework) | Exploit Framework | Classic exploit, payload, and post-exploitation framework | 🟡 | [![updated](https://img.shields.io/github/last-commit/rapid7/metasploit-framework?style=flat-square&label=)](https://github.com/rapid7/metasploit-framework) |
| **RouterSploit**<br>[GitHub](https://github.com/threat9/routersploit) | Exploit Framework | Exploits and checks for embedded / network devices | 🟢 | [![updated](https://img.shields.io/github/last-commit/threat9/routersploit?style=flat-square&label=)](https://github.com/threat9/routersploit) |
| **BeEF**<br>[GitHub](https://github.com/beefproject/beef) | Exploit Framework | Browser Exploitation Framework | 🟢 | [![updated](https://img.shields.io/github/last-commit/beefproject/beef?style=flat-square&label=)](https://github.com/beefproject/beef) |
| **Sliver**<br>[GitHub](https://github.com/BishopFox/sliver) | C2 | Open-source adversary emulation / C2 framework | 🟢 | [![updated](https://img.shields.io/github/last-commit/BishopFox/sliver?style=flat-square&label=)](https://github.com/BishopFox/sliver) |
| **Havoc**<br>[GitHub](https://github.com/HavocFramework/Havoc) | C2 | Modern post-exploitation command and control | 🟢 | [![updated](https://img.shields.io/github/last-commit/HavocFramework/Havoc?style=flat-square&label=)](https://github.com/HavocFramework/Havoc) |
| **MobSF**<br>[GitHub](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | Mobile | Static and dynamic analysis for Android / iOS | 🟢 | [![updated](https://img.shields.io/github/last-commit/MobSF/Mobile-Security-Framework-MobSF?style=flat-square&label=)](https://github.com/MobSF/Mobile-Security-Framework-MobSF) |
| **Frida**<br>[GitHub](https://github.com/frida/frida) | Dynamic Instrumentation | Dynamic instrumentation toolkit for apps | 🟢 | [![updated](https://img.shields.io/github/last-commit/frida/frida?style=flat-square&label=)](https://github.com/frida/frida) |
| **Objection**<br>[GitHub](https://github.com/sensepost/objection) | Mobile | Runtime mobile exploration powered by Frida | 🟢 | [![updated](https://img.shields.io/github/last-commit/sensepost/objection?style=flat-square&label=)](https://github.com/sensepost/objection) |
| **RedTeam C# Scripts**<br>[GitHub](https://github.com/Mr-Un1k0d3r/RedTeamCSharpScripts) | Red Team | Collection of C# scripts for red team operations | 🟢 | [![updated](https://img.shields.io/github/last-commit/Mr-Un1k0d3r/RedTeamCSharpScripts?style=flat-square&label=)](https://github.com/Mr-Un1k0d3r/RedTeamCSharpScripts) |
| **Atomic Red Team**<br>[GitHub](https://github.com/redcanaryco/atomic-red-team) | Adversary Emulation | Small, focused tests mapped to ATT&CK techniques | 🟢 | [![updated](https://img.shields.io/github/last-commit/redcanaryco/atomic-red-team?style=flat-square&label=)](https://github.com/redcanaryco/atomic-red-team) |
| **CALDERA**<br>[GitHub](https://github.com/mitre/caldera) | Adversary Emulation | Automated adversary emulation platform by MITRE | 🟢 | [![updated](https://img.shields.io/github/last-commit/mitre/caldera?style=flat-square&label=)](https://github.com/mitre/caldera) |

---

## 🧰 Web Proxies & Manual Testing

Intercept, replay, and mutate HTTP(S) traffic during web assessments.

| Tool | Description | License | Updated |
|---|---|---|---|
| **Burp Suite**<br>[portswigger.net](https://portswigger.net/burp) | Industry-standard web security testing platform (Community / Pro) | 🟡 | — |
| **Caido**<br>[caido.io](https://caido.io/) | Modern lightweight web proxy for bug bounty and pentest | 🟡 | [![updated](https://img.shields.io/github/last-commit/caido/caido?style=flat-square&label=)](https://github.com/caido/caido) |
| **mitmproxy**<br>[GitHub](https://github.com/mitmproxy/mitmproxy) | Interactive TLS-capable intercepting HTTP proxy (CLI + web) | 🟢 | [![updated](https://img.shields.io/github/last-commit/mitmproxy/mitmproxy?style=flat-square&label=)](https://github.com/mitmproxy/mitmproxy) |
| **OWASP ZAP**<br>[GitHub](https://github.com/zaproxy/zaproxy) | Free proxy + automated scanner | 🟢 | [![updated](https://img.shields.io/github/last-commit/zaproxy/zaproxy?style=flat-square&label=)](https://github.com/zaproxy/zaproxy) |
| **WATOBO**<br>[GitHub](https://github.com/siberas/watobo) | Intercepting proxy + scanner for pentests | 🟢 | [![updated](https://img.shields.io/github/last-commit/siberas/watobo?style=flat-square&label=)](https://github.com/siberas/watobo) |

---

## 🔎 SAST — Static Analysis

Find vulnerabilities in source code without running the application.

| Tool | Languages / scope | Description | License | Updated |
|---|---|---|---|---|
| **Semgrep**<br>[GitHub](https://github.com/semgrep/semgrep) | 30+ languages | Fast pattern-based SAST with YAML rules; CI-friendly | 🟡 | [![updated](https://img.shields.io/github/last-commit/semgrep/semgrep?style=flat-square&label=)](https://github.com/semgrep/semgrep) |
| **CodeQL**<br>[codeql.github.com](https://codeql.github.com/) | Multilang | Semantic code analysis from GitHub (query-as-code) | 🟡 | — |
| **Bearer**<br>[GitHub](https://github.com/Bearer/bearer) | JS/TS, Ruby, PHP, Java, Go, Python | SAST focused on data flows and privacy | 🟢 | [![updated](https://img.shields.io/github/last-commit/Bearer/bearer?style=flat-square&label=)](https://github.com/Bearer/bearer) |
| **Bandit**<br>[GitHub](https://github.com/PyCQA/bandit) | Python | Common security issues in Python | 🟢 | [![updated](https://img.shields.io/github/last-commit/PyCQA/bandit?style=flat-square&label=)](https://github.com/PyCQA/bandit) |
| **Brakeman**<br>[GitHub](https://github.com/presidentbeef/brakeman) | Ruby on Rails | Rails-focused static security scanner | 🟢 | [![updated](https://img.shields.io/github/last-commit/presidentbeef/brakeman?style=flat-square&label=)](https://github.com/presidentbeef/brakeman) |
| **Find Security Bugs**<br>[GitHub](https://github.com/find-sec-bugs/find-sec-bugs) | Java, Android, Scala, Kotlin, Groovy | SpotBugs plugin for web / Android security | 🟢 | [![updated](https://img.shields.io/github/last-commit/find-sec-bugs/find-sec-bugs?style=flat-square&label=)](https://github.com/find-sec-bugs/find-sec-bugs) |
| **SpotBugs**<br>[GitHub](https://github.com/spotbugs/spotbugs) | Java | Static analysis of Java bytecode | 🟢 | [![updated](https://img.shields.io/github/last-commit/spotbugs/spotbugs?style=flat-square&label=)](https://github.com/spotbugs/spotbugs) |
| **PMD**<br>[GitHub](https://github.com/pmd/pmd) | Multilang | Static analysis for quality and security rules | 🟢 | [![updated](https://img.shields.io/github/last-commit/pmd/pmd?style=flat-square&label=)](https://github.com/pmd/pmd) |
| **Security Code Scan**<br>[GitHub](https://github.com/security-code-scan/security-code-scan) | C#, VB.NET | Roslyn analyzer for .NET vulnerabilities | 🟢 | [![updated](https://img.shields.io/github/last-commit/security-code-scan/security-code-scan?style=flat-square&label=)](https://github.com/security-code-scan/security-code-scan) |
| **Infer#**<br>[GitHub](https://github.com/microsoft/infersharp) | C# | Interprocedural .NET analysis based on Facebook Infer | 🟢 | [![updated](https://img.shields.io/github/last-commit/microsoft/infersharp?style=flat-square&label=)](https://github.com/microsoft/infersharp) |
| **Insider**<br>[GitHub](https://github.com/insidersec/insider) | Java, Kotlin, Swift, .NET, JS | CLI SAST for multiple stacks | 🟢 | [![updated](https://img.shields.io/github/last-commit/insidersec/insider?style=flat-square&label=)](https://github.com/insidersec/insider) |
| **Codechecker**<br>[GitHub](https://github.com/Ericsson/codechecker) | C/C++ | Wrapper around Clang Static Analyzer / Clang-Tidy | 🟢 | [![updated](https://img.shields.io/github/last-commit/Ericsson/codechecker?style=flat-square&label=)](https://github.com/Ericsson/codechecker) |
| **Cppcheck**<br>[GitHub](https://github.com/danmar/cppcheck) | C/C++ | Static analysis focused on undefined behavior | 🟢 | [![updated](https://img.shields.io/github/last-commit/danmar/cppcheck?style=flat-square&label=)](https://github.com/danmar/cppcheck) |
| **LLVM Clang SA**<br>[GitHub](https://github.com/llvm/llvm-project) | C, C++, Obj-C | Clang Static Analyzer | 🟢 | [![updated](https://img.shields.io/github/last-commit/llvm/llvm-project?style=flat-square&label=)](https://github.com/llvm/llvm-project) |
| **PVS-Studio**<br>[pvs-studio.com](https://pvs-studio.com/) | Multilang | Commercial static analyzer (trial available) | 🔴 | — |
| **Codemodder**<br>[GitHub](https://github.com/pixee/codemodder-python) | Java, Python | Auto-fix for security and quality issues | 🟢 | [![updated](https://img.shields.io/github/last-commit/pixee/codemodder-python?style=flat-square&label=)](https://github.com/pixee/codemodder-python) |
| **gosec**<br>[GitHub](https://github.com/securego/gosec) | Go | Inspector for security problems in Go code | 🟢 | [![updated](https://img.shields.io/github/last-commit/securego/gosec?style=flat-square&label=)](https://github.com/securego/gosec) |
| **PHP Vulnerability Hunter**<br>[GitHub](https://github.com/OneSourceCat/phpvulhunter) | PHP | PHP vulnerability finder (legacy) | 🟢 | [![updated](https://img.shields.io/github/last-commit/OneSourceCat/phpvulhunter?style=flat-square&label=)](https://github.com/OneSourceCat/phpvulhunter) |
| **Cobra**<br>[GitHub](https://github.com/wufeifei/cobra) | PHP, Java | Source code security audit (legacy) | 🟢 | [![updated](https://img.shields.io/github/last-commit/wufeifei/cobra?style=flat-square&label=)](https://github.com/wufeifei/cobra) |

---

## 🎯 DAST / IAST

Dynamic and interactive analysis of running applications.

| Tool | Type | Description | License | Updated |
|---|---|---|---|---|
| **OWASP ZAP**<br>[GitHub](https://github.com/zaproxy/zaproxy) | DAST | Free web proxy and automated scanner from OWASP | 🟢 | [![updated](https://img.shields.io/github/last-commit/zaproxy/zaproxy?style=flat-square&label=)](https://github.com/zaproxy/zaproxy) |
| **Nuclei**<br>[GitHub](https://github.com/projectdiscovery/nuclei) | DAST | Fast YAML-template scanner for CVE / misconfig (HTTP, DNS, TCP…) | 🟢 | [![updated](https://img.shields.io/github/last-commit/projectdiscovery/nuclei?style=flat-square&label=)](https://github.com/projectdiscovery/nuclei) |
| **Nikto**<br>[GitHub](https://github.com/sullo/nikto) | DAST | Classic web scanner for dangerous files and misconfigurations | 🟢 | [![updated](https://img.shields.io/github/last-commit/sullo/nikto?style=flat-square&label=)](https://github.com/sullo/nikto) |
| **Wapiti**<br>[GitHub](https://github.com/wapiti-scanner/wapiti) | DAST | Black-box web scanner (XSS, SQLi, and more) | 🟢 | [![updated](https://img.shields.io/github/last-commit/wapiti-scanner/wapiti?style=flat-square&label=)](https://github.com/wapiti-scanner/wapiti) |
| **w3af**<br>[GitHub](https://github.com/andresriancho/w3af) | DAST | Web Application Attack and Audit Framework | 🟢 | [![updated](https://img.shields.io/github/last-commit/andresriancho/w3af?style=flat-square&label=)](https://github.com/andresriancho/w3af) |
| **Dalfox**<br>[GitHub](https://github.com/hahwul/dalfox) | XSS | Parameter analysis and XSS scanning / exploitation helper | 🟢 | [![updated](https://img.shields.io/github/last-commit/hahwul/dalfox?style=flat-square&label=)](https://github.com/hahwul/dalfox) |
| **Commix**<br>[GitHub](https://github.com/commixproject/commix) | Command Injection | Automated OS command injection detection and exploitation | 🟢 | [![updated](https://img.shields.io/github/last-commit/commixproject/commix?style=flat-square&label=)](https://github.com/commixproject/commix) |
| **jwt_tool**<br>[GitHub](https://github.com/ticarpi/jwt_tool) | API / Auth | Toolkit for testing, forging, and attacking JWTs | 🟢 | [![updated](https://img.shields.io/github/last-commit/ticarpi/jwt_tool?style=flat-square&label=)](https://github.com/ticarpi/jwt_tool) |
| **Snyk**<br>[GitHub](https://github.com/snyk/cli) | DAST / SCA | Scan code, dependencies, containers, and IaC | 🟡 | [![updated](https://img.shields.io/github/last-commit/snyk/cli?style=flat-square&label=)](https://github.com/snyk/cli) |
| **SonarQube**<br>[GitHub](https://github.com/SonarSource/sonarqube) | SAST / Quality | Code quality + security hotspots | 🟡 | [![updated](https://img.shields.io/github/last-commit/SonarSource/sonarqube?style=flat-square&label=)](https://github.com/SonarSource/sonarqube) |
| **Contrast Security**<br>[contrastsecurity.com](https://www.contrastsecurity.com/) | IAST | Agent-based interactive analysis at runtime | 🔴 | — |
| **PT Application Inspector**<br>[ptsecurity.com](https://www.ptsecurity.com/ww-en/products/ai/) | SAST/DAST | Commercial application analyzer (Positive Technologies) | 🔴 | — |
| **CloudSploit**<br>[GitHub](https://github.com/aquasecurity/cloudsploit) | Cloud | Misconfiguration checks for AWS / Azure / GCP / Oracle | 🟢 | [![updated](https://img.shields.io/github/last-commit/aquasecurity/cloudsploit?style=flat-square&label=)](https://github.com/aquasecurity/cloudsploit) |
| **Mend (WhiteSource)**<br>[mend.io](https://www.mend.io/) | SCA / AppSec | Commercial open-source risk platform | 🔴 | — |

---

## 📦 SCA / IaC

Dependency and infrastructure-as-code analysis.

| Tool | Focus | Description | License | Updated |
|---|---|---|---|---|
| **Trivy**<br>[GitHub](https://github.com/aquasecurity/trivy) | SCA + IaC + Containers | All-in-one: deps, images, IaC, secrets | 🟢 | [![updated](https://img.shields.io/github/last-commit/aquasecurity/trivy?style=flat-square&label=)](https://github.com/aquasecurity/trivy) |
| **Grype**<br>[GitHub](https://github.com/anchore/grype) | SCA / Containers | Vulnerability scanner for images and filesystems | 🟢 | [![updated](https://img.shields.io/github/last-commit/anchore/grype?style=flat-square&label=)](https://github.com/anchore/grype) |
| **OSV-Scanner**<br>[GitHub](https://github.com/google/osv-scanner) | SCA | Scanner powered by [OSV.dev](https://osv.dev) (Google) | 🟢 | [![updated](https://img.shields.io/github/last-commit/google/osv-scanner?style=flat-square&label=)](https://github.com/google/osv-scanner) |
| **Dependency-Track**<br>[GitHub](https://github.com/DependencyTrack/dependency-track) | SCA Platform | Continuous analysis platform for SBOM / dependencies | 🟢 | [![updated](https://img.shields.io/github/last-commit/DependencyTrack/dependency-track?style=flat-square&label=)](https://github.com/DependencyTrack/dependency-track) |
| **OWASP Dependency-Check**<br>[GitHub](https://github.com/jeremylong/DependencyCheck) | SCA | Match dependencies against known CVE | 🟢 | [![updated](https://img.shields.io/github/last-commit/jeremylong/DependencyCheck?style=flat-square&label=)](https://github.com/jeremylong/DependencyCheck) |
| **Checkov**<br>[GitHub](https://github.com/bridgecrewio/checkov) | IaC | Policy-as-code for Terraform, K8s, CloudFormation, Docker | 🟢 | [![updated](https://img.shields.io/github/last-commit/bridgecrewio/checkov?style=flat-square&label=)](https://github.com/bridgecrewio/checkov) |
| **KICS**<br>[GitHub](https://github.com/Checkmarx/kics) | IaC | Keeping Infrastructure as Code Secure — multi-IaC scanner | 🟢 | [![updated](https://img.shields.io/github/last-commit/Checkmarx/kics?style=flat-square&label=)](https://github.com/Checkmarx/kics) |
| **tfsec**<br>[GitHub](https://github.com/aquasecurity/tfsec) | IaC | Terraform security scanner (Trivy lineage) | 🟢 | [![updated](https://img.shields.io/github/last-commit/aquasecurity/tfsec?style=flat-square&label=)](https://github.com/aquasecurity/tfsec) |
| **Terrascan**<br>[GitHub](https://github.com/tenable/terrascan) | IaC | Compliance / security scanning for IaC | 🟢 | [![updated](https://img.shields.io/github/last-commit/tenable/terrascan?style=flat-square&label=)](https://github.com/tenable/terrascan) |

---

## 📋 SBOM

Software Bill of Materials generation.

| Tool | Format | Description | License | Updated |
|---|---|---|---|---|
| **Syft**<br>[GitHub](https://github.com/anchore/syft) | SPDX, CycloneDX | Generate SBOM from images, directories, and manifests | 🟢 | [![updated](https://img.shields.io/github/last-commit/anchore/syft?style=flat-square&label=)](https://github.com/anchore/syft) |
| **cdxgen**<br>[GitHub](https://github.com/CycloneDX/cdxgen) | CycloneDX | Universal CycloneDX SBOM generator | 🟢 | [![updated](https://img.shields.io/github/last-commit/CycloneDX/cdxgen?style=flat-square&label=)](https://github.com/CycloneDX/cdxgen) |
| **Trivy**<br>[GitHub](https://github.com/aquasecurity/trivy) | SPDX, CycloneDX | SBOM as part of scanning | 🟢 | [![updated](https://img.shields.io/github/last-commit/aquasecurity/trivy?style=flat-square&label=)](https://github.com/aquasecurity/trivy) |

---

## 🔐 Secret Detection

| Tool | Description | License | Updated |
|---|---|---|---|
| **Gitleaks**<br>[GitHub](https://github.com/gitleaks/gitleaks) | Fast secret detection in git history and filesystem | 🟢 | [![updated](https://img.shields.io/github/last-commit/gitleaks/gitleaks?style=flat-square&label=)](https://github.com/gitleaks/gitleaks) |
| **TruffleHog**<br>[GitHub](https://github.com/trufflesecurity/trufflehog) | Secret detection with live verification (API keys, etc.) | 🟢 | [![updated](https://img.shields.io/github/last-commit/trufflesecurity/trufflehog?style=flat-square&label=)](https://github.com/trufflesecurity/trufflehog) |
| **git-secret**<br>[GitHub](https://github.com/sobolevn/git-secret) | Encrypt secrets in git via GPG | 🟢 | [![updated](https://img.shields.io/github/last-commit/sobolevn/git-secret?style=flat-square&label=)](https://github.com/sobolevn/git-secret) |
| **detect-secrets**<br>[GitHub](https://github.com/Yelp/detect-secrets) | Enterprise-friendly baseline secret scanner (Yelp) | 🟢 | [![updated](https://img.shields.io/github/last-commit/Yelp/detect-secrets?style=flat-square&label=)](https://github.com/Yelp/detect-secrets) |

---

## 🛰️ Scanners

Network, web, and general-purpose vulnerability scanners.

| Tool | Type | Description | License | Updated |
|---|---|---|---|---|
| **Nmap**<br>[GitHub](https://github.com/nmap/nmap) | Network | Reference network discovery / port scanner | 🟢 | [![updated](https://img.shields.io/github/last-commit/nmap/nmap?style=flat-square&label=)](https://github.com/nmap/nmap) |
| **Masscan**<br>[GitHub](https://github.com/robertdavidgraham/masscan) | Network | Asynchronous ultra-fast port scanner | 🟢 | [![updated](https://img.shields.io/github/last-commit/robertdavidgraham/masscan?style=flat-square&label=)](https://github.com/robertdavidgraham/masscan) |
| **RustScan**<br>[GitHub](https://github.com/RustScan/RustScan) | Network | Extremely fast port scanner that pipes into Nmap | 🟢 | [![updated](https://img.shields.io/github/last-commit/RustScan/RustScan?style=flat-square&label=)](https://github.com/RustScan/RustScan) |
| **OpenVAS / Greenbone**<br>[GitHub](https://github.com/greenbone/openvas-scanner) | Network VA | Full vulnerability assessment stack | 🟢 | [![updated](https://img.shields.io/github/last-commit/greenbone/openvas-scanner?style=flat-square&label=)](https://github.com/greenbone/openvas-scanner) |
| **Nessus**<br>[tenable.com](https://www.tenable.com/products/nessus) | Network VA | Commercial VA scanner by Tenable | 🔴 | — |
| **InsightVM (Nexpose)**<br>[rapid7.com](https://www.rapid7.com/products/insightvm/) | Network VA | Vulnerability management by Rapid7 | 🔴 | — |
| **Tsunami**<br>[GitHub](https://github.com/google/tsunami-security-scanner) | Network | Modular high-severity scanner by Google | 🟢 | [![updated](https://img.shields.io/github/last-commit/google/tsunami-security-scanner?style=flat-square&label=)](https://github.com/google/tsunami-security-scanner) |
| **testssl.sh**<br>[GitHub](https://github.com/drwetter/testssl.sh) | TLS / SSL | CLI checker for TLS/SSL ciphers, protocols, and vulns | 🟢 | [![updated](https://img.shields.io/github/last-commit/drwetter/testssl.sh?style=flat-square&label=)](https://github.com/drwetter/testssl.sh) |
| **SSLyze**<br>[GitHub](https://github.com/nabla-c0d3/sslyze) | TLS / SSL | Fast and powerful SSL/TLS scanning library | 🟢 | [![updated](https://img.shields.io/github/last-commit/nabla-c0d3/sslyze?style=flat-square&label=)](https://github.com/nabla-c0d3/sslyze) |
| **Sqlmap**<br>[GitHub](https://github.com/sqlmapproject/sqlmap) | Web / SQLi | Automated SQL Injection detection and exploitation | 🟢 | [![updated](https://img.shields.io/github/last-commit/sqlmapproject/sqlmap?style=flat-square&label=)](https://github.com/sqlmapproject/sqlmap) |
| **NoSQLMap**<br>[GitHub](https://github.com/codingo/NoSQLMap) | NoSQL | Audit and exploit NoSQL injection | 🟢 | [![updated](https://img.shields.io/github/last-commit/codingo/NoSQLMap?style=flat-square&label=)](https://github.com/codingo/NoSQLMap) |
| **WhatWeb**<br>[GitHub](https://github.com/urbanadventurer/WhatWeb) | Fingerprint | Identify CMS, frameworks, and site tech | 🟢 | [![updated](https://img.shields.io/github/last-commit/urbanadventurer/WhatWeb?style=flat-square&label=)](https://github.com/urbanadventurer/WhatWeb) |
| **Wappalyzer**<br>[wappalyzer.com](https://www.wappalyzer.com/) | Fingerprint | Identify technologies used on websites | 🟡 | — |
| **wappalyzergo**<br>[GitHub](https://github.com/projectdiscovery/wappalyzergo) | Fingerprint | Go port of Wappalyzer fingerprinting for CLI / pipelines | 🟢 | [![updated](https://img.shields.io/github/last-commit/projectdiscovery/wappalyzergo?style=flat-square&label=)](https://github.com/projectdiscovery/wappalyzergo) |
| **Xray**<br>[GitHub](https://github.com/chaitin/xray) | Web | Passive / active web scanner (Chaitin) | 🟢 | [![updated](https://img.shields.io/github/last-commit/chaitin/xray?style=flat-square&label=)](https://github.com/chaitin/xray) |
| **Osmedeus**<br>[GitHub](https://github.com/j3ssie/Osmedeus) | Orchestration | Workflow engine for automated recon / scan | 🟢 | [![updated](https://img.shields.io/github/last-commit/j3ssie/Osmedeus?style=flat-square&label=)](https://github.com/j3ssie/Osmedeus) |
| **OneForAll**<br>[GitHub](https://github.com/shmilylty/OneForAll) | Subdomain / Recon | Powerful subdomain collection | 🟢 | [![updated](https://img.shields.io/github/last-commit/shmilylty/OneForAll?style=flat-square&label=)](https://github.com/shmilylty/OneForAll) |
| **Sn1per**<br>[GitHub](https://github.com/1N3/Sn1per) | Pentest Automation | Automated pentest framework | 🟡 | [![updated](https://img.shields.io/github/last-commit/1N3/Sn1per?style=flat-square&label=)](https://github.com/1N3/Sn1per) |
| **AutoRecon**<br>[GitHub](https://github.com/Tib3rius/AutoRecon) | Recon | Multi-threaded network recon for CTF / pentest | 🟢 | [![updated](https://img.shields.io/github/last-commit/Tib3rius/AutoRecon?style=flat-square&label=)](https://github.com/Tib3rius/AutoRecon) |
| **Legion**<br>[GitHub](https://github.com/GoVanguard/legion) | Network GUI | GUI wrapper around Nmap and other scanners | 🟢 | [![updated](https://img.shields.io/github/last-commit/GoVanguard/legion?style=flat-square&label=)](https://github.com/GoVanguard/legion) |
| **Raccoon**<br>[GitHub](https://github.com/evyatarmeged/Raccoon) | Recon | Asynchronous recon / offensive reconnaissance | 🟢 | [![updated](https://img.shields.io/github/last-commit/evyatarmeged/Raccoon?style=flat-square&label=)](https://github.com/evyatarmeged/Raccoon) |
| **Scanless**<br>[GitHub](https://github.com/vesche/scanless) | Network | Port scan via public online scanners (opsec) | 🟢 | [![updated](https://img.shields.io/github/last-commit/vesche/scanless?style=flat-square&label=)](https://github.com/vesche/scanless) |
| **Golismero**<br>[GitHub](https://github.com/golismero/golismero) | Framework | Security framework with plugins | 🟢 | [![updated](https://img.shields.io/github/last-commit/golismero/golismero?style=flat-square&label=)](https://github.com/golismero/golismero) |
| **Arachni**<br>[GitHub](https://github.com/Arachni/arachni) | Web | Modular web scanner (maintenance mode) | 🟢 | [![updated](https://img.shields.io/github/last-commit/Arachni/arachni?style=flat-square&label=)](https://github.com/Arachni/arachni) |
| **Acunetix**<br>[acunetix.com](https://www.acunetix.com/) | Web | Commercial DAST | 🔴 | — |
| **Invicti (Netsparker)**<br>[invicti.com](https://www.invicti.com/) | Web | Commercial DAST with proof-based scanning | 🔴 | — |
| **ScanOval**<br>[bdu.fstec.ru](https://bdu.fstec.ru/site/scanoval) | OVAL / BDU | OVAL-based vulnerability checks (FSTEC BDU) | 🌐 | — |
| **Puma Scan**<br>[GitHub](https://github.com/pumasecurity/puma-scan) | .NET SAST | Roslyn analyzer for .NET security | 🟡 | [![updated](https://img.shields.io/github/last-commit/pumasecurity/puma-scan?style=flat-square&label=)](https://github.com/pumasecurity/puma-scan) |

---

## 🧭 Recon & Enumeration

| Tool | Description | License | Updated |
|---|---|---|---|
| **Amass**<br>[GitHub](https://github.com/owasp-amass/amass) | OWASP: deep subdomain enumeration and attack-surface mapping | 🟢 | [![updated](https://img.shields.io/github/last-commit/owasp-amass/amass?style=flat-square&label=)](https://github.com/owasp-amass/amass) |
| **subfinder**<br>[GitHub](https://github.com/projectdiscovery/subfinder) | Passive subdomain discovery (ProjectDiscovery) | 🟢 | [![updated](https://img.shields.io/github/last-commit/projectdiscovery/subfinder?style=flat-square&label=)](https://github.com/projectdiscovery/subfinder) |
| **httpx**<br>[GitHub](https://github.com/projectdiscovery/httpx) | Fast HTTP probing / tech detection | 🟢 | [![updated](https://img.shields.io/github/last-commit/projectdiscovery/httpx?style=flat-square&label=)](https://github.com/projectdiscovery/httpx) |
| **dnsx**<br>[GitHub](https://github.com/projectdiscovery/dnsx) | DNS toolkit for resolve and enumeration | 🟢 | [![updated](https://img.shields.io/github/last-commit/projectdiscovery/dnsx?style=flat-square&label=)](https://github.com/projectdiscovery/dnsx) |
| **Chaos**<br>[GitHub](https://github.com/projectdiscovery/chaos-client) | ProjectDiscovery DNS dataset client for passive recon | 🟢 | [![updated](https://img.shields.io/github/last-commit/projectdiscovery/chaos-client?style=flat-square&label=)](https://github.com/projectdiscovery/chaos-client) |
| **ffuf**<br>[GitHub](https://github.com/ffuf/ffuf) | Fast web fuzzer (dirs, vhosts, params) | 🟢 | [![updated](https://img.shields.io/github/last-commit/ffuf/ffuf?style=flat-square&label=)](https://github.com/ffuf/ffuf) |
| **gobuster**<br>[GitHub](https://github.com/OJ/gobuster) | Directory, DNS, and vhost brute-forcing | 🟢 | [![updated](https://img.shields.io/github/last-commit/OJ/gobuster?style=flat-square&label=)](https://github.com/OJ/gobuster) |
| **feroxbuster**<br>[GitHub](https://github.com/epi052/feroxbuster) | Fast, recursive content discovery written in Rust | 🟢 | [![updated](https://img.shields.io/github/last-commit/epi052/feroxbuster?style=flat-square&label=)](https://github.com/epi052/feroxbuster) |
| **Arjun**<br>[GitHub](https://github.com/s0md3v/Arjun) | HTTP parameter discovery suite | 🟢 | [![updated](https://img.shields.io/github/last-commit/s0md3v/Arjun?style=flat-square&label=)](https://github.com/s0md3v/Arjun) |
| **knock**<br>[GitHub](https://github.com/guelfoweb/knock) | Subdomain enumeration via wordlist + DNS | 🟢 | [![updated](https://img.shields.io/github/last-commit/guelfoweb/knock?style=flat-square&label=)](https://github.com/guelfoweb/knock) |
| **subDomainsBrute**<br>[GitHub](https://github.com/lijiejie/subDomainsBrute) | Multi-threaded subdomain brute-force | 🟢 | [![updated](https://img.shields.io/github/last-commit/lijiejie/subDomainsBrute?style=flat-square&label=)](https://github.com/lijiejie/subDomainsBrute) |
| **SubDomain3**<br>[GitHub](https://github.com/yanxiu0614/subdomain3) | High-speed subdomain scanner | 🟢 | [![updated](https://img.shields.io/github/last-commit/yanxiu0614/subdomain3?style=flat-square&label=)](https://github.com/yanxiu0614/subdomain3) |
| **domained**<br>[GitHub](https://github.com/TypeError/domained) | Wrapper around multiple subdomain tools | 🟢 | [![updated](https://img.shields.io/github/last-commit/TypeError/domained?style=flat-square&label=)](https://github.com/TypeError/domained) |
| **katana**<br>[GitHub](https://github.com/projectdiscovery/katana) | Next-gen crawling / spidering | 🟢 | [![updated](https://img.shields.io/github/last-commit/projectdiscovery/katana?style=flat-square&label=)](https://github.com/projectdiscovery/katana) |
| **gau**<br>[GitHub](https://github.com/lc/gau) | Fetch known URLs from public sources | 🟢 | [![updated](https://img.shields.io/github/last-commit/lc/gau?style=flat-square&label=)](https://github.com/lc/gau) |
| **waybackurls**<br>[GitHub](https://github.com/tomnomnom/waybackurls) | Fetch URLs from the Wayback Machine for a domain | 🟢 | [![updated](https://img.shields.io/github/last-commit/tomnomnom/waybackurls?style=flat-square&label=)](https://github.com/tomnomnom/waybackurls) |
| **hakrawler**<br>[GitHub](https://github.com/hakluke/hakrawler) | Simple, fast web crawler for gathering URLs / endpoints | 🟢 | [![updated](https://img.shields.io/github/last-commit/hakluke/hakrawler?style=flat-square&label=)](https://github.com/hakluke/hakrawler) |

---

## 🏢 Active Directory & Internal

Identity attack-path mapping and Windows / AD assessment tooling.

| Tool | Description | License | Updated |
|---|---|---|---|
| **BloodHound**<br>[GitHub](https://github.com/SpecterOps/BloodHound) | Graph analysis of AD / Entra ID attack paths | 🟡 | [![updated](https://img.shields.io/github/last-commit/SpecterOps/BloodHound?style=flat-square&label=)](https://github.com/SpecterOps/BloodHound) |
| **SharpHound**<br>[GitHub](https://github.com/SpecterOps/SharpHound) | BloodHound data collector for Active Directory | 🟢 | [![updated](https://img.shields.io/github/last-commit/SpecterOps/SharpHound?style=flat-square&label=)](https://github.com/SpecterOps/SharpHound) |
| **Impacket**<br>[GitHub](https://github.com/fortra/impacket) | Python collection of Windows network protocol tools | 🟢 | [![updated](https://img.shields.io/github/last-commit/fortra/impacket?style=flat-square&label=)](https://github.com/fortra/impacket) |
| **NetExec**<br>[GitHub](https://github.com/Pennyw0rth/NetExec) | Network authentication / assessment (CrackMapExec successor) | 🟢 | [![updated](https://img.shields.io/github/last-commit/Pennyw0rth/NetExec?style=flat-square&label=)](https://github.com/Pennyw0rth/NetExec) |
| **Responder**<br>[GitHub](https://github.com/lgandx/Responder) | LLMNR / NBT-NS / mDNS poisoner for credential capture | 🟢 | [![updated](https://img.shields.io/github/last-commit/lgandx/Responder?style=flat-square&label=)](https://github.com/lgandx/Responder) |
| **Certipy**<br>[GitHub](https://github.com/ly4k/Certipy) | Active Directory Certificate Services enumeration & abuse | 🟢 | [![updated](https://img.shields.io/github/last-commit/ly4k/Certipy?style=flat-square&label=)](https://github.com/ly4k/Certipy) |
| **Rubeus**<br>[GitHub](https://github.com/GhostPack/Rubeus) | Kerberos abuse toolkit for offensive AD ops | 🟢 | [![updated](https://img.shields.io/github/last-commit/GhostPack/Rubeus?style=flat-square&label=)](https://github.com/GhostPack/Rubeus) |
| **PowerView**<br>[GitHub](https://github.com/PowerShellMafia/PowerSploit) | PowerShell AD situational awareness (PowerSploit) | 🟢 | [![updated](https://img.shields.io/github/last-commit/PowerShellMafia/PowerSploit?style=flat-square&label=)](https://github.com/PowerShellMafia/PowerSploit) |

---

## 🔑 Password Cracking

| Tool | Description | License | Updated |
|---|---|---|---|
| **Hashcat**<br>[GitHub](https://github.com/hashcat/hashcat) | Advanced GPU password recovery | 🟢 | [![updated](https://img.shields.io/github/last-commit/hashcat/hashcat?style=flat-square&label=)](https://github.com/hashcat/hashcat) |
| **John the Ripper**<br>[GitHub](https://github.com/openwall/john) | Fast password cracker (CPU + many formats) | 🟢 | [![updated](https://img.shields.io/github/last-commit/openwall/john?style=flat-square&label=)](https://github.com/openwall/john) |
| **Hydra**<br>[GitHub](https://github.com/vanhauser-thc/thc-hydra) | Parallel online brute-force for network services | 🟢 | [![updated](https://img.shields.io/github/last-commit/vanhauser-thc/thc-hydra?style=flat-square&label=)](https://github.com/vanhauser-thc/thc-hydra) |
| **Medusa**<br>[GitHub](https://github.com/jmk-foofus/medusa) | Speedy, parallel, modular login brute-forcer | 🟢 | [![updated](https://img.shields.io/github/last-commit/jmk-foofus/medusa?style=flat-square&label=)](https://github.com/jmk-foofus/medusa) |

---

## ☁️ Cloud & Container Security

CSPM, CNAPP-adjacent OSS, and Kubernetes hardening.

| Tool | Focus | Description | License | Updated |
|---|---|---|---|---|
| **Prowler**<br>[GitHub](https://github.com/prowler-cloud/prowler) | CSPM | Multi-cloud security assessment (AWS, Azure, GCP, …) | 🟢 | [![updated](https://img.shields.io/github/last-commit/prowler-cloud/prowler?style=flat-square&label=)](https://github.com/prowler-cloud/prowler) |
| **ScoutSuite**<br>[GitHub](https://github.com/nccgroup/ScoutSuite) | CSPM | Multi-cloud security auditing tool | 🟢 | [![updated](https://img.shields.io/github/last-commit/nccgroup/ScoutSuite?style=flat-square&label=)](https://github.com/nccgroup/ScoutSuite) |
| **CloudMapper**<br>[GitHub](https://github.com/duo-labs/cloudmapper) | AWS | Network visualization and inventory for AWS accounts | 🟢 | [![updated](https://img.shields.io/github/last-commit/duo-labs/cloudmapper?style=flat-square&label=)](https://github.com/duo-labs/cloudmapper) |
| **kube-bench**<br>[GitHub](https://github.com/aquasecurity/kube-bench) | Kubernetes | CIS Kubernetes Benchmark checks | 🟢 | [![updated](https://img.shields.io/github/last-commit/aquasecurity/kube-bench?style=flat-square&label=)](https://github.com/aquasecurity/kube-bench) |
| **kube-hunter**<br>[GitHub](https://github.com/aquasecurity/kube-hunter) | Kubernetes | Hunt for security weaknesses in K8s clusters | 🟢 | [![updated](https://img.shields.io/github/last-commit/aquasecurity/kube-hunter?style=flat-square&label=)](https://github.com/aquasecurity/kube-hunter) |
| **Falco**<br>[GitHub](https://github.com/falcosecurity/falco) | Runtime | Cloud-native runtime security / threat detection | 🟢 | [![updated](https://img.shields.io/github/last-commit/falcosecurity/falco?style=flat-square&label=)](https://github.com/falcosecurity/falco) |
| **Trivy**<br>[GitHub](https://github.com/aquasecurity/trivy) | Containers / IaC | Image, filesystem, and IaC vulnerability scanner | 🟢 | [![updated](https://img.shields.io/github/last-commit/aquasecurity/trivy?style=flat-square&label=)](https://github.com/aquasecurity/trivy) |
| **Docker Bench**<br>[GitHub](https://github.com/docker/docker-bench-security) | Containers | CIS Docker Benchmark script | 🟢 | [![updated](https://img.shields.io/github/last-commit/docker/docker-bench-security?style=flat-square&label=)](https://github.com/docker/docker-bench-security) |
| **Orca Security**<br>[orca.security](https://orca.security/) | CNAPP | Commercial agentless cloud security platform | 🔴 | — |
| **Wiz**<br>[wiz.io](https://www.wiz.io/) | CNAPP | Commercial cloud security platform | 🔴 | — |
| **Prisma Cloud**<br>[paloaltonetworks.com](https://www.paloaltonetworks.com/prisma/cloud) | CNAPP | Commercial CNAPP by Palo Alto Networks | 🔴 | — |

---

## 📡 Network Analysis & IDS

| Tool | Description | License | Updated |
|---|---|---|---|
| **Wireshark**<br>[GitHub](https://github.com/wireshark/wireshark) | Network protocol analyzer | 🟢 | [![updated](https://img.shields.io/github/last-commit/wireshark/wireshark?style=flat-square&label=)](https://github.com/wireshark/wireshark) |
| **tcpdump**<br>[GitHub](https://github.com/the-tcpdump-group/tcpdump) | Classic command-line packet analyzer | 🟢 | [![updated](https://img.shields.io/github/last-commit/the-tcpdump-group/tcpdump?style=flat-square&label=)](https://github.com/the-tcpdump-group/tcpdump) |
| **Zeek**<br>[GitHub](https://github.com/zeek/zeek) | Network security monitoring framework (formerly Bro) | 🟢 | [![updated](https://img.shields.io/github/last-commit/zeek/zeek?style=flat-square&label=)](https://github.com/zeek/zeek) |
| **Suricata**<br>[GitHub](https://github.com/OISF/suricata) | High-performance IDS / IPS / NSM engine | 🟢 | [![updated](https://img.shields.io/github/last-commit/OISF/suricata?style=flat-square&label=)](https://github.com/OISF/suricata) |
| **Snort**<br>[GitHub](https://github.com/snort3/snort3) | Network intrusion detection and prevention | 🟢 | [![updated](https://img.shields.io/github/last-commit/snort3/snort3?style=flat-square&label=)](https://github.com/snort3/snort3) |
| **Wazuh**<br>[GitHub](https://github.com/wazuh/wazuh) | Open-source XDR / SIEM platform | 🟢 | [![updated](https://img.shields.io/github/last-commit/wazuh/wazuh?style=flat-square&label=)](https://github.com/wazuh/wazuh) |
| **OSSEC**<br>[GitHub](https://github.com/ossec/ossec-hids) | Host-based intrusion detection system | 🟢 | [![updated](https://img.shields.io/github/last-commit/ossec/ossec-hids?style=flat-square&label=)](https://github.com/ossec/ossec-hids) |
| **ModSecurity**<br>[GitHub](https://github.com/owasp-modsecurity/ModSecurity) | Open-source web application firewall engine | 🟢 | [![updated](https://img.shields.io/github/last-commit/owasp-modsecurity/ModSecurity?style=flat-square&label=)](https://github.com/owasp-modsecurity/ModSecurity) |

---

## 🔬 Forensics & Incident Response

| Tool | Description | License | Updated |
|---|---|---|---|
| **Volatility 3**<br>[GitHub](https://github.com/volatilityfoundation/volatility3) | Advanced memory forensics framework | 🟢 | [![updated](https://img.shields.io/github/last-commit/volatilityfoundation/volatility3?style=flat-square&label=)](https://github.com/volatilityfoundation/volatility3) |
| **Velociraptor**<br>[GitHub](https://github.com/Velocidex/velociraptor) | Endpoint visibility and digital forensics / IR | 🟢 | [![updated](https://img.shields.io/github/last-commit/Velocidex/velociraptor?style=flat-square&label=)](https://github.com/Velocidex/velociraptor) |
| **Autopsy**<br>[GitHub](https://github.com/sleuthkit/autopsy) | Digital forensics platform (GUI on The Sleuth Kit) | 🟢 | [![updated](https://img.shields.io/github/last-commit/sleuthkit/autopsy?style=flat-square&label=)](https://github.com/sleuthkit/autopsy) |
| **The Sleuth Kit**<br>[GitHub](https://github.com/sleuthkit/sleuthkit) | Library and tools for disk image forensics | 🟢 | [![updated](https://img.shields.io/github/last-commit/sleuthkit/sleuthkit?style=flat-square&label=)](https://github.com/sleuthkit/sleuthkit) |
| **Plaso**<br>[GitHub](https://github.com/log2timeline/plaso) | Super timeline engine for digital forensics | 🟢 | [![updated](https://img.shields.io/github/last-commit/log2timeline/plaso?style=flat-square&label=)](https://github.com/log2timeline/plaso) |
| **osquery**<br>[GitHub](https://github.com/osquery/osquery) | SQL-powered operating system instrumentation | 🟢 | [![updated](https://img.shields.io/github/last-commit/osquery/osquery?style=flat-square&label=)](https://github.com/osquery/osquery) |
| **TheHive**<br>[GitHub](https://github.com/TheHive-Project/TheHive) | Scalable Security Incident Response Platform | 🟢 | [![updated](https://img.shields.io/github/last-commit/TheHive-Project/TheHive?style=flat-square&label=)](https://github.com/TheHive-Project/TheHive) |
| **Cortex**<br>[GitHub](https://github.com/TheHive-Project/Cortex) | Observable analysis & active response engine | 🟢 | [![updated](https://img.shields.io/github/last-commit/TheHive-Project/Cortex?style=flat-square&label=)](https://github.com/TheHive-Project/Cortex) |

---

## 🧠 Threat Intelligence

| Tool | Description | License | Updated |
|---|---|---|---|
| **MISP**<br>[GitHub](https://github.com/MISP/MISP) | Open-source threat intelligence sharing platform | 🟢 | [![updated](https://img.shields.io/github/last-commit/MISP/MISP?style=flat-square&label=)](https://github.com/MISP/MISP) |
| **OpenCTI**<br>[GitHub](https://github.com/OpenCTI-Platform/opencti) | Open Cyber Threat Intelligence platform | 🟢 | [![updated](https://img.shields.io/github/last-commit/OpenCTI-Platform/opencti?style=flat-square&label=)](https://github.com/OpenCTI-Platform/opencti) |
| **OpenTAXII**<br>[GitHub](https://github.com/eclecticiq/OpenTAXII) | TAXII server implementation for CTI exchange | 🟢 | [![updated](https://img.shields.io/github/last-commit/eclecticiq/OpenTAXII?style=flat-square&label=)](https://github.com/eclecticiq/OpenTAXII) |
| **YARA**<br>[GitHub](https://github.com/VirusTotal/yara) | Pattern-matching for malware researchers | 🟢 | [![updated](https://img.shields.io/github/last-commit/VirusTotal/yara?style=flat-square&label=)](https://github.com/VirusTotal/yara) |
| **Sigma**<br>[GitHub](https://github.com/SigmaHQ/sigma) | Generic signature format for SIEM systems | 🟢 | [![updated](https://img.shields.io/github/last-commit/SigmaHQ/sigma?style=flat-square&label=)](https://github.com/SigmaHQ/sigma) |
| **AbuseIPDB**<br>[abuseipdb.com](https://www.abuseipdb.com/) | IP abuse reporting and reputation database | ☁️ | — |
| **VirusTotal**<br>[virustotal.com](https://www.virustotal.com/) | Multi-engine file / URL malware analysis | ☁️ | — |
| **AlienVault OTX**<br>[otx.alienvault.com](https://otx.alienvault.com/) | Open Threat Exchange community intel | ☁️ | — |
| **Hudson Rock**<br>[hudsonrock.com](https://www.hudsonrock.com/) | Infostealer / cybercrime intelligence | ☁️ | — |

---

## 🕳️ Breach & Leak Lookup

Credential and leak monitoring / digital risk protection lookups.

| Tool | Description | License | Updated |
|---|---|---|---|
| **Have I Been Pwned**<br>[haveibeenpwned.com](https://haveibeenpwned.com/) | Check if emails / passwords appear in known breaches | ☁️ | — |
| **DeHashed**<br>[dehashed.com](https://dehashed.com/) | Breach data search for credentials, WHOIS, and monitoring | ☁️ | — |
| **Intelligence X**<br>[intelx.io](https://intelx.io/) | Search leaked and historical data | ☁️ | — |
| **LeakIX**<br>[leakix.net](https://leakix.net/) | Search engine for publicly exposed services and leaks | ☁️ | — |
| **Hudson Rock**<br>[hudsonrock.com](https://cavalier.hudsonrock.com/) | Free / paid infostealer compromise checks | ☁️ | — |

---

## 🧬 Binary Analysis & Reverse Engineering

| Tool | Description | License | Updated |
|---|---|---|---|
| **Ghidra**<br>[GitHub](https://github.com/NationalSecurityAgency/ghidra) | NSA open-source software reverse engineering suite | 🟢 | [![updated](https://img.shields.io/github/last-commit/NationalSecurityAgency/ghidra?style=flat-square&label=)](https://github.com/NationalSecurityAgency/ghidra) |
| **radare2**<br>[GitHub](https://github.com/radareorg/radare2) | UNIX-like reverse engineering framework | 🟢 | [![updated](https://img.shields.io/github/last-commit/radareorg/radare2?style=flat-square&label=)](https://github.com/radareorg/radare2) |
| **Cutter**<br>[GitHub](https://github.com/rizinorg/cutter) | Free GUI for Rizin / reverse engineering | 🟢 | [![updated](https://img.shields.io/github/last-commit/rizinorg/cutter?style=flat-square&label=)](https://github.com/rizinorg/cutter) |
| **Binary Ninja**<br>[binary.ninja](https://binary.ninja/) | Commercial reverse engineering platform | 🔴 | — |
| **IDA**<br>[hex-rays.com](https://hex-rays.com/ida-pro/) | Commercial industry-standard disassembler / debugger | 🔴 | — |
| **Binwalk**<br>[GitHub](https://github.com/ReFirmLabs/binwalk) | Firmware analysis and extraction tool | 🟢 | [![updated](https://img.shields.io/github/last-commit/ReFirmLabs/binwalk?style=flat-square&label=)](https://github.com/ReFirmLabs/binwalk) |
| **PE-bear**<br>[GitHub](https://github.com/hasherezade/pe-bear) | PE file reversing toolkit | 🟢 | [![updated](https://img.shields.io/github/last-commit/hasherezade/pe-bear?style=flat-square&label=)](https://github.com/hasherezade/pe-bear) |
| **Detect It Easy**<br>[GitHub](https://github.com/horsicq/Detect-It-Easy) | Packer / compiler / crypto detection for binaries | 🟢 | [![updated](https://img.shields.io/github/last-commit/horsicq/Detect-It-Easy?style=flat-square&label=)](https://github.com/horsicq/Detect-It-Easy) |

---

## 📚 Wordlists & Payloads

| Tool | Description | License | Updated |
|---|---|---|---|
| **SecLists**<br>[GitHub](https://github.com/danielmiessler/SecLists) | Collection of security wordlists and payloads | 🟢 | [![updated](https://img.shields.io/github/last-commit/danielmiessler/SecLists?style=flat-square&label=)](https://github.com/danielmiessler/SecLists) |
| **PayloadsAllTheThings**<br>[GitHub](https://github.com/swisskyrepo/PayloadsAllTheThings) | Useful payloads and bypasses for Web AppSec | 🟢 | [![updated](https://img.shields.io/github/last-commit/swisskyrepo/PayloadsAllTheThings?style=flat-square&label=)](https://github.com/swisskyrepo/PayloadsAllTheThings) |
| **FuzzDB**<br>[GitHub](https://github.com/fuzzdb-project/fuzzdb) | Attack patterns, discovery dictionaries, and injectables | 🟢 | [![updated](https://img.shields.io/github/last-commit/fuzzdb-project/fuzzdb?style=flat-square&label=)](https://github.com/fuzzdb-project/fuzzdb) |
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
