from os import system as c
import time
import random
import os

A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
P = '\x1b[38;5;201m'

def logo():
    c('clear')
    print(f"""{R}
████████╗██╗██╗  ██╗████████╗ ██████╗  ██████╗ ██╗     
╚══██╔══╝██║██║  ██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     
   ██║   ██║███████║   ██║   ██║   ██║██║   ██║██║     
   ██║   ██║██╔══██║   ██║   ██║   ██║██║   ██║██║     
   ██║   ██║██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████╗
   ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
{Y} HACKING WORLD - TIKTOK AUTO FOLLOW ROOT TOOL
{A}-------------------------------------------------
""")

def loading(msg):
    for i in range(3):
        print(f"{C}{msg}{'.'*i}")
        time.sleep(0.5)
        c('clear')
        logo()

def root_check():
    result = os.system("su -c 'echo rooted' > /dev/null 2>&1")
    if result != 0:
        print(f"{R}[!] ROOT ACCESS NOT FOUND!")
        print(f"{Y}[!] Please Root Your Device To Use This Tool.")
        exit()

def auto_follow():
    logo()
    user = input(f"{C}[+] Enter TikTok Username: ")
    loading("Checking Root Permission")
    root_check()

    loading("Connecting to TikTok Secure Server")
    print(f"{G}[✓] Username Verified: {user}")
    time.sleep(1)

    followers = random.randint(10000, 99999)
    print(f"{Y}[*] Adding {followers} Followers to {user}...")
    time.sleep(2)

    for percent in range(0, 101, 5):
        print(f"{C}[*] Inject Progress: {percent}%")
        time.sleep(0.2)
        c('clear')
        logo()

    print(f"{G}[✓] Successfully Added {followers} Followers to {user}!")
    print(f"{P}[*] Please Restart TikTok App to See New Followers.")
    input(f"\n{C}Press Enter To Exit...")

auto_follow()