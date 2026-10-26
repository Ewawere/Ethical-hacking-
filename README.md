# Local Ethical Hacking Lab

A safe, local-only ethical hacking training environment for learning real-world workflow on devices you own and control.

This project is designed to simulate a real security lab while keeping everything inside a controlled environment.

Important:
- Only scan targets on your own lab network
- Never test public systems or networks without explicit authorization
- Use only local vulnerable apps or devices you own
- This is for training and education only

## Run it on your phone

### 1) Install Termux
Install Termux from F-Droid or its official source.

### 2) Install Python and Nmap
```bash
pkg update && pkg upgrade
pkg install git python nmap
```

### 3) Clone the project
```bash
cd $HOME
git clone https://github.com/Ewawere/Ethical-hacking-.git
cd Ethical-hacking-
```

### 4) Start the site locally
```bash
python3 -m http.server 8000
```

Then open in your browser:
```text
http://localhost:8000/app/
```

To install it like an app on Android:
- open the site in Chrome or Edge
- tap the menu button
- choose "Add to Home screen"

### 5) Run the lab tools in Termux
Only on your own local lab network:
```bash
python3 scripts/scan_lab.py 10.0.2.0/24
```

## Features
- Desktop-like interface optimized for mobile
- Installable PWA experience
- Local-only lab controls
- Safe recon and reporting tools
- Realistic learning workflow without public scanning

## Folder overview
- app/ = installable web dashboard
- labs/ = local vulnerable apps
- scripts/ = safe recon and reporting tools
- docs/ = setup and learning path
