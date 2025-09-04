import threading
import tkinter as tk
from tkinter import ttk, messagebox


from modules.ip_scanner import scan_ip
from modules.port_scanner import scan_ports
from modules.barcode_generator import generate_barcode
from modules.qrcode_generator import generate_qr_code
from modules.password_generator import generate_password
from modules.wordlist_generator import generate_wordlist
from modules.phone_info import get_phone_info
from modules.subdomain_checker import check_subdomain
from modules.ddos_attack import ddos_attack



def ip_scanner_action():
    ip = ip_entry.get()
    if ip:
        scan_ip(ip)
        ip_output.config(state='normal')
        ip_output.delete(1.0, tk.END)
        ip_output.insert(tk.END, f"Scanned IP: {ip}")
        ip_output.config(state='disabled')

def port_scanner_action():
    host = port_host_entry.get()
    ports = port_ports_entry.get()
    if host and ports:
        ports_list = [int(p.strip()) for p in ports.split(',')]
        open_ports = scan_ports(host, ports_list)
        port_output.config(state='normal')
        port_output.delete(1.0, tk.END)
        port_output.insert(tk.END, f"Open Ports: {open_ports}")
        port_output.config(state='disabled')

def barcode_generator_action():
    data = barcode_entry.get()
    if data:
        generate_barcode(data)
        barcode_output.config(state='normal')
        barcode_output.delete(1.0, tk.END)
        barcode_output.insert(tk.END, f"Barcode generated for: {data}")
        barcode_output.config(state='disabled')

def qr_code_generator_action():
    data = qr_entry.get()
    if data:
        generate_qr_code(data)
        qr_output.config(state='normal')
        qr_output.delete(1.0, tk.END)
        qr_output.insert(tk.END, f"QR Code generated for: {data}")
        qr_output.config(state='disabled')

def password_generator_action():
    try:
        length = int(password_length_entry.get())
        pwd = generate_password(length)
        password_output.config(state='normal')
        password_output.delete(1.0, tk.END)
        password_output.insert(tk.END, f"Generated Password: {pwd}")
        password_output.config(state='disabled')
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number for password length!")

def wordlist_generator_action():
    chars = wordlist_chars_entry.get()
    try:
        length = int(wordlist_length_entry.get())
        wordlist = generate_wordlist(chars, length)
        wordlist_output.config(state='normal')
        wordlist_output.delete(1.0, tk.END)
        wordlist_output.insert(tk.END, f"Sample Wordlist: {wordlist[:5]}...")
        wordlist_output.config(state='disabled')
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number for word length!")

def phone_info_action():
    phone = phone_entry.get()
    if phone:
        get_phone_info(phone)
        phone_output.config(state='normal')
        phone_output.delete(1.0, tk.END)
        phone_output.insert(tk.END, f"Fetched info for: {phone}")
        phone_output.config(state='disabled')

def subdomain_checker_action():
    domain = subdomain_domain_entry.get()
    subs = subdomain_list_entry.get()
    if domain and subs:
        subdomains = [s.strip() for s in subs.split(',')]
        check_subdomain(domain, subdomains)
        subdomain_output.config(state='normal')
        subdomain_output.delete(1.0, tk.END)
        subdomain_output.insert(tk.END, f"Checked subdomains for {domain}")
        subdomain_output.config(state='disabled')

def ddos_attack_action():
    url = ddos_url_entry.get()
    try:
        num_requests = int(ddos_requests_entry.get())
        threading.Thread(target=run_ddos, args=(url, num_requests), daemon=True).start()
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number of requests!")

def run_ddos(url, num_requests):
    ddos_attack(url, num_requests)
    messagebox.showinfo("DDoS Attack", "Simulation completed!")



root = tk.Tk()
root.title("Cybersecurity Tool Suite")
root.geometry("600x500")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)


tab_ip = ttk.Frame(notebook)
notebook.add(tab_ip, text="IP Scanner")
tk.Label(tab_ip, text="Enter IP Address (e.g., 192.168.1.1):").pack(pady=5)
ip_entry = tk.Entry(tab_ip, width=40)
ip_entry.pack()
tk.Button(tab_ip, text="Scan IP", command=ip_scanner_action).pack(pady=5)
ip_output = tk.Text(tab_ip, height=5, state='disabled')
ip_output.pack()


