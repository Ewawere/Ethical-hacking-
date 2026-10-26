#!/usr/bin/env python3
import subprocess
import sys


def run(cmd):
    print(f"[+] Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


def start_lab():
    print("[+] Starting local lab environment...")
    run(["docker", "compose", "-f", "labs/docker-compose.yml", "up", "-d"])


def stop_lab():
    print("[+] Stopping local lab environment...")
    run(["docker", "compose", "-f", "labs/docker-compose.yml", "down"])


def status():
    print("[+] Checking lab services...")
    run(["docker", "compose", "-f", "labs/docker-compose.yml", "ps"])


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python scripts/lab_manager.py start")
        print("  python scripts/lab_manager.py stop")
        print("  python scripts/lab_manager.py status")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "start":
        start_lab()
    elif cmd == "stop":
        stop_lab()
    elif cmd == "status":
        status()
    else:
        print("Unknown command.")
        sys.exit(2)


if __name__ == "__main__":
    main()
