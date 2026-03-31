# Port Scanner

A lightweight multithreaded TCP port scanner written in Python. Built as a learning project to understand how port scanning works at the socket level, and how threading can speed up network reconnaissance.

---

## How It Works

The scanner spawns one thread per port in the target range. Each thread attempts a TCP connection using `socket.connect_ex()` — if the call returns `0`, the port is open. A lock ensures thread-safe writes to the shared results list.

---

## Usage

```bash
python port_scanner.py
```

By default, it scans ports 1–1000 on `127.0.0.1`. Edit the `ip` and port range directly in the script to target a different host.

---

## Security Notes

Open ports are visible attack surfaces. Even in a lab environment, it is worth understanding what each open port exposes:

- **Firewall rules** — block all non-essential inbound traffic at the perimeter
- **IDS/IPS** — rapid connection attempts from a single source should trigger an alert
- **Least privilege** — services should only bind to the ports they need, never run as root

This scanner performs the same initial reconnaissance an attacker would run during enumeration. Understanding how it works helps in hardening systems against it.

---

## Requirements

- Python 3.x
- No external dependencies — uses the standard library only (`socket`, `threading`)

---

## Disclaimer

This tool is for educational and authorized testing purposes only. Scanning networks or systems without explicit permission is illegal. The developer is not responsible for any misuse.