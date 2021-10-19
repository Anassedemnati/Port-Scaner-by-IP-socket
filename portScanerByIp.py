#!/usr/bin/env python3
import socket
import ipaddress
import re

port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

port_min = 0
port_max = 65535

print(r"""    ___                           _   _     _                            
   /   \___ _ __ ___  _ __   __ _| |_(_)   /_\  _ __   __ _ ___ ___  ___ 
  / /\ / _ \ '_ ` _ \| '_ \ / _` | __| |  //_\\| '_ \ / _` / __/ __|/ _ \
 / /_//  __/ | | | | | | | | (_| | |_| | /  _  \ | | | (_| \__ \__ \  __/
/___,' \___|_| |_| |_|_| |_|\__,_|\__|_| \_/ \_/_| |_|\__,_|___/___/\___|
                                                                         """)
print("\n****************************************************************")
print("\n*  Port Scaner by IP socket,                                   *")
print("\n*  https://github.com/Anassedemnati                            *")
print("\n*  https://www.linkedin.com/in/anassedemnati/                  *")
print("\n****************************************************************")

open_ports = []
while True:
    ip_address_input = input("\n Enter the ip address that you want to scan: ")
    try:
        ip_address_obj = ipaddress.ip_address(ip_address_input)
        # it will only execute if the ip is valid.
        print("valid ip address!")
        break
    except:
        print("invalid ip address!!")

while True:
    print("plese enter the range of port you want to scan in format (ex: 60 - 120)")
    port_range = input("enter port range: ")

    port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))

        break


for port in range(port_min, port_max + 1):
    try:
        # Create a socket object
        # You can create a socket connection similar to opening a file in Python.
        # We can change the code to allow for domain names as well.
        # With socket.AF_INET you can enter either a domain name or an ip address
        # and it will then continue with the connection.

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # You want to set a timeout for the socket to try and connect to the server.
            # If you make the duration longer it will return better results.
            # We put it at 0.5s. So for every port it scans it will allow 0.5s
            # for a successful connection.
            s.settimeout(0.5)

            s.connect((ip_address_input, port))
            open_ports.append(port)
    except:
        pass

for port in open_ports:
    print(f"Port {port} is open on {ip_address_input}")
