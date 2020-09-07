
'''
Item Order In Fingerprint Lists
===============================
	engine        
	status 
    cname    
	fingerprint

Available Fingerprints
======================
1. Acquia
2. Activecampaign
3. AfterShip
4. AgileCRM
5. Aha
6. Airee.ru
7. Anima
8. Apigee
9. AWS/S3      
10. Bigcartel
11. Bitbucket
12. Brightcove
13. Canny.io
14. CampaignMonitor
15. Cargo
16. CargoCollective
17. Cloudfront
18. Desk
19. ElasticBeanstalk_AWS_service
20. Fastly
21. Feedpress
22. Freshdesk
23. Frontify
24. GetResponse
25. Ghost
26. Github
27. Help Juice
28. Helprace
29. Help Scout
30. Heroku
31. Hubspot
32. Instapage
33. InterCom
34. JetBrains
35. Kajabi
36. Landingi
37. LaunchRock
38. LeadPages.com
39. Mashery
40. MicrosoftAzure
41. Ngrok
42. Pantheon
43. Pingdom
44. Proposify
45. Readme.io
46. ReadTheDocs.org
47. Shopify
48. SimpleBooklet
49. Smartling
50. Smugmug
51. StatusPage
52. Strikingly
53. Surge.sh
54. Surveygizmo
55. Tave
56. Teamwork
57. Thinkific
58. Tictail
59. Tilda
60. Tumblr
61. Uberflip
62. Unbounce
63. UptimeRobot
64. UserVoice
65. Vend
66. WebFlow
67. WishPond
68. Worksites.net
69. Wordpress
70. Zendesk
'''


f1 = [
	"Acquia", #Service
	"Vulnerable", #Status
        ["acquia-test.co"], #CNAME
	"The site you are looking for could not be found."  #Fingerprint
	]

f2 = [
	"ActiveCampaign",
	"Vulnerable",
        ["activehosted.com"],  
	"alt=\"LIGHTTPD - fly light.\""
	]
    
f3 = [
	"AfterShip",
	"Vulnerable",
        ["aftership.com"],  
	"Oops.</h2><p class=\"text-muted text-tight\">The page you're looking for doesn't exist."
	]
    
f4 = [
	"AgileCRM",
	"Vulnerable",
	["cname.agilecrm.com", "agilecrm.com"],
	"Sorry, this page is no longer available."
	]    

f5 = [
	"Aha",
	"Vulnerable",
        ["ideas.aha.io"],  
	"There is no portal here ... sending you back to Aha!"
	]
    
f6 = [
        "Airee.ru",
        "Vulnerable",
        ["cdn.airee.com", "airee.com"],
        "Ошибка 402. Сервис Айри.рф не оплачен"
        # "Сайт xyz.xyz.ru. , на который вы заходите, не оплатил сервис Айри.рф. Доступ к сайту временно невозможен."
	] 

f7 = [
        "Anima",
        "Vulnerable",
        ["NOT_AVAILABLE"],
        # "Missing Website"
        "If this is your website and you've just created it, try refreshing in a minute"
        # A record : 35.164.217.247
	]     

f8 = [
	"Apigee",
	"Vulnerable",
        ["-portal.apigee.net"],  
	""  #NoResponse_HenceNoFingerprint
	]   

f9 = [
	"AWS/S3",
	"Vulnerable",
        ["amazonaws"],  
	"The specified bucket does not exist"
	]      
    
f10 = [
	"Bigcartel",
	"Vulnerable",
        ["bigcartel.com"],
	"<h1>Oops! We could&#8217;t find that page.</h1>"
    ]

f11 = [
	"Bitbucket",
	"Vulnerable",
        ["bitbucket.io"],
	"Repository not found" 
	] 

f12 = [
	"Brightcove",
	"Vulnerable",
        ["bcvp0rtal.com", "brightcovegallery.com", "gallery.video"],
	"<p class=\"bc-gallery-error-code\">Error Code: 404</p>",
	]      

f13 = [
        "Canny.io",
        "Vulnerable",
        ["cname.canny.io"],
        # "Company Not Found"
        "There is no such company. Did you enter the right URL?"
	] 

f14 = [
	"CampaignMonitor",
	"Vulnerable",
        ["createsend.com", "name.createsend.com"], 
	"Double check the URL or <a href=\"mailto:help@createsend.com"
	]
    
f15 = [
	"Cargo",
	"Vulnerable",
        ["cargocollective.com"], 
	"If you're moving your domain away from Cargo you must make this configuration through your registrar's DNS control panel."
	]

f16 = [
	"CargoCollective",
	"Vulnerable",
        ["subdomain.cargocollective.com"], 
	"404 Not Found",
	]

f17 = [
	"Cloudfront",
	"Edge case ",
        ["cloudfront.net"],
	"Bad Request: ERROR: The request could not be satisfied",
	]    

