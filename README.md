<h1 align="center">SubDover</h1>
<p align="center">
    <a href="https://python.org">
    <img src="https://img.shields.io/badge/Python-3.7-green.svg">
  </a>
  <a href="https://github.com/Technowlogy-Pushpender/subdover/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-BSD%203-lightgrey.svg">
  </a>
  <a href="https://github.com/Technowlogy-Pushpender/subdover/releases">
    <img src="https://img.shields.io/badge/Release-1.0-blue.svg">
  </a>
    <a href="https://github.com/Technowlogy-Pushpender/subdover">
    <img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg">
  </a>
</p>

**Subdover** is a *MultiThreaded* Subdomain Takeover Vulnerability Scanner *Written In Python3*, Which has more than *55+ Fingerprints* of potentially vulnerable serivces. Uses *CNAME record* for verfication of findings. 

Built-in Subdomain Enumeration Feature & Auto HTTP prober [Uses Open Source Tool for Subdomain Enum & HTTP probing i.e. **findomain** & **httpx**]

## Disclaimer
<p align="center">
  :computer: This project was created only for good purposes and personal use.
</p>

THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER. THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.

## Features
- [x] More than 55+ Fingerprints of potentially vulnerable services
- [x] Uses CNAME record for verification of findings
- [x] Built-in Subdomain Enumeration Method [Used findomain for Subdomain Enum]
- [x] Can Scan targets from subdomain list
- [x] Can Test Single Target for Subdomain Takeover 
- [x] MultiThread, Extermely Fast Scanner [Default Threads: 10]
- [x] You can choose number of threads
- [X] You can save result in TXT file
- [x] Extremely Clean Output
- [x] OS Independent [Can be used on any OS which supports Python3]


