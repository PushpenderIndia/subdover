from src.fingerprints import * 
import requests
import argparse
import sys
import os
import subprocess
import dns.resolver
import threading
import numpy as np
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

from colorama import init
from colorama import Fore, Back, Style
init()

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

if os.name in ('ce', 'nt', 'dos'):
    AttackerSystem = "Windows"
elif 'posix' in os.name:
    AttackerSystem = "Linux"

# Declearing Environmental Path for Subdover    
subdover_dir = str(os.path.realpath(__file__)).replace("subdover.py", "").replace("\\", "/")
findomain_path = subdover_dir + "externals/findomain.exe"
httpx_path = subdover_dir + "externals/httpx.exe"

def get_arguments():
    parser = argparse.ArgumentParser(description=f'{Fore.RED}SubDover v1.5')
    parser._optionals.title = f"{Fore.GREEN}Optional Arguments{Fore.YELLOW}"
    parser.add_argument("-t", "--thread", dest="thread", help="Number of Threads to Used. Default=10", default=10)
    parser.add_argument("-o", "--output", dest="output", help="Save Result in TXT file")
    parser.add_argument("-u", "--update", dest="check_and_update", help="Check & Update Subdover", action='store_true')
    parser.add_argument("-skip", "--skip-httpx", dest="skip_httpx_probing", help=F"Skip HTTP/HTTPS Protocal Resolution ({Fore.WHITE}HTTP Probing{Fore.YELLOW}) [{Fore.RED}NOTE{Fore.YELLOW}]: You must manually use httpx/httprobe on your subdomain list & then provide that final subdomains list using {Fore.GREEN}--list {Fore.YELLOW}or {Fore.GREEN}-l{Fore.YELLOW} flag", action='store_true')
    parser.add_argument("-s", "--fingerprints", dest="show_fingerprint", help="Show Available Fingerprints & Exit", action='store_true')   
    
    required_arguments = parser.add_argument_group(f'{Fore.RED}Required Arguments{Fore.GREEN}')
    required_arguments.add_argument("-d", "--domain", dest="domain", help="Target Wildcard Domain [For AutoSubdomainEnumeration], ex:- google.com")
    required_arguments.add_argument("-l", "--list", dest="subdomain_list", help="Target Subdomain List, ex:- google_subdomain.txt")
    return parser.parse_args()

