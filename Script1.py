import socket
import struct
import os

"""
Got from stackoverflow -> 
"""


def getdefaultgateway():
    with open("/proc/net/route") as fh:
        for line in fh:
            fields = line.strip().split()
            if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                continue
            return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))


"""
Stackoverflow as well
"""


def ping(host):
    response = os.system("ping -c 1" + host)
    if response == 0:
        return "SUCCEDED"
    else:
        return "FAILED"


def main():
    print("***  Beginning Test  ***")
    for i in range(0, 5):
        print(i)
    gateway = getdefaultgateway()
    remote = "8.8.8.8"
    dns = "google.com"
    print(f"Default gateway is {gateway}")
    print(f"Connection to default gateway has {ping(gateway)}")
    print(f"Remote connection has {ping(remote)}")
    print(f"DNS resolution has {ping(dns)}")
    print("***  Test Completed  ***")