f18 = [
	"Desk",
	"Not vulnerable",
        ["desk.com"],
	"Please try again or try Desk.com free for 14 days.",
	]
    
f19 = [
        "ElasticBeanstalk_AWS_service",
        "Vulnerable",
        ["elasticbeanstalk.com"],
        "" #No Fingerprint Available
    ]     

f20 = [
	"Fastly",
	"Edge case ",
        ["fastly.net"],
	"Fastly error: unknown domain:",
	]

f21 = [
	"Feedpress",
	"Vulnerable",
        ["redirect.feedpress.me"],
	"The feed has not been found."
	]
    
f22 = [
	"Freshdesk",
	"Vulnerable",  #NotSure
        ["freshdesk.com"],
	"May be this is still fresh!"
	] 

f23 = [
        "Frontify",
        "Vulnerable",
        ["frontify.com"],
        "404 - Page not found. Oops... look like you got lost."
	]     

f24 = [
	"GetResponse",
	"Vulnerable",
        [".gr8.com"],
	"With GetResponse Landing Pages, lead generation has never been easier"
	]

f25 = [
	"Ghost",
	"Vulnerable",
        ["ghost.io"],
	"The thing you were looking for is no longer here, or never was"
	]

f26 = [
	"Github",
	"Vulnerable",
        ["github.io"],
	"There isn't a GitHub Pages site here."
	]

f27 = [
	"Help Juice",
	"Vulnerable",
        ["helpjuice.com"],
	"We could not find what you're looking for"
	]

f28 = [
        "Helprace",
        "Vulnerable",
        ["helprace.com"],
        # "Alias not configured!"
        "Admin of this Helprace account needs to set up domain alias"
    ] 

f29 = [
	"Help Scout",
	"Vulnerable",
        ["helpscoutdocs.com"],
	"No settings were found for this company"
	]

f30 = [
	"Heroku",
	"Edge case ",
        ["herokuapp"],
	"No such app"
	]
    
f31 = [
        "Hubspot",
        "Vulnerable",   ##Not Sure
        ["sites.hubspot.net"],
        "Domain Not found",
	]      

f32 = [
	"Instapage",
	"Vulnerable",
        ["pageserve.co", "secure.pageserve.co", "https://instapage.com/"],
	"You've Discovered A Missing Link. Our Apologies!"
	]
    
f33 = [
	"InterCom",
	"Vulnerable",
        ["custom.intercom.help"],
	"<h1 class=\"headline\"Uh oh. That page doesn't exist.</h1>"
	]    

f34 = [
	"JetBrains",
	"Vulnerable",
        ["myjetbrains.com"],
	"is not a registered InCloud YouTrack"
	]

f35 = [
	"Kajabi",
	"Vulnerable",
        ["endpoint.mykajabi.com"],
	"<h1>The page you were looking for doesn't exist.</h1>"
	]

f36 = [
        "Landingi",
        "Vulnerable",
        ["cname.landingi.com"],
        # A Record : 174.129.25.170
        # "<h1>It looks like you’re lost...</h1>"
        "<p>The page you are looking for is not found.</p>"
    ] 

f37 = [
        "LaunchRock",
        "Vulnerable",
        ["launchrock.com"],
        "It looks like you may have taken a wrong turn somewhere. Don't worry...it happens to all of us."
	]   
""" 
LaunchRock
----------
A Record :
        54.243.190.28
        54.243.190.39
        54.243.190.47
        54.243.190.54
"""

f38 = [
        "LeadPages.com",
        "Vulnerable",
        ["custom-proxy.leadpages.net", "leadpages.net"],
        "Double check that you have the right web address and give it another go!</p>"
	] 
    
f39 = [
	"Mashery",
	"Edge Case ",
        ["mashery.com"],
	"Unrecognized domain"
	]    

f40 = [
	"MicrosoftAzure",
	"Vulnerable",  
        ["cloudapp.net", "cloudapp.azure.com", "azurewebsites.net", "blob.core.windows.net", "cloudapp.azure.com", "azure-api.net", "azurehdinsight.net", "azureedge.net", "azurecontainer.io", "database.windows.net", "azuredatalakestore.net", "search.windows.net", "azurecr.io", "redis.cache.windows.net", "azurehdinsight.net", "servicebus.windows.net", "visualstudio.com"],
	"404 Web Site not found"     
	]
    
f41 = [
        "Ngrok",
        "Vulnerable",
        ["ngrok.io"],
        "ngrok.io not found"
	]           

f42 = [
	"Pantheon",
	"Vulnerable",
        ["pantheonsite.io"],
	"The gods are wise, but do not know of the site which you seek."
	]
    
f43 = [
	"Pingdom",
	"Vulnerable",
        ["stats.pingdom.com"],
	"This public report page has not been activated by the user"
	]

