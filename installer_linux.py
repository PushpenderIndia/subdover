#!/usr/bin/python3

import os, subprocess, sys
from datetime import datetime
from datetime import date

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def isRoot():
    if not os.geteuid() == 0:
        sys.exit("{RED}[!] Installer must be run as root")

def getCurrentTime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")  
    
def getCurrentDate():
    return date.today().strftime("%Y-%m-%d")
    
def printInfo(text):
    print("\n=========================================================================")
    print(f"[{BLUE}{getCurrentTime()}{WHITE}] [{GREEN}INFO{WHITE}] " + text)
    print("=========================================================================")
    
def printWarning(text):
    print("\n=========================================================================")
    print(f"[{BLUE}{getCurrentTime()}{WHITE}] [{YELLOW}WARNING{WHITE}] " + text)    
    print("=========================================================================")

def install_python_dependencies():
    printInfo(f"installing Python3 dependencies ...")
    os.system("apt-get update && apt-get install python3-pip")
    os.system("pip3 install -r requirements.txt")

def install_golang():
    result = subprocess.run("go version", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    if result.returncode != 0:
        printWarning(f"golang is not installed. {GREEN}Installing...{WHITE}")
        # Installing package
        os.system("sudo apt install -y golang")

        # Then adding the following to your .bashrc
        os.system("export GOROOT=/usr/lib/go")
        os.system("export GOPATH=$HOME/go")
        os.system("export PATH=$GOPATH/bin:$GOROOT/bin:$PATH")
        
        # Reloading your .bashrc              
        os.system("source .bashrc")

def install_httpx():
    result = subprocess.run("httpx -version", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    if result.returncode != 0:
        printWarning(f"httpx is not installed. {GREEN}Installing...{WHITE}")
        os.system("git clone https://github.com/projectdiscovery/httpx.git; cd httpx/cmd/httpx; go build; mv httpx /usr/local/bin/")

def install_findomain():
    result = subprocess.run("findomain --version", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    if result.returncode != 0:
        printWarning(f"findomain is not installed. {GREEN}Installing...{WHITE}")
        choice = input("[?] Want to Install findomain via (S)ourceCode or From (B)inaries (B/S) ? : ")
        if choice.lower() == "b" or choice.lower == "": 
            os.system("wget https://github.com/Edu4rdSHL/findomain/releases/latest/download/findomain-linux -O findomain")
            os.system("chmod +x findomain")
            os.system("mv findomain /usr/local/bin/")
        
        else:
            os.system("git clone https://github.com/Edu4rdSHL/findomain.git")
            os.system("cd findomain")
            os.system("cargo build --release") 
            os.system("sudo cp target/release/findomain /usr/bin/")  
    
    printInfo(f"{GREEN}[+] Done!{WHITE}")

        
if __name__ == '__main__':
    isRoot()
    
    print(f"\n[*] starting installation @ {getCurrentTime()} /{getCurrentDate()}/\n")
    
    install_python_dependencies()
    install_golang()
    install_httpx()
    install_findomain()
