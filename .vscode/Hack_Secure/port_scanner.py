import socket
import threading

# Validate IP address format
def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

# Scan TCP port
def scan_tcp(ip, port, open_ports):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((ip, port)) == 0:
            open_ports.append(port)
        s.close()
    except:
        pass

# Scan UDP port
def scan_udp(ip, port, open_ports):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0.5)
        s.sendto(b'', (ip, port))
        s.recvfrom(1024)  # Try receiving any data
        open_ports.append(port)
    except socket.timeout:
        pass
    except:
        pass

# Main function for scanning
def main():
    try:
        ip = input("Enter IP address to scan: ").strip()
        if not is_valid_ip(ip):
            print("Invalid IP address.")
            return

        try:
            start_port = int(input("Enter starting port: "))
            end_port = int(input("Enter ending port: "))
        except ValueError:
            print("Ports must be numbers.")
            return

        if start_port < 0 or end_port > 65535 or start_port > end_port:
            print("Invalid port range.")
            return

        scan_type = input("Select scan type (TCP/UDP): ").strip().upper()

        if scan_type not in ['TCP', 'UDP']:
            print("Invalid scan type. Please enter TCP or UDP.")
            return

        open_ports = []
        threads = []

        print(f"\nStarting {scan_type} scan on {ip} from port {start_port} to {end_port}...\n")

        for port in range(start_port, end_port + 1):
            if scan_type == 'TCP':
                t = threading.Thread(target=scan_tcp, args=(ip, port, open_ports))
            else:
                t = threading.Thread(target=scan_udp, args=(ip, port, open_ports))

            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        if open_ports:
            print(f"\nOpen {scan_type} ports found:")
            for port in sorted(open_ports):
                print(f"  - Port {port} is open.")
        else:
            print(f"\nNo open {scan_type} ports found.")

    except KeyboardInterrupt:
        print("\nScan cancelled.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
