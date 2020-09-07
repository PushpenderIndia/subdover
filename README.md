<h1 align="center">SubDover</h1>
<p align="center">
    <a href="https://python.org">
    <img src="https://img.shields.io/badge/Python-3.7-green.svg">
  </a>
  <a href="https://github.com/PushpenderIndia/subdover/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-BSD%203-lightgrey.svg">
  </a>
  <a href="https://github.com/PushpenderIndia/subdover/releases">
    <img src="https://img.shields.io/badge/Release-1.0-blue.svg">
  </a>
    <a href="https://github.com/PushpenderIndia/subdover">
    <img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg">
  </a>
</p>

**Subdover** is a *MultiThreaded* Subdomain Takeover Vulnerability Scanner *Written In Python3*, Which has more than *70+ Fingerprints* of potentially vulnerable serivces. Uses *CNAME record* for verfication of findings. 

Built-in Subdomain Enumeration Feature & Auto HTTP prober [Uses Open Source Tool for Subdomain Enum & HTTP probing i.e. **findomain** & **httpx**]

Total_Fingerprints(**Aquatone** + **Subjack** + **Subzy** + **SubOver**) <<< Total_Fingerprints(**SubDover**)

## Disclaimer
<p align="center">
  :computer: This project was created only for good purposes and personal use.
</p>

THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER. THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.

## Features
- [x] More than 70+ Fingerprints of potentially vulnerable services
- [x] Uses CNAME record for verification of findings
- [x] Built-in Subdomain Enumeration Method [**Used findomain for Subdomain Enum**]
- [x] Can Scan targets from subdomain list
- [x] Can Test Single Target for Subdomain Takeover 
- [x] MultiThread, Extermely Fast Scanner [**Default Threads: 10**]
- [x] You can choose number of threads
- [X] You can save result in TXT file
- [x] Extremely Clean Output
- [x] OS Independent [**Can be used on any OS which supports Python3**]


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
$ git clone https://github.com/PushpenderIndia/subdover.git

# Navigate to subdover folder
$ cd subdover

# Installing dependencies
$ apt-get update && apt-get install python3-pip
$ pip3 install -r requirements.txt

# NOTE : Install findomain & httpx On your Linux OS
# Installtion Guide (findomain) : https://github.com/Edu4rdSHL/findomain
# Installtion Guide (httpx) : https://github.com/projectdiscovery/httpx

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

