**********************************************************************************************************************************************
"""This code uses the socket module to check if a specific port is open on a given host. 
The function is_port_open takes in a host and port and returns True if the port is open and False if it's closed. 
The function detect_port_scan takes in a host and uses is_port_open to check if a large number of ports are open on that host. 
If more than 10 ports are open, the code assumes that a port scan is taking place and alerts the user."""
**********************************************************************************************************************************************

import socket

def is_port_open(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((host, port))
        s.shutdown(2)
        return True
    except:
        return False

def detect_port_scan(host):
    open_ports = []
    for port in range(1, 65535):
        if is_port_open(host, port):
            open_ports.append(port)

    if len(open_ports) > 10:
        print("[ALERT] Port scan detected on host " + host + " with " + str(len(open_ports)) + " open ports.")

detect_port_scan("192.168.1.1")