def check_dependencies(commandToCheck):
    a = subprocess.run(str(commandToCheck), shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    if a.returncode == 0:
        print(f"{Fore.GREEN}[+] {Fore.WHITE}{commandToCheck.split()[0]} {Fore.GREEN}is Installed on your system.{Fore.WHITE}")
    else:
        print(f"{Fore.RED}[!] {Fore.WHITE}{commandToCheck.split()[0]}{Fore.RED} is not Installed on your system.{Fore.WHITE}")
        sys.exit()

def check_and_update():            
    try:
        ongoing_version = requests.get("https://raw.githubusercontent.com/PushpenderIndia/subdover/master/version.txt")
    except Exception:
        print(f"{Fore.WHITE}[{Fore.RED}ERR{Fore.WHITE}] No Internet Connection")
        sys.exit()
        
    ongoing_version = ongoing_version.text.strip()
    
    with open(subdover_dir+"version.txt", "r") as f:
        currentVersion = f.read()
        if currentVersion != ongoing_version:
            print(f"{Fore.YELLOW}[*] Installing Subdover v{ongoing_version}")
            subprocess.run("git pull origin master", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            print(f"{Fore.GREEN}[+] Updated to latest version: v{ongoing_version}..")
            
            with open(subdover_dir+"version.txt", "w") as f:
                f.write(ongoing_version)
            sys.exit()
        else:
            print(f"{Fore.GREEN}[+] Subdover is already Up-to-Date: v{ongoing_version}..")
            sys.exit()

def readTargetFromFile(filepath):
    """
    Returns: List of Subdomain
    """
    subdomain_list = []
    
    with open(filepath, "r") as f:
        for subdomain in f.readlines():
            if subdomain != "": 
                subdomain_list.append(subdomain.strip())  

    return subdomain_list
    
def split_list(list_name, total_part_num):
    """
    Takes Python List and Split it into desired no. of sublist
    """
    final_list = []
    split = np.array_split(list_name, total_part_num)
    for array in split:
        final_list.append(list(array))		
    return final_list    
    
def enumSubdomain(domain):
    if AttackerSystem == "Windows":
        print("[*] Finding Subdomain Using findomain ...") 
        subprocess.run(f"\"{findomain_path}\" --output --target {domain}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

        print(f"[*] Adding Appropriate Web Protocal to Subdomains using httpx ...")
        subprocess.run(f"type {domain}.txt | \"{httpx_path}\" -threads 100 -o {domain}-httpx.txt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    else:
        print("[*] Finding Subdomain Using findomain ...") 
        subprocess.run(f"findomain --output --target {domain}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        
        print(f"[*] Adding Appropriate Web Protocal to Subdomains using httpx ...")
        subprocess.run(f"cat {domain}.txt | httpx -threads 100 -o {domain}-httpx.txt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
     
    print(f"[*] Saving Subdomains in TXT file ...")
    os.remove(f"{domain}.txt")
    os.rename(f"{domain}-httpx.txt", f"{domain}.txt")
    print(f"[+] Done")  
    
def enumCNAME(domain):
    cname = ""

    domain_without_protocal = domain.replace("http://", "")
    domain_without_protocal = domain_without_protocal.replace("https://", "")
    
    try:
        result = dns.resolver.resolve(domain_without_protocal, 'CNAME')
        for cnameeval in result:
            cname = cnameeval.target.to_text()
    except Exception:
        pass
        
    return cname
    
def confirm_vulnerable(domain, service_cname_list):
    confirm = False

    enumeratedCNAME = enumCNAME(domain)
    if enumeratedCNAME == "":  # Because URL such as https://githublol.github.io (which doesn't exist) will have CNAME==""
        confirm = "NotSure"
    
    else:
        for service_cname in service_cname_list:
            if service_cname in enumeratedCNAME:
                confirm = True
                
    return confirm, enumeratedCNAME          

def testTarget(url):
    not_success = True

    try:
        response = requests.get(url, headers=headers, timeout=(3,5), verify=False)
        targetResponse = response.text
    except Exception:
        targetResponse = "ConnectionError_SubDover"
        
    for fingerprint in fingerprints_list:
        error = fingerprint[3]
        
        if targetResponse == "ConnectionError_SubDover":
            print(f"{Fore.RED}[!] ConnectionError : {Fore.WHITE}{url}")
            not_success = False
            break
        
        elif error.lower() in targetResponse.lower():
            if error.lower() == "":
                pass
                
            else:
                service_cname_list = fingerprint[2]
                confirm, enumeratedCNAME = confirm_vulnerable(url, service_cname_list)
                if confirm == True:            
                    print(f"{Fore.GREEN}[+] {fingerprint[1]} ===> : {Fore.WHITE}[{Fore.RED}Service{Fore.WHITE}: {fingerprint[0]}] {Fore.WHITE}[{Fore.RED}CNAME{Fore.WHITE}: {enumeratedCNAME}] : {Fore.GREEN}{url}{Fore.WHITE}")
                    not_success = False
                    if arguments.output:
                        with open(arguments.output, "a") as f:
                            f.write(f"[+] {fingerprint[1]} ===> : [Service: {fingerprint[0]}] [CNAME: {enumeratedCNAME}] : {url}\n")
                    break
                    
                elif confirm == "NotSure" and fingerprint[0] not in ["CargoCollective", "Akamai"]: 
                    #CargoCollective & Akamai fingerprints can leads to False +ve 
                    #If script is unable to confirm detection using CNAME, then we will ignore that detection
                    
                    print(f"{Fore.GREEN}[+] {fingerprint[1]} ===> : {Fore.WHITE}[{Fore.RED}Service{Fore.WHITE}: {fingerprint[0]}] {Fore.WHITE}[{Fore.RED}CNAME{Fore.WHITE}: 404, UnableToVerify-CouldBeFalsePositive] : {Fore.GREEN}{url}{Fore.WHITE}")
                    not_success = False
                    if arguments.output:
                        with open(arguments.output, "a") as f:
                            f.write(f"[+] {fingerprint[1]} ===> : [Service: {fingerprint[0]}] [CNAME: 404, UnableToVerify-CouldBeFalsePositive] : {url}\n")
                    break                    
         
    if not_success:
        print(f"{Fore.WHITE}[-] Not Vulnerable  : {Fore.GREEN}{url}{Fore.WHITE}")        

def start_scanning(subdomain_list):
    for subdomain in subdomain_list:
        testTarget(subdomain)     

if __name__ == '__main__':
    print(f"\t\t{Fore.YELLOW}Author: {Fore.GREEN}Pushpender Singh  | {Fore.YELLOW}GitHub: {Fore.GREEN}PushpenderIndia\n{Fore.WHITE}")
    arguments = get_arguments() 
    
    if AttackerSystem == "Linux":
        print("========================================================")
        print("[>>] Checking Dependencies ...")
        print("========================================================")
        check_dependencies("findomain --version")
        check_dependencies("httpx -version")
        print("\n")    

    KillThread = False
    
    if arguments.output:
        with open(arguments.output, "w") as f:
            f.write("                   +===============================+\n")
            f.write("                   | SUBDOVER (SUBDomain takeOVER) |\n")
            f.write("                   +===============================+\n\n")
            f.write("       (Tool Author: Pushpender | GitHub: @PushpenderIndia)\n")
            f.write("+======================================================================+\n")
            f.write("| Potentially Vulnerable Targets to Subdomain Takeover (DNS Hijacking) |\n")
            f.write("+======================================================================+\n")

    if arguments.check_and_update:
        if AttackerSystem == "Windows":
            try:
                git_path = subprocess.check_output("where git", shell=True)
                check_and_update()
            except Exception:
                print(f"{Fore.WHITE}[{Fore.RED}ERR{Fore.WHITE}] GIT is NOT Installed on Your System! You can't use AutoUpdater .") 
                sys.exit()
        else:
            try:
                git_path = subprocess.check_output("which git", shell=True)
                check_and_update()
            except Exception:
                print(f"{Fore.WHITE}[{Fore.RED}ERR{Fore.WHITE}] GIT is NOT Installed on Your System! You can't use AutoUpdater .")              
                sys.exit()
    try:
        if arguments.show_fingerprint:
            print("+------------------------+")
            print("| Available Fingerprints |")
            print("+------------------------+")
            number = 1
            for fingerprint in fingerprints_list:
                print(f"{number}. {fingerprint[0]}")
                number += 1
        
        elif arguments.subdomain_list:
            if arguments.skip_httpx_probing:
                subdomain_list = readTargetFromFile(arguments.subdomain_list)

            else:
                print("==================================================================") 
                print(f"[*] Adding Appropriate Web Protocal to Subdomains using httpx ...")
                if "\\" in arguments.subdomain_list:
                    filename = arguments.subdomain_list.split("\\")[-1]
                    
                elif "\\\\" in arguments.subdomain_list:
                    filename = arguments.subdomain_list.split("\\\\")[-1]
                    
                elif "/" in arguments.subdomain_list:
                    filename = arguments.subdomain_list.split("/")[-1] 
                    
                else:
                    filename = arguments.subdomain_list
                    
                outputFileName = arguments.subdomain_list.replace(filename, filename.replace(" ", "_")) + "_httpx.txt"    
                
                if AttackerSystem == "Windows":
                    subprocess.run(f"type \"{arguments.subdomain_list}\" | \"{httpx_path}\" -threads 100 -o \"" + outputFileName + "\"", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                else:
                    subprocess.run(f"cat \"{arguments.subdomain_list}\" | httpx -threads 100 -o \"" + outputFileName + "\"", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            
                print(f"[+] Done !")
                print("==================================================================\n")        
                subdomain_list = readTargetFromFile(outputFileName)
            
            final_subdomain_list = split_list(subdomain_list, int(arguments.thread))

            print("==================================================")
            print(f"[>>] Total Threads                : {arguments.thread}")
            print(f"[>>] Total Targets Loaded         : {len(subdomain_list)}")
            print(f"[>>] Total Fingerprints Available : {len(fingerprints_list)}")
            print("[>>] Scanning Targets for Subdomain Takeover")
            print("==================================================")
                        
            for thread_num in range(int(arguments.thread)):   
                t1 = threading.Thread(target=start_scanning, args=(final_subdomain_list[thread_num],)) 
                t1.start()
                
        elif arguments.domain:
            print("========================================================")
            print(f"[>>] Enumerating Subdomains for : {arguments.domain}")
            print("========================================================")
            enumSubdomain(arguments.domain)          
            
            subdomain_list = readTargetFromFile(f"{arguments.domain}.txt")
            
            final_subdomain_list = split_list(subdomain_list, int(arguments.thread))
            print("\n=============================================")
            print(f"[>>] Total Threads                : {arguments.thread}")
            print(f"[>>] Total Targets Loaded         : {len(subdomain_list)}")
            print(f"[>>] Total Fingerprints Available : {len(fingerprints_list)}")
            print("[>>] Scanning Targets for Subdomain Takeover")
            print("=============================================")
            
            for thread_num in range(int(arguments.thread)):
                t1 = threading.Thread(target=start_scanning, args=(final_subdomain_list[thread_num],)) 
                t1.start()           
        
        else:
            url = input("\n[?] Enter URL: ")
            testTarget(url)
            
    except KeyboardInterrupt:
        sys.exit()


    
