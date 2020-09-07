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
    parser = argparse.ArgumentParser(description=f'{RED}SubDover v1.1')
    parser._optionals.title = f"{GREEN}Optional Arguments{YELLOW}"
    parser.add_argument("-t", "--thread", dest="thread", help="Number of Threads to Used. Default=10", default=10)
    parser.add_argument("-o", "--output", dest="output", help="Save Result in TXT file")
    parser.add_argument("--update", dest="check_and_update", help="Check & Update Subdover", action='store_true')
    parser.add_argument("-s", "--fingerprints", dest="show_fingerprint", help="Show Available Fingerprints & Exit", action='store_true')   
    
    required_arguments = parser.add_argument_group(f'{RED}Required Arguments{GREEN}')
    required_arguments.add_argument("-d", "--domain", dest="domain", help="Target Wildcard Domain [For AutoSubdomainEnumeration], ex:- google.com")
    required_arguments.add_argument("-l", "--list", dest="subdomain_list", help="Target Subdomain List, ex:- google_subdomain.txt")
    return parser.parse_args()

def check_and_update():            
    try:
        ongoing_version = requests.get("https://raw.githubusercontent.com/PushpenderIndia/subdover/master/version.txt")
    except Exception:
        print(f"{WHITE}[{RED}ERR{WHITE}] No Internet Connection")
        sys.exit()
        
    ongoing_version = ongoing_version.text.strip()
    
    with open(f"{subdover_dir}version.txt", "r") as currentVersion:
        if currentVersion.read() != ongoing_version:
            print(f"{YELLOW}[*] Installing Subdover v{ongoing_version}")
            subprocess.run("git pull origin master", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            print(f"{GREEN}[+] Updated to latest version: v{ongoing_version}..")
            
            with open(f"{subdover_dir}version.txt", "w") as f:
                f.write(ongoing_version)
            sys.exit()
        else:
            print(f"{GREEN}[+] Subdover is already Up-to-Date: v{ongoing_version}..")
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
        subprocess.run(f"{findomain_path} --output --target {domain}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

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
            print(f"{RED}[!] ConnectionError : {WHITE}{url}")
            not_success = False
            break
        
        elif error.lower() in targetResponse.lower():
            if error.lower() == "":
                pass
                
            else:
                service_cname_list = fingerprint[2]
                confirm, enumeratedCNAME = confirm_vulnerable(url, service_cname_list)
                if confirm == True:            
                    print(f"{GREEN}[+] {fingerprint[1]} ===> : {WHITE}[{RED}Service{WHITE}: {fingerprint[0]}] {WHITE}[{RED}CNAME{WHITE}: {enumeratedCNAME}] : {GREEN}{url}{WHITE}")
                    not_success = False
                    if arguments.output:
                        with open(arguments.output, "a") as f:
                            f.write(f"[+] {fingerprint[1]} ===> : [Service: {fingerprint[0]}] [CNAME: {enumeratedCNAME}] : {url}\n")
                    break
                    
                elif confirm == "NotSure" and fingerprint[0] not in ["CargoCollective", "Akamai"]: 
                    #CargoCollective & Akamai fingerprints can leads to False +ve 
                    #If script is unable to confirm detection using CNAME, then we will ignore that detection
                    
                    print(f"{GREEN}[+] {fingerprint[1]} ===> : {WHITE}[{RED}Service{WHITE}: {fingerprint[0]}] {WHITE}[{RED}CNAME{WHITE}: 404, UnableToVerify-CouldBeFalsePositive] : {GREEN}{url}{WHITE}")
                    not_success = False
                    if arguments.output:
                        with open(arguments.output, "a") as f:
                            f.write(f"[+] {fingerprint[1]} ===> : [Service: {fingerprint[0]}] [CNAME: 404, UnableToVerify-CouldBeFalsePositive] : {url}\n")
                    break                    
         
    if not_success:
        print(f"{WHITE}[-] Not Vulnerable  : {GREEN}{url}{WHITE}")        

def start_scanning(subdomain_list):
    for subdomain in subdomain_list:
        testTarget(subdomain)     

if __name__ == '__main__':
    print(f"\t\t{YELLOW}Author: {GREEN}Pushpender Singh  | {YELLOW}GitHub: {GREEN}Technowlogy-Pushpender\n{WHITE}")
    arguments = get_arguments() 

    KillThread = False
    
    if arguments.output:
        with open(arguments.output, "w") as f:
            f.write("                   +===============================+\n")
            f.write("                   | SUBDOVER (SUBDomain takeOVER) |\n")
            f.write("                   +===============================+\n\n")
            f.write("       (Tool Author: Pushpender | GitHub: Technowlogy-Pushpender)\n")
            f.write("+======================================================================+\n")
            f.write("| Potentially Vulnerable Targets to Subdomain Takeover (DNS Hijacking) |\n")
            f.write("+======================================================================+\n")

    if arguments.check_and_update:
        if AttackerSystem == "Windows":
            try:
                git_path = subprocess.check_output("where git", shell=True)
                check_and_update()
            except Exception:
                print(f"{WHITE}[{RED}ERR{WHITE}] GIT is NOT Installed on Your System! You can't use AutoUpdater .") 
                sys.exit()
        else:
            try:
                git_path = subprocess.check_output("which git", shell=True)
                check_and_update()
            except Exception:
                print(f"{WHITE}[{RED}ERR{WHITE}] GIT is NOT Installed on Your System! You can't use AutoUpdater .")              
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
            print("==================================================================")
            print(f"[*] Adding Appropriate Web Protocal to Subdomains using httpx ...")
            
            if AttackerSystem == "Windows":
                subprocess.run(f"type {arguments.subdomain_list} | \"{httpx_path}\" -threads 100 -o {arguments.subdomain_list}-httpx.txt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            else:
                subprocess.run(f"cat {arguments.subdomain_list} | httpx -threads 100 -o {arguments.subdomain_list}-httpx.txt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            
            print(f"[*] Writing Subdomains in New TXT file ...")
            os.remove(f"{arguments.subdomain_list}")
            os.rename(f"{arguments.subdomain_list}-httpx.txt", f"{arguments.subdomain_list}")
            print(f"[+] Done !")
            print("==================================================================\n")        
            subdomain_list = readTargetFromFile(arguments.subdomain_list)
            
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


    
