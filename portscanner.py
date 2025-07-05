import nmap

scanner = nmap.PortScanner()

target = input("Enter the target IP address or website: ")

print("""
Choose the type of scan:
1) SYN ACK Scan
2) UDP Scan
3) Comprehensive Scan
""")

scan_type = int(input("Enter your choice (1/2/3): "))

if scan_type == 1:
    print(f"Running SYN ACK scan on {target}...")
    scanner.scan(target, '1-1024', '-v -sS')
elif scan_type == 2:
    print(f"Running UDP scan on {target}...")
    scanner.scan(target, '1-1024', '-v -sU')
elif scan_type == 3:
    print(f"Running comprehensive scan on {target}...")
    scanner.scan(target, '1-1024', '-v -sS -sV -sC -A -O')
else:
    print("Invalid scan type selected.")
    exit()

print(scanner.scaninfo())

hosts = scanner.all_hosts()
if not hosts:
    print("No hosts found. Scan may have failed or target is unreachable.")
    exit()

host = hosts[0]
print(f"IP Status: {scanner[host].state()}")
print(scanner[host].all_protocols())

for proto in scanner[host].all_protocols():
    ports = scanner[host][proto].keys()
    for port in ports:
        print(f"Port: {port}\tState: {scanner[host][proto][port]['state']}")
