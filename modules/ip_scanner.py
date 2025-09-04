import socket

def scan_ip(target_ip):
    try:
        socket.inet_aton(target_ip)
        print(f"IP {target_ip} is valid.")
        return True
    except socket.error:
        print(f"IP {target_ip} is invalid.")
        return False