f44 = [
	"Proposify",
	"Vulnerable",
        ["proposify.biz"],
	"If you need immediate assistance, please contact <a href=\"mailto:support@proposify.biz"
	]

f45 = [
	"Readme.io",
	"Vulnerable",
        ["readme.io"],
	"Project doesnt exist... yet!"
	] 

f46 = [
        "ReadTheDocs.org",
        "Vulnerable",
        ["readthedocs.io"],
        "is unknown to Read the Docs"
	]    

f47 = [
	"Shopify",
	"Edge Case ",
        ["myshopify.com"],
	"Sorry, this shop is currently unavailable"
	]

f48 = [
	"SimpleBooklet",
	"Vulnerable",
        ["simplebooklet.com"],
	"We can't find this <a href=\"https://simplebooklet.com"
	]
    
f49 = [
	"Smartling",
	"Vulnerable",
        ["smartling.com"],
	"Domain is not configured"
	]

f50 = [
	"Smugmug",
	"Vulnerable",
        ["domains.smugmug.com"],
	""  #NotAvailable
	]      

f51 = [
	"StatusPage",
	"Vulnerable",
        ["statuspage.io"],
	"You are being <a href=\"https://www.statuspage.io\">redirected"
	]

f52 = [
	"Strikingly",
	"Vulnerable",
        [".s.strikinglydns.com"],
	"But if you're looking to build your own website,"
	]

f53 = [
	"Surge.sh",
	"Vulnerable",
        ["surge.sh"],
	"project not found"
	]    

f54 = [
	"Surveygizmo",
	"Vulnerable",
        ["privatedomain.sgizmo.com", "privatedomain.surveygizmo.eu", "privatedomain.sgizmoca.com"],
	"data-html-name"
	] 

f55 = [
	"Tave",
	"Vulnerable",
        ["clientaccess.tave.com"],
	"<h1>Error 404: Page Not Found</h1>"
	]
    
f56 = [
	"Teamwork",
	"Vulnerable",
        ["teamwork.com"],
	"Oops - We didn't find your site."
	]

f57 = [
	"Thinkific",
	"Vulnerable",
        ["thinkific.com"],
	"You may have mistyped the address or the page may have moved."
	]

f58 = [
	"Tictail",
	"Vulnerable",
        ["domains.tictail.com"],
	"to target URL: <a href=\"https://tictail.com", "Start selling on Tictail."
	]

f59 = [
	"Tilda",
	"Edge Case ",
        ["tilda.ws"],
	"Please renew your subscription"
	]

f60 = [
	"Tumblr",
	"Vulnerable",
        ["domains.tumblr.com"],
	"Whatever you were looking for doesn't currently exist at this address"
	]    

f61 = [
        "Uberflip",
        "Vulnerable",
        ["read.uberflip.com", "uberflip.com"],
        "Non-hub domain, The URL you've accessed does not provide a hub. Please check the URL and try again."
	] 

f62 = [
	"Unbounce",
	"Edge Case ",
        ["unbouncepages.com"],
	"The requested URL was not found on this server"
	]

f63 = [
	"UptimeRobot",
	"Vulnerable",
        ["stats.uptimerobot.com"],
	"This public status page <b>does not seem to exist</b>."
	]

f64 = [
	"UserVoice",
	"Vulnerable",
        ["uservoice.com"],
	"This UserVoice subdomain is currently available"
	]

f65 = [
	"Vend",
	"Vulnerable",
        ["vendecommerce.com"],
	"Looks like you've traveled too far into cyberspace"
	]
    
f66 = [
	"WebFlow",
	"Vulnerable",
        ["proxy.webflow.com", "proxy-ssl.webflow.com"],
	"<p class=\"description\">The page you are looking for doesn't exist or has been moved.</p>"
	]

f67 = [
	"WishPond",
	"Vulnerable",
        ["wishpond.com"],
	"https://www.wishpond.com/404?campaign=true"
	]
    
f68 = [
        "Worksites.net",
        "Vulnerable",
        ["NOT_AVAILABLE"],
        "Hello! Sorry, but the website you&rsquo;re looking for doesn&rsquo;t exist."
        ## A Record IP ==> 69.164.223.206
	]       
    

f69 = [
	"Wordpress",
	"Vulnerable",
        ["wordpress.com"],
	"Do you want to register "
	]    

f70 = [
	"Zendesk",
	"Not Vulnerable",
        ["zendesk.com"],
	"Help Center Closed"
	]
      

"""
Kinsta
Edge Case
[""]
""
# Here is the response from kinsta for orphan CNAME.
# 404 Not Found
# Content-Length=[33604]
# Server = kinsta-nginx

"""     

fingerprints_list = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,f27,f28,f29,f30,f31,f32,f33,f34,f35,f36,f37,f38,f39,f40,f41,f42,f43,f44,f45,f46,f47,f48,f49,f50,f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65,f66,f67,f68,f69,f70]
