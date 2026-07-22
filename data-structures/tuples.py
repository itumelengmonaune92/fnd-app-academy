"""
The Challenge: "Immutable Network Device Configuration Log"

Background:
In Network & Desktop Support operations, device state logs use tuples 
to ensure critical network data remains immutable and tamper-proof.

Requirements:
1. Data Setup & Unpacking:
   - Create a single device log tuple: ("CPT-SW-01", "192.168.1.50", 8080, "ACTIVE")
   - Unpack this tuple into four distinct variables (name, ip, port, status) 
     and print an admin summary using an f-string.

2. Tuple Concatenation & Searching:
   - Define a simple tuple of active port numbers: ports = (80, 443, 8080, 8080, 22)
   - Combine it with a new tuple of backup ports (3389, 8080) using concatenation (+).
   - Use `.count()` to find how many times port 8080 appears in the combined ports tuple.
   - Use `.index()` to find the position of port 22.

3. Immutability Verification:
   - Attempt to change the status of your device tuple to "OFFLINE" inside a try/except 
     block to demonstrate and handle Python's TypeError for tuple immutability.
"""

# 1. Data Setup & Unpacking
device_logs = ("CPT-SW-01", "192.168.1.50", 8080, "ACTIVE")

# unpack all values into four distinct variables
name, ip, port, status = device_logs
print(f"Admin summary: name: {name}, ip_address: {ip}, port_no: {port}, status: {status}")

# 2. Tuple Concatenation & Searching
active_ports = (80, 443, 8080, 8080, 22)
backup_ports = (3389, 8080)

combined_ports = active_ports + backup_ports
total_ports = combined_ports.count(8080)
port_position_22 = combined_ports.index(22)

print()
print(f"Combined ports: {combined_ports}")
print(f"Total numbner of ports: {total_ports}")
print(f"Port number 22 is located at index no: {port_position_22}")

# 3. Immutability Verification
try:
   device_logs[3] = "OFFLINE"
except TypeError as e:
   print(f"Manual status change is not allowed: {e}")
   print()