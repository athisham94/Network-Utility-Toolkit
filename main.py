from modules.ip_scanner import scan_ip
from modules.port_scanner import scan_ports
from modules.barcode_generator import generate_barcode
from modules.qrcode_generator import generate_qr_code
from modules.password_generator import generate_password
from modules.wordlist_generator import generate_wordlist
from modules.phone_info import get_phone_info
from modules.subdomain_checker import check_subdomain
from modules.ddos_attack import ddos_attack

def display_menu():
    print("\nPlease choose an option:")
    print("1. IP Scanner")
    print("2. Port Scanner")
    print("3. Barcode Generator")
    print("4. QR Code Generator")
    print("5. Password Generator")
    print("6. Wordlist Generator")
    print("7. Phone Info")
    print("8. Subdomain Checker")
    print("9. DDoS Attack")
    print("0. Exit")

def main():
    while True:
        display_menu()
        
        # Taking user input
        choice = input("Enter your choice (0-9): ")

        if choice == '1':
            # IP Scanner
            ip = input("Enter an IP address to scan (e.g., 192.168.1.1): ")
            scan_ip(ip)
        
        elif choice == '2':
            # Port Scanner
            host = input("Enter the host to scan (e.g., example.com): ")
            ports_input = input("Enter ports to scan (comma-separated, e.g., 80, 443, 22): ")
            ports = [int(port.strip()) for port in ports_input.split(',')]
            open_ports = scan_ports(host, ports)
            print(f"Open Ports: {open_ports}")
        
        elif choice == '3':
            # Barcode Generator
            data = input("Enter data for barcode generation (e.g., 1234567890): ")
            generate_barcode(data)
        
        elif choice == '4':
            # QR Code Generator
            data = input("Enter data for QR code generation (e.g., https://www.example.com): ")
            generate_qr_code(data)
        
        elif choice == '5':
            # Password Generator
            length = int(input("Enter the length of the password (e.g., 12): "))
            password = generate_password(length)
            print(f"Generated Password: {password}")
        
        elif choice == '6':
            # Wordlist Generator
            chars = input("Enter characters to generate wordlist from (e.g., abc123): ")
            length = int(input("Enter word length for wordlist (e.g., 4): "))
            wordlist = generate_wordlist(chars, length)
            print(f"Generated Wordlist: {wordlist[:5]}...")  # Display first 5 entries
        
        elif choice == '7':
            # Phone Info
            phone_number = input("Enter a phone number with country code (e.g., +14155552671): ")
            get_phone_info(phone_number)
        
        elif choice == '8':
            # Subdomain Checker
            domain = input("Enter a domain to check for subdomains (e.g., example.com): ")
            subdomains_input = input("Enter subdomains to check (comma-separated, e.g., www, api, mail): ")
            subdomains = [sub.strip() for sub in subdomains_input.split(',')]
            check_subdomain(domain, subdomains)
        
        elif choice == '9':
            # DDoS Attack
            url = input("Enter a URL for DDoS simulation (e.g., http://example.com): ")
            num_requests = int(input("Enter the number of requests to send (e.g., 100): "))
            ddos_attack(url, num_requests)
        
        elif choice == '0':
            # Exit the program
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
