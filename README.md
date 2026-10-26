# Local Ethical Hacking Lab

A safe, local-only ethical hacking training environment for learning real-world workflow on devices you own and control.

This project is designed to simulate a real security lab while keeping everything inside a controlled environment.

Important:
- Only scan targets on your own lab network
- Never test public systems or networks without explicit authorization
- Use only local vulnerable apps or devices you own
- This is for training and education only

## Features
- Desktop-like UI optimized for mobile
- Local vulnerable apps via Docker
- Safe reconnaissance tooling
- Learning modules for security workflows
- Report generation for practical exercises

## Tech stack
- Python
- Docker
- Nmap
- HTML/CSS/JS
- Local-only lab network

## Quick start
1. Install Docker
2. Install Python 3
3. Install Nmap
4. Start the lab:
   python scripts/lab_manager.py start
5. Open the app in a browser
6. Use the local dashboard to run scans and track exercises

## Lab targets
Use only IP ranges you own, such as:
- 10.0.2.0/24
- 192.168.56.0/24

## Learning flow
1. Set up the lab
2. Recon the network
3. Enumerate services
4. Review exposures
5. Build reports
6. Document remediation

## Folder overview
- app/ = dashboard UI
- labs/ = vulnerable Docker apps
- scripts/ = safe scanning and report tools
- docs/ = study guides and setup instructions
