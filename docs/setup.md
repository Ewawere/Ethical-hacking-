# Setup Guide

## Requirements
- Docker
- Python 3
- Nmap

## Step 1: Install Docker
Install Docker Desktop or Docker Engine.

## Step 2: Install nmap
Linux:
```bash
sudo apt update
sudo apt install nmap
```

## Step 3: Start lab
```bash
python scripts/lab_manager.py start
```

## Step 4: Open the dashboard
Open the app/index.html file in your browser.

## Step 5: Scan the allowed local range
```bash
python scripts/scan_lab.py 10.0.2.0/24
```

## Step 6: Review findings
Use the generated data to study service exposure and document remediation.
