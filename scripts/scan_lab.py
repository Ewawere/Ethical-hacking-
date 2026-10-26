#!/usr/bin/env python3
import subprocess
import sys
import xml.etree.ElementTree as ET

ALLOWED_RANGES = [
    "10.0.2.0/24",
    "192.168.56.0/24"
]


def allowed(target):
    for range_value in ALLOWED_RANGES:
        prefix = range_value.split("/")[0]
        if target.startswith(prefix.rsplit(".", 1)[0]):
            return True
    return False


def nmap_scan(target):
    cmd = ["nmap", "-sV", "-Pn", "-oX", "-", target]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stderr)
    return result.stdout


def parse_scan(xml_text):
    root = ET.fromstring(xml_text)
    hosts = []
    for host in root.findall("host"):
        address = host.find("address[@addrtype='ipv4']")
        if address is None:
            continue
        ip = address.get("addr")
        ports = []
        for port in host.findall("./ports/port"):
            item = {
                "port": port.get("portid"),
                "protocol": port.get("protocol"),
                "state": port.find("state").get("state"),
                "service": port.find("service").get("name") if port.find("service") is not None else "unknown"
            }
            ports.append(item)
        hosts.append({"ip": ip, "ports": ports})
    return hosts


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/scan_lab.py 10.0.2.0/24")
        sys.exit(1)

    target = sys.argv[1]
    if not allowed(target):
        print("Target outside your allowed lab scope.")
        sys.exit(2)

    xml_text = nmap_scan(target)
    scan = parse_scan(xml_text)

    for host in scan:
        print(f"\nHost: {host['ip']}")
        for port in host["ports"]:
            print(f"  {port['port']}/{port['protocol']} - {port['service']} ({port['state']})")


if __name__ == "__main__":
    main()
