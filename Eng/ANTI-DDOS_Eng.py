import subprocess, time, sys, os # big up rex for reminding me of os.system :hahayes:
os.system('clear') # clear the screen :hahayes:

banner = """
 ____________________________________________________
|                                                   |
| [--] Name: ANTI-DDOS-Firewall                     |
|                                                   |                            
| [--] Created by: Michael Panfilov                 |
|                                                   |
| [--] Version: 0.1                                 |
|                                                   |________________________________
| [--] Warning: This programm for proctection your wifi ,isn't for global corparation|
|                                                   _________________________________|
|___________________________________________________|
"""

print(banner)

menu = input("""
	Welcome to  Anti-DDoS-Firewall AutoSetup
	Press enter to begin setup: """)

print("")
time.sleep(1)
print("\x1b[32mStarting...\x1b[37m")
time.sleep(1)
os.system('clear')
print("")
print("\x1b[32mBlocking Invalid Packets...")
os.system('iptables -t mangle -A PREROUTING -m conntrack --ctstate INVALID -j DROP')
time.sleep(1)
print("Blocking Non-SYN Packets...")
os.system('iptables -t mangle -A PREROUTING -p tcp ! --syn -m conntrack --ctstate NEW -j DROP')
time.sleep(1)
print("Blocking Uncommon MSS Values...")
os.system('iptables -t mangle -A PREROUTING -p tcp -m conntrack --ctstate NEW -m tcpmss ! --mss 536:65535 -j DROP')
time.sleep(1)
print("Blocking Bogus TCP Packets...")
os.system('iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG NONE -j DROP ')
os.system('iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,SYN FIN,SYN -j DROP')
os.system('iptables -t mangle -A PREROUTING -p tcp --tcp-flags SYN,RST SYN,RST -j DROP')
os.system('iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,RST FIN,RST -j DROP')
os.system('iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,ACK FIN -j DROP')
os.system('iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,URG URG -j DROP')
os.system('iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,FIN FIN -j DROP') 
os.system('iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,PSH PSH -j DROP')
os.system('iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL ALL -j DROP')
os.system('iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL NONE -j DROP')
os.system('iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL FIN,PSH,URG -j DROP')
os.system('iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL SYN,FIN,PSH,URG -j DROP')
os.system('iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL SYN,RST,ACK,FIN,URG -j DROP')
time.sleep(1)
print("Disabling ICMP...")
os.system('iptables -t mangle -A PREROUTING -p icmp -j DROP') # l00k i already dd0s3d u
time.sleep(1)
print("Rejecting connections from hosts with more than 80 established connections...")
connlimit = input("\x1b[31mNOTE: THIS RULE MIGHT BLOCK LEGITIMATE CONNECTIONS, WOULD YOU LIKE TO ADD THIS RULE? (y/n): ")
if connlimit == "y":
	os.system('iptables -A INPUT -p tcp -m connlimit --connlimit-above 80 -j REJECT --reject-with tcp-reset')
	time.sleep(1)
	print("\x1b[32mConnlimit rule added, continuing...")
	time.sleep(1)
	print("Blocking Fragmented Packets... (lowkey useless but we add it anyways)")
	os.system('iptables -t mangle -A PREROUTING -f -j DROP')
	time.sleep(1)
	print("All done. Thanks for using. \x1b[31mExiting.\x1b[37m")
	print("")
	exit()
if connlimit == "n":
	print("\x1b[32mConnlimit rule not added, continuing...")
	time.sleep(1)
	print("Blocking Fragmented Packets... (lowkey useless but we add it anyways)")
	os.system('iptables -t mangle -A PREROUTING -f -j DROP')
	time.sleep(1)
	print("All done. Thanks for using this firewall.")
	print("")
	exit()
