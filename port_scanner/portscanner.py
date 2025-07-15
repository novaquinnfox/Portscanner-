import socket
from datetime import datetime

# Target (use '127.0.0.1' or 'google.com')
target = input("Enter the IP or domain to scan: ")

# Time stamp
print("Scanning started at:", datetime.now())
print("-" * 50)

try:
    for port in range(1, 101):  # Scan ports 1 to 100
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program.")
except socket.gaierror:
    print("Hostname could not be resolved.")
except socket.error:
    print("Couldn't connect to server.")

print("-" * 50)
print("Scanning ended at:", datetime.now())
