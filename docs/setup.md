# Setup guide

This project is a static learning dashboard and documentation site. It is not meant to be used against public networks or unknown systems.

Requirements:
- a computer, phone, or tablet you can use for browsing
- a private local lab or VM
- Python 3
- Docker or a local Linux VM
- optional tools: Nmap, curl, Burp Suite, Wireshark

Recommended local lab setup:
- Use a private home network
- Run local vulnerable apps in Docker or a VM
- Keep everything isolated from the public internet
- Test only machines you own or are explicitly authorized to test

Suggested lab targets:
- DVWA
- Juice Shop
- OWASP WebGoat
- Metasploitable

Typical local workflow:
1. Confirm scope and authorization
2. Identify private target ranges
3. Run Nmap or a local enumeration tool
4. Review exposed ports and services
5. Document findings and remediation steps

Example commands:
```bash
python3 --version
python3 -m http.server 8000
nmap -sV -Pn 10.0.2.0/24
```

For mobile or iPhone use:
- serve the frontend from a local machine or a Vercel deployment
- open the app in Safari or Chrome
- keep all testing inside your private local lab network

This is for ethical, legal, and authorized learning only.
