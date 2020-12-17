import subprocess, time, sys, os # big up rex for reminding me of os.system :hahayes:
os.system('clear') # clear the screen :hahayes:

banner = """
 ____________________________________________________
|                                                   |
| [--] Название: ANTI-DDOS-Firewall                 |
|                                                   |                            
| [--] Автор: Панфилов Михаил                       |
|                                                   |
| [--] Версия: 0.1                                  |
|                                                   |__________________________________________
| [--] Внимание: Данная программа для защиты вашего wifi ,не для глобальной корпарационной сети|
|                                                   ___________________________________________|
|___________________________________________________|
"""

print(banner)

menu = input("""
	Добро пожаловать в Anti-DDoS-Firewall Установщик
	Нажмите ENTER для начала установки: """)

print("")
time.sleep(1)
print("\x1b[32mStarting...\x1b[37m")
time.sleep(1)
os.system('Очистка')
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
connlimit = input("Нажмите (на Eng раскладке) y: ")
if connlimit == "y":
	os.system('iptables -A INPUT -p tcp -m connlimit --connlimit-above 80 -j REJECT --reject-with tcp-reset')
	time.sleep(1)
	print("\x1b[32mConnlimit rule added, continuing...")
	time.sleep(1)
	print("Blocking Fragmented Packets... (lowkey useless but we add it anyways)")
	os.system('iptables -t mangle -A PREROUTING -f -j DROP')
	time.sleep(1)
	print("Все отлично. Спасибо за использование данного Firewall.")
	print("")
	exit()

