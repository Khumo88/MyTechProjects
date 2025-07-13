
import socket

def scan_ports(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a timeout for the connection attempt
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

def main():
    target = input("Enter target IP or hostname to scan: ")

    open_ports = []
    
    print(f"\n=🔎 Scanning ports 1 to 1024 0n {target}..\n")

    for port in range(1, 1025):
        print(f"Scanning port {port}...")
        if scan_ports(target, port):
            print(f"✅ Port {port} is OPEN")
            open_ports.append(port)
        else:
            print(f"❌ Port {port} is CLOSED")
    
    # Save to file
    with open("open_ports.txt", "w") as file:
        for port in open_ports:
            file.write(f"Port {port} is OPEN\n")
    
    print("\n🔎 Port scanning completed. Open ports saved to open_ports.txt")
            
if __name__ == "__main__":
    main()