tab_port = ttk.Frame(notebook)
notebook.add(tab_port, text="Port Scanner")
tk.Label(tab_port, text="Host (e.g., example.com):").pack(pady=5)
port_host_entry = tk.Entry(tab_port, width=40)
port_host_entry.pack()
tk.Label(tab_port, text="Ports (comma-separated, e.g., 22,80,443):").pack(pady=5)
port_ports_entry = tk.Entry(tab_port, width=40)
port_ports_entry.pack()
tk.Button(tab_port, text="Scan Ports", command=port_scanner_action).pack(pady=5)
port_output = tk.Text(tab_port, height=5, state='disabled')
port_output.pack()


tab_barcode = ttk.Frame(notebook)
notebook.add(tab_barcode, text="Barcode Generator")
tk.Label(tab_barcode, text="Enter data (e.g., 1234567890):").pack(pady=5)
barcode_entry = tk.Entry(tab_barcode, width=40)
barcode_entry.pack()
tk.Button(tab_barcode, text="Generate Barcode", command=barcode_generator_action).pack(pady=5)
barcode_output = tk.Text(tab_barcode, height=5, state='disabled')
barcode_output.pack()


tab_qr = ttk.Frame(notebook)
notebook.add(tab_qr, text="QR Code Generator")
tk.Label(tab_qr, text="Enter data (e.g., https://example.com):").pack(pady=5)
qr_entry = tk.Entry(tab_qr, width=40)
qr_entry.pack()
tk.Button(tab_qr, text="Generate QR Code", command=qr_code_generator_action).pack(pady=5)
qr_output = tk.Text(tab_qr, height=5, state='disabled')
qr_output.pack()


tab_password = ttk.Frame(notebook)
notebook.add(tab_password, text="Password Generator")
tk.Label(tab_password, text="Password Length (e.g., 12):").pack(pady=5)
password_length_entry = tk.Entry(tab_password, width=10)
password_length_entry.pack()
tk.Button(tab_password, text="Generate Password", command=password_generator_action).pack(pady=5)
password_output = tk.Text(tab_password, height=5, state='disabled')
password_output.pack()


tab_wordlist = ttk.Frame(notebook)
notebook.add(tab_wordlist, text="Wordlist Generator")
tk.Label(tab_wordlist, text="Characters (e.g., abc123):").pack(pady=5)
wordlist_chars_entry = tk.Entry(tab_wordlist, width=40)
wordlist_chars_entry.pack()
tk.Label(tab_wordlist, text="Word Length (e.g., 4):").pack(pady=5)
wordlist_length_entry = tk.Entry(tab_wordlist, width=10)
wordlist_length_entry.pack()
tk.Button(tab_wordlist, text="Generate Wordlist", command=wordlist_generator_action).pack(pady=5)
wordlist_output = tk.Text(tab_wordlist, height=5, state='disabled')
wordlist_output.pack()


tab_phone = ttk.Frame(notebook)
notebook.add(tab_phone, text="Phone Info")
tk.Label(tab_phone, text="Phone Number with Country Code (e.g., +14155552671):").pack(pady=5)
phone_entry = tk.Entry(tab_phone, width=40)
phone_entry.pack()
tk.Button(tab_phone, text="Get Info", command=phone_info_action).pack(pady=5)
phone_output = tk.Text(tab_phone, height=5, state='disabled')
phone_output.pack()


tab_subdomain = ttk.Frame(notebook)
notebook.add(tab_subdomain, text="Subdomain Checker")
tk.Label(tab_subdomain, text="Domain (e.g., example.com):").pack(pady=5)
subdomain_domain_entry = tk.Entry(tab_subdomain, width=40)
subdomain_domain_entry.pack()
tk.Label(tab_subdomain, text="Subdomains (comma-separated, e.g., www,api,mail):").pack(pady=5)
subdomain_list_entry = tk.Entry(tab_subdomain, width=40)
subdomain_list_entry.pack()
tk.Button(tab_subdomain, text="Check Subdomains", command=subdomain_checker_action).pack(pady=5)
subdomain_output = tk.Text(tab_subdomain, height=5, state='disabled')
subdomain_output.pack()


tab_ddos = ttk.Frame(notebook)
notebook.add(tab_ddos, text="DDoS Attack (Safe)")
tk.Label(tab_ddos, text="URL (e.g., http://example.com):").pack(pady=5)
ddos_url_entry = tk.Entry(tab_ddos, width=40)
ddos_url_entry.pack()
tk.Label(tab_ddos, text="Number of Requests (e.g., 100):").pack(pady=5)
ddos_requests_entry = tk.Entry(tab_ddos, width=10)
ddos_requests_entry.pack()
tk.Button(tab_ddos, text="Run DDoS Simulation", command=ddos_attack_action).pack(pady=5)

root.mainloop()