## How to Install Subdover in PentestBox
```bash
# Navigate to C:\PentestBox\bin\customtools Directory
$ cd C:\PentestBox\bin\customtools

# Clone This GitHub Repo
$ git clone https://github.com/PushpenderIndia/subdover.git

# Navigate to subdover folder
$ cd subdover

# Install Python Dependencies
$ python -m pip install -r requirements.txt

# Add Console Shortcut/Alias In PentestBox
$ echo subdover=python "%pentestbox_ROOT%\bin\customtools\subdover\subdover.py" $* >> ../customaliases
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

| No. | Service Name   			    | Status     | CNAME | Fingerprints |
| --- | ------------   				| ------     | ----- | ------------ |
| 1.  | Acquia                      | Vulnerable | `['acquia-test.co']` | `The site you are looking for could not be found.` |
| 2.  | ActiveCampaign              | Vulnerable | `['activehosted.com']` | `alt="LIGHTTPD - fly light."` |
| 3.  | AfterShip                   | Vulnerable | `['aftership.com']` | `Oops.</h2><p class="text-muted text-tight">The page you're looking for doesn't exist.` |
| 4.  | AgileCRM                    | Vulnerable | `['cname.agilecrm.com', 'agilecrm.com']` | `Sorry, this page is no longer available.` |
| 5.  | Aha                         | Vulnerable | `['ideas.aha.io']` | `There is no portal here ... sending you back to Aha!` |
| 6.  | Airee.ru                    | Vulnerable | `['cdn.airee.com', 'airee.com']` | `LaterADD` |
| 7.  | Anima                       | Vulnerable | `['NOT_AVAILABLE']` | `If this is your website and you've just created it, try refreshing in a minute` |
| 8.  | Apigee                      | Vulnerable | `['-portal.apigee.net']` |  |
| 9.  | AWS/S3                      | Vulnerable | `['amazonaws']` | `The specified bucket does not exist` |
| 10. | Bigcartel                   | Vulnerable | `['bigcartel.com']` | `<h1>Oops! We could&#8217;t find that page.</h1>` |
| 11. | Bitbucket                   | Vulnerable | `['bitbucket.io']` | `Repository not found` |
| 12. | Brightcove                  | Vulnerable | `['bcvp0rtal.com', 'brightcovegallery.com', 'gallery.video']` | `<p class="bc-gallery-error-code">Error Code: 404</p>` |
| 13. | Canny.io                    | Vulnerable | `['cname.canny.io']` | `There is no such company. Did you enter the right URL?` |
| 14. | CampaignMonitor             | Vulnerable | `['createsend.com', 'name.createsend.com']` | `Double check the URL or <a href="mailto:help@createsend.com` |
| 15. | Cargo                       | Vulnerable | `['cargocollective.com']` | `If you're moving your domain away from Cargo you must make this configuration through your registrar's DNS control panel.` |
| 16. | CargoCollective             | Vulnerable | `['subdomain.cargocollective.com']` | `404 Not Found` |
| 17. | Cloudfront                  | Edge case  | `['cloudfront.net']` | `Bad Request: ERROR: The request could not be satisfied` |
| 18. | Desk                        | Not vulnerable | `['desk.com']` | `Please try again or try Desk.com free for 14 days.` |
| 19. | ElasticBeanstalk_AWS_service| Vulnerable | `['elasticbeanstalk.com']` |  |
| 20. | Fastly                      | Edge case  | `['fastly.net']` | `Fastly error: unknown domain:` |
| 21. | Feedpress                   | Vulnerable | `['redirect.feedpress.me']` | `The feed has not been found.` |
| 22. | Freshdesk                   | Vulnerable | `['freshdesk.com']` | `May be this is still fresh!` |
| 23. | Frontify                    | Vulnerable | `['frontify.com']` | `404 - Page not found. Oops... look like you got lost.` |
| 24. | GetResponse                 | Vulnerable | `['.gr8.com']` | `With GetResponse Landing Pages, lead generation has never been easier` |
| 25. | Ghost                       | Vulnerable | `['ghost.io']` | `The thing you were looking for is no longer here, or never was` |
| 26. | Github                      | Vulnerable | `['github.io']` | `There isn't a GitHub Pages site here.` |
| 27. | Help Juice                  | Vulnerable | `['helpjuice.com']` | `We could not find what you're looking for` |
| 28. | Helprace                    | Vulnerable | `['helprace.com']` | `Admin of this Helprace account needs to set up domain alias` |
| 29. | Help Scout                  | Vulnerable | `['helpscoutdocs.com']` | `No settings were found for this company` |
| 30. | Heroku                      | Edge case  | `['herokuapp']` | `No such app` |
| 31. | Hubspot                     | Vulnerable | `['sites.hubspot.net']` | `Domain Not found` |
| 32. | Instapage                   | Vulnerable | `['pageserve.co', 'secure.pageserve.co', 'instapage.com']` | `You've Discovered A Missing Link. Our Apologies!` |
| 33. | InterCom                    | Vulnerable | `['custom.intercom.help']` | `<h1 class="headline"Uh oh. That page doesn't exist.</h1>` |
| 34. | JetBrains                   | Vulnerable | `['myjetbrains.com']` | `is not a registered InCloud YouTrack` |
| 35. | Kajabi                      | Vulnerable | `['endpoint.mykajabi.com']` | `<h1>The page you were looking for doesn't exist.</h1>` |
| 36. | Landingi                    | Vulnerable | `['cname.landingi.com']` | `<p>The page you are looking for is not found.</p>` |
| 37. | LaunchRock                  | Vulnerable | `['launchrock.com']` | `It looks like you may have taken a wrong turn somewhere. Don't worry...it happens to all of us.` |
| 38. | LeadPages.com               | Vulnerable | `['custom-proxy.leadpages.net', 'leadpages.net']` | `Double check that you have the right web address and give it another go!</p>` |
| 39. | Mashery                     | Edge Case  | `['mashery.com']` | `Unrecognized domain` |
| 40. | MicrosoftAzure              | Vulnerable | `['cloudapp.net', 'cloudapp.azure.com', 'azurewebsites.net', 'blob.core.windows.net', 'cloudapp.azure.com', 'azure-api.net', 'azurehdinsight.net', 'azureedge.net', 'azurecontainer.io', 'database.windows.net', 'azuredatalakestore.net', 'search.windows.net', 'azurecr.io', 'redis.cache.windows.net', 'azurehdinsight.net', 'servicebus.windows.net', 'visualstudio.com']` | `404 Web Site not found` |
| 41. | Ngrok                       | Vulnerable | `['ngrok.io']` | `ngrok.io not found` |
| 42. | Pantheon                    | Vulnerable | `['pantheonsite.io']` | `The gods are wise, but do not know of the site which you seek.` |
| 43. | Pingdom                     | Vulnerable | `['stats.pingdom.com']` | `This public report page has not been activated by the user` |
| 44. | Proposify                   | Vulnerable | `['proposify.biz']` | `If you need immediate assistance, please contact <a href="mailto:support@proposify.biz` |
| 45. | Readme.io                   | Vulnerable | `['readme.io']` | `Project doesnt exist... yet!` |
| 46. | ReadTheDocs.org             | Vulnerable | `['readthedocs.io']` | `is unknown to Read the Docs` |
| 47. | Shopify                     | Edge Case  | `['myshopify.com']` | `Sorry, this shop is currently unavailable` |
| 48. | SimpleBooklet               | Vulnerable | `['simplebooklet.com']` | `We can't find this <a href="https://simplebooklet.com` |
| 49. | Smartling                   | Vulnerable | `['smartling.com']` | `Domain is not configured` |
| 50. | Smugmug                     | Vulnerable | `['domains.smugmug.com']` |  |
| 51. | StatusPage                  | Vulnerable | `['statuspage.io']` | `You are being <a href="https://www.statuspage.io">redirected` |
| 52. | Strikingly                  | Vulnerable | `['.s.strikinglydns.com']` | `But if you're looking to build your own website,` |
| 53. | Surge.sh                    | Vulnerable | `['surge.sh']` | `project not found` |
| 54. | Surveygizmo                 | Vulnerable | `['privatedomain.sgizmo.com', 'privatedomain.surveygizmo.eu', 'privatedomain.sgizmoca.com']` | `data-html-name` |
| 55. | Tave                        | Vulnerable | `['clientaccess.tave.com']` | `<h1>Error 404: Page Not Found</h1>` |
| 56. | Teamwork                    | Vulnerable | `['teamwork.com']` | `Oops - We didn't find your site.` |
| 57. | Thinkific                   | Vulnerable | `['thinkific.com']` | `You may have mistyped the address or the page may have moved.` |
| 58. | Tictail                     | Vulnerable | `['domains.tictail.com']` | `to target URL: <a href="https://tictail.com` |
| 59. | Tilda                       | Edge Case  | `['tilda.ws']` | `Please renew your subscription` |
| 60. | Tumblr                      | Vulnerable | `['domains.tumblr.com']` | `Whatever you were looking for doesn't currently exist at this address` |
| 61. | Uberflip                    | Vulnerable | `['read.uberflip.com', 'uberflip.com']` | `Non-hub domain, The URL you've accessed does not provide a hub. Please check the URL and try again.` |
| 62. | Unbounce                    | Edge Case  | `['unbouncepages.com']` | `The requested URL was not found on this server` |
| 63. | UptimeRobot                 | Vulnerable | `['stats.uptimerobot.com']` | `This public status page <b>does not seem to exist</b>.` |
| 64. | UserVoice                   | Vulnerable | `['uservoice.com']` | `This UserVoice subdomain is currently available` |
| 65. | Vend                        | Vulnerable | `['vendecommerce.com']` | `Looks like you've traveled too far into cyberspace` |
| 66. | WebFlow                     | Vulnerable | `['proxy.webflow.com', 'proxy-ssl.webflow.com']` | `<p class="description">The page you are looking for doesn't exist or has been moved.</p>` |
| 67. | WishPond                    | Vulnerable | `['wishpond.com']` | `https://www.wishpond.com/404?campaign=true` |
| 68. | Worksites.net               | Vulnerable | `['NOT_AVAILABLE']` | `Hello! Sorry, but the website you&rsquo;re looking for doesn&rsquo;t exist.` |
| 69. | Wordpress                   | Vulnerable | `['wordpress.com']` | `Do you want to register ` |
| 70. | Zendesk                     | Not Vulnerable | `['zendesk.com']` | `Help Center Closed` |

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
* PayPal Email: `shrisatender@gmail.com` [**Please Don't Send Emails to This Address**]

## More Features Coming Soon...
                        
                        
