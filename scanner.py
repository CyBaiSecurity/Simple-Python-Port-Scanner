import socket
import threading

ip = "127.0.0.1"
lock = threading.Lock()
open_ports = []


def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((ip, port))
    s.close()


    if result == 0:
        with lock:
            print(f"Port {port} is open!")
            open_ports.append(port)

threads = []

for port in range (1,1001):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"\nScan complete. Open ports: {open_ports}")