## Tested On
[![Kali)](https://www.google.com/s2/favicons?domain=https://www.kali.org/)](https://www.kali.org) **Kali Linux - ROLLING EDITION**

[![Windows)](https://www.google.com/s2/favicons?domain=https://www.microsoft.com/en-in/windows/)](https://www.microsoft.com/en-in/windows/) **Windows 8.1 - Pro**

## Prerequisite
- [x] Python 3.X
- [x] Few External Modules

## How To Use in Linux
```bash
# Navigate to the /opt directory (optional)
$ cd /opt/

# Clone this repository
$ git clone https://github.com/Technowlogy-Pushpender/subdover.git

# Navigate to subdover folder
$ cd subdover

# Installing dependencies
$ apt-get update && apt-get install python3-pip
$ pip3 install -r requirements.txt

# If you want to enumerate subdomain using this script only, then you have to install findomain in your OS
$ # Check out this URL for Installtion Guide: https://github.com/Edu4rdSHL/findomain

# Giving Executable Permission & Checking Help Menu
$ chmod +x subdover.py
$ python3 subdover.py --help

# Testing Single Target [Running Without Giving Parameter]
$ python3 subdover.py

# Enumerating Subdomain & Testing them for Subdomain Takeover
$ python3 subdover.py -d target.com 

# Testing targets for Subdomain Takeover from subdomain list
$ python3 subdover.py --list example_target.txt 

# Changing Number of Threads
$ python3 subdover.py --thread 30 -d target.com

# Saving Result
$ python3 subdover.py -d target.com -o result.txt

# Show Fingerprints & Exit
$ python3 subdover.py -s

```

## How To Use in Windows
```bash
# Download this project as zip

# Navigate to subdover folder
$ cd subdover

# Installing dependencies
$ python -m pip install -r requirements.txt

# Checking Help Menu
$ python subdover.py --help

# Testing Single Target [Running Without Giving Parameter]
$ python subdover.py

# Enumerating Subdomain & Testing them for Subdomain Takeover
$ python subdover.py -d target.com 

# Testing targets for Subdomain Takeover from subdomain list
$ python subdover.py --list example_target.txt 

# Changing Number of Threads
$ python subdover.py --thread 30 -d target.com

# Saving Result
$ python subdover.py -d target.com -o result.txt

# Show Fingerprints & Exit
$ python subdover.py -s

```

## Available Arguments 
* Optional Arguments

| Short Hand  | Full Hand | Description |
| ----------  | --------- | ----------- |
| -h          | --help    | show this help message and exit |
| -t          | --thread  | Number of Threads to Used. Default=10 |
| -o          | --output  | Save Result in TXT file|
| -s          | --fingerprints  | Show Available Fingerprints & Exit|                  

* Required Arguments

| Short Hand  | Full Hand | Description |
| ----------  | --------- | ----------- |
| -d          | --domain  | Target Wildcard Domain [For AutoSubdomainEnumeration], ex:- google.com |
| -l          | --list    | Target Subdomain List, ex:- google_subdomain.txt |

## Available Fingerprints & CNAMES of potentially vulnerable servies

| No. | Service Name    | Status | CNAME | Fingerprints |
| --- | ------------    | ------ | ----- | ------------ |
| 1.  | Acquia          | | | |
| 2.  | Activecampaign  | | | |
| 3.  | AfterShip       | | | |
| 4.  | Aha             | | | |
| 5.  | Apigee          | | | |
| 6.  | AWS/S3          | | | |      
| 7.  | Bigcartel       | | | |
| 8.  | Bitbucket       | | | |
| 9.  | Brightcove      | | | |
| 10. | CampaignMonitor | | | |
| 11. | Cargo           | | | |
| 12. | CargoCollective | | | |
| 13. | Cloudfront      | | | |
| 14. | Desk            | | | |
| 15. | Fastly          | | | |
| 16. | Feedpress       | | | |
| 17. | Freshdesk       | | | |
| 18. | GetResponse     | | | |
| 19. | Ghost           | | | |
| 20. | Github          | | | |
| 21. | Help Juice      | | | |
| 22. | Help Scout      | | | |
| 23. | Heroku          | | | |
| 24. | Instapage       | | | |
| 25. | InterCom        | | | |
| 26. | JetBrains       | | | |
| 27. | Kajabi          | | | |
| 28. | Mashery         | | | |
| 29. | MicrosoftAzure  | | | |
| 30. | Pantheon        | | | |
| 31. | Pingdom         | | | |
| 32. | Proposify       | | | |
| 33. | Readme.io       | | | |
| 34. | Shopify         | | | |
| 35. | SimpleBooklet   | | | |
| 36. | Smartling       | | | |
| 37. | Smugmug         | | | |
| 38. | StatusPage      | | | |
| 39. | Strikingly      | | | |
| 40. | Surge.sh        | | | |
| 41. | Surveygizmo     | | | |
| 42. | Tave            | | | |
| 43. | Teamwork        | | | |
| 44. | Thinkific       | | | |
| 45. | Tictail         | | | |
| 46. | Tilda           | | | |
| 47. | Tumblr          | | | |
| 48. | Unbounce        | | | |
| 49. | UptimeRobot     | | | |
| 50. | UserVoice       | | | |
| 51. | Vend            | | | |
| 52. | WebFlow         | | | |
| 53. | WishPond        | | | |
| 54. | Wordpress       | | | |
| 55. | Zendesk         | | | |

#### Will Update This Section Later

## Screenshots

#### Help Menu
![](/img/1.Help_Menu.JPG)

#### Scan Single Target
![](/img/2.Scan_Single_Target.JPG)

#### Enumerate Subdomaun & Scan 
![](/img/3.Enum_Subdomain_And_Scan.JPG)

#### Scan Targets from SubdomainList
![](/img/4.Scan_Target_Using_SubdomainList.JPG)

#### Saving Result
![](/img/5.Saving_Result.JPG)

#### Result of Scan
![](/img/6.Result_of_Scan.JPG)

## Contribute

* All Contributors are welcome, this repo needs contributors who will improve this tool to make it best.

## TODO

- [ ] Add More Fingerprints & CNAMES 

## Contact

singhpushpender250@gmail.com 

## Buy Me A Coffee

* Support my Open Source projects by making Donation, It really motivates me to work on more projects
* PayPal Email: `shrisatender@gmail.com` [**Don't Expect to Get Reply From This Email, So Kindly Don't Send Email**]

## More Features Coming Soon...
                        
                        
