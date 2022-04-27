
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
71. Appery.io
72. Vercel.com
73. Datocms.com
74. Jazzhr
75. Kinsta
76. Smartjob
77. Wufoo
78. Wix
79. Sprintful 
80. Pagewiz
81. short-io
82. Netlify
83. Gitbook
84. Flywheel
85. Announcekit
86. Flexbe
87. Gemfury
88. Hatenablog
'''

fingerprints_list = [
    [
        "Acquia", #Service
        "Vulnerable", #Status
        ["acquia-test.co"], #CNAME
        "The site you are looking for could not be found."  #Fingerprint
    ],

    [
        "ActiveCampaign",
        "Vulnerable",
        ["activehosted.com"],  
        "alt=\"LIGHTTPD - fly light.\""
    ],
    
    [
        "AfterShip",
        "Vulnerable",
        ["aftership.com"],  
        "Oops.</h2><p class=\"text-muted text-tight\">The page you're looking for doesn't exist."
    ],
    
    [
        "AgileCRM",
        "Vulnerable",
        ["cname.agilecrm.com", "agilecrm.com"],
        "Sorry, this page is no longer available."
    ],    

    [
        "Aha",
        "Vulnerable",
        ["ideas.aha.io"],  
        "There is no portal here ... sending you back to Aha!"
    ],
    
    [
        "Airee.ru",
        "Vulnerable",
        ["cdn.airee.com", "airee.com"],
        "Ошибка 402. Сервис Айри.рф не оплачен"
        # "Сайт xyz.xyz.ru. , на который вы заходите, не оплатил сервис Айри.рф. Доступ к сайту временно невозможен."
    ], 

    [
        "Anima",
        "Vulnerable",
        ["NOT_AVAILABLE"],
        # "Missing Website"
        "If this is your website and you've just created it, try refreshing in a minute"
        # A record : 35.164.217.247
    ],     

    [
        "Apigee",
        "Vulnerable",
        ["-portal.apigee.net"],  
        ""  #NoResponse_HenceNoFingerprint
    ],   

    [
        "AWS/S3",
        "Vulnerable",
        ["amazonaws"],  
        "The specified bucket does not exist"
    ],      
    
    [
        "Bigcartel",
        "Vulnerable",
        ["bigcartel.com"],
        "<h1>Oops! We could&#8217;t find that page.</h1>"
    ],

    [
        "Bitbucket",
        "Vulnerable",
        ["bitbucket.io"],
        "Repository not found" 
    ], 

    [
        "Brightcove",
        "Vulnerable",
        ["bcvp0rtal.com", "brightcovegallery.com", "gallery.video"],
        "<p class=\"bc-gallery-error-code\">Error Code: 404</p>",
    ],      

    [
        "Canny.io",
        "Vulnerable",
        ["cname.canny.io"],
        # "Company Not Found"
        "There is no such company. Did you enter the right URL?"
    ], 

    [
     
        "CampaignMonitor",
        "Vulnerable",
        ["createsend.com", "name.createsend.com"], 
        "Double check the URL or <a href=\"mailto:help@createsend.com"
    ],
    
    [
        "Cargo",
        "Vulnerable",
        ["cargocollective.com"], 
        "If you're moving your domain away from Cargo you must make this configuration through your registrar's DNS control panel."
    ],

    [
        "CargoCollective",
        "Vulnerable",
        ["subdomain.cargocollective.com"], 
        "404 Not Found"
    ],

    [
        "Cloudfront",
        "Edge case ",
        ["cloudfront.net"],
        "Bad Request: ERROR: The request could not be satisfied"
    ],    

    [
        "Desk",
        "Not vulnerable",
        ["desk.com"],
        "Please try again or try Desk.com free for 14 days."
    ],
    
    [
        "ElasticBeanstalk_AWS_service",
        "Vulnerable",
        ["elasticbeanstalk.com"],
        "" #No Fingerprint Available
    ],     

    [
        "Fastly",
        "Edge case ",
        ["fastly.net"],
        "Fastly error: unknown domain:"
    ],

    [
        "Feedpress",
        "Vulnerable",
        ["redirect.feedpress.me"],
        "The feed has not been found."
    ],
    
    [
        "Freshdesk",
        "Vulnerable",  #NotSure
        ["freshdesk.com"],
        "May be this is still fresh!"
    ], 

    [
        "Frontify",
        "Vulnerable",
        ["frontify.com"],
        "404 - Page Not Found</h1>"
    ],     

    [
        "GetResponse",
        "Vulnerable",
        [".gr8.com"],
        "With GetResponse Landing Pages, lead generation has never been easier"
    ],

    [
        "Ghost",
        "Vulnerable",
        ["ghost.io"],
        "The thing you were looking for is no longer here, or never was"
    ],

    [
        "Github",
        "Vulnerable",
        ["github.io"],
        "There isn't a GitHub Pages site here."
    ],

    [
        "Help Juice",
        "Vulnerable",
        ["helpjuice.com"],
        "We could not find what you're looking for"
    ],

    [
        "Helprace",
        "Vulnerable",
        ["helprace.com"],
        # "Alias not configured!"
        "Admin of this Helprace account needs to set up domain alias"
    ], 

    [
        "Help Scout",
        "Vulnerable",
        ["helpscoutdocs.com"],
        "No settings were found for this company"
    ],

    [
        "Heroku",
        "Edge case ",
        ["herokuapp"],
        "No such app"
    ],
    
    [
        "Hubspot",
        "Vulnerable",   ##Not Sure
        ["sites.hubspot.net"],
        "Domain Not found"
    ],      

    [
        "Instapage",
        "Vulnerable",
        ["pageserve.co", "secure.pageserve.co", "https://instapage.com/"],
        "You've Discovered A Missing Link. Our Apologies!"
    ],
    
    [
        "InterCom",
        "Vulnerable",
        ["custom.intercom.help"],
        "<h1 class=\"headline\"Uh oh. That page doesn't exist.</h1>"
    ],    

    [
        "JetBrains",
        "Vulnerable",
        ["myjetbrains.com"],
        "is not a registered InCloud YouTrack"
    ],

    [
        "Kajabi",
        "Vulnerable",
        ["endpoint.mykajabi.com"],
        "<h1>The page you were looking for doesn't exist.</h1>"
    ],

    [
        "Landingi",
        "Vulnerable",
        ["cname.landingi.com"],
        # A Record : 174.129.25.170
        # "<h1>It looks like you’re lost...</h1>"
        "<p>The page you are looking for is not found.</p>"
    ], 

    [
        "LaunchRock",
        "Vulnerable",
        ["launchrock.com"],
        "It looks like you may have taken a wrong turn somewhere. Don't worry...it happens to all of us."
    ],  

# LaunchRock
# ----------
# A Record :
#         54.243.190.28
#         54.243.190.39
#         54.243.190.47
#         54.243.190.54


    [
        "LeadPages.com",
        "Vulnerable",
        ["custom-proxy.leadpages.net", "leadpages.net"],
        "Double check that you have the right web address and give it another go!</p>"
    ], 
    
    [
        "Mashery",
        "Edge Case ",
        ["mashery.com"],
        "Unrecognized domain"
    ],    

    [
        "MicrosoftAzure",
        "Vulnerable",  
        ["cloudapp.net", "cloudapp.azure.com", "azurewebsites.net", "blob.core.windows.net", "cloudapp.azure.com", "azure-api.net", "azurehdinsight.net", "azureedge.net", "azurecontainer.io", "database.windows.net", "azuredatalakestore.net", "search.windows.net", "azurecr.io", "redis.cache.windows.net", "azurehdinsight.net", "servicebus.windows.net", "visualstudio.com"],
        "404 Web Site not found"     
    ],
    
    [
        "Ngrok",
        "Vulnerable",
        ["ngrok.io"],
        "ngrok.io not found"
    ],           

    [
        "Pantheon",
        "Vulnerable",
        ["pantheonsite.io"],
        "The gods are wise, but do not know of the site which you seek."
    ],
    
    [
        "Pingdom",
        "Vulnerable",
        ["stats.pingdom.com"],
        "This public report page has not been activated by the user"
    ],

    [
        "Proposify",
        "Vulnerable",
        ["proposify.biz"],
        "If you need immediate assistance, please contact <a href=\"mailto:support@proposify.biz"
    ],

    [
        "Readme.io",
        "Vulnerable",
        ["readme.io"],
        "Project doesnt exist... yet!"
    ], 

    [
        "ReadTheDocs.org",
        "Vulnerable",
        ["readthedocs.io"],
        "is unknown to Read the Docs"
    ],    

    [
        "Shopify",
        "Edge Case ",
        ["myshopify.com"],
        "Sorry, this shop is currently unavailable"
    ],

    [
        "SimpleBooklet",
        "Vulnerable",
        ["simplebooklet.com"],
        "We can't find this <a href=\"https://simplebooklet.com"
    ],
    
    [
        "Smartling",
        "Vulnerable",
        ["smartling.com"],
        "Domain is not configured"
    ],

    [
        "Smugmug",
        "Vulnerable",
        ["domains.smugmug.com"],
        ""  #NotAvailable
    ],     

    [
        "StatusPage",
        "Vulnerable",
        ["statuspage.io"],
        "You are being <a href=\"https://www.statuspage.io\">redirected"
    ],

    [
        "Strikingly",
        "Vulnerable",
        [".s.strikinglydns.com"],
        "But if you're looking to build your own website,"
    ],

    [
        "Surge.sh",
        "Vulnerable",
        ["surge.sh"],
        "project not found"
    ],    

    [
        "Surveygizmo",
        "Vulnerable",
        ["privatedomain.sgizmo.com", "privatedomain.surveygizmo.eu", "privatedomain.sgizmoca.com"],
        "data-html-name"
    ], 

    [
        "Tave",
        "Vulnerable",
        ["clientaccess.tave.com"],
        "<h1>Error 404: Page Not Found</h1>"
    ],
    
    [
        "Teamwork",
        "Vulnerable",
        ["teamwork.com"],
        "Oops - We didn't find your site."
    ],

    [
        "Thinkific",
        "Vulnerable",
        ["thinkific.com"],
        "You may have mistyped the address or the page may have moved."
    ],

    [
        "Tictail",
        "Vulnerable",
        ["domains.tictail.com"],
        "to target URL: <a href=\"https://tictail.com", "Start selling on Tictail."
    ],

    [
        "Tilda",
        "Edge Case ",
        ["tilda.ws"],
        "Please renew your subscription"
    ],

    [
        "Tumblr",
        "Vulnerable",
        ["domains.tumblr.com"],
        "Whatever you were looking for doesn't currently exist at this address"
    ],    

    [
        "Uberflip",
        "Vulnerable",
        ["read.uberflip.com", "uberflip.com"],
        "Non-hub domain, The URL you've accessed does not provide a hub. Please check the URL and try again."
    ], 

    [
        "Unbounce",
        "Edge Case ",
        ["unbouncepages.com"],
        "The requested URL was not found on this server"
    ],

    [
        "UptimeRobot",
        "Vulnerable",
        ["stats.uptimerobot.com"],
        "This public status page <b>does not seem to exist</b>."
    ],

    [
        "UserVoice",
        "Vulnerable",
        ["uservoice.com"],
        "This UserVoice subdomain is currently available"
    ],

    [
        "Vend",
        "Vulnerable",
        ["vendecommerce.com"],
        "Looks like you've traveled too far into cyberspace"
    ],
    
    [
        "WebFlow",
        "Vulnerable",
        ["proxy.webflow.com", "proxy-ssl.webflow.com"],
        "<p class=\"description\">The page you are looking for doesn't exist or has been moved.</p>"
    ],

    [
        "WishPond",
        "Vulnerable",
        ["wishpond.com"],
        "https://www.wishpond.com/404?campaign=true"
    ],
    
    [
        "Worksites.net",
        "Vulnerable",
        ["NOT_AVAILABLE"],
        "Hello! Sorry, but the website you&rsquo;re looking for doesn&rsquo;t exist."
        ## A Record IP ==> 69.164.223.206
    ],       
    

    [
        "Wordpress",
        "Vulnerable",
        ["wordpress.com"],
        "Do you want to register "
    ],   

    [
        "Zendesk",
        "Not Vulnerable",
        ["zendesk.com"],
        "Help Center Closed"
    ],
 
    [
        "Appery.io",
        "Vulnerable",
        [""],  #404 Cname
        "<p>This page will be updated automatically when your app is published.</p>",
        # Pointing to 107.20.248.61
    ],
 
    [
        "Vercel.com",
        "Vulnerable",
        [""], #404 Cname
        "The deployment could not be found on Vercel."
    ],
   
    [
        "Datocms.com",
        "Vulnerable",
        [""], #404 Cname
        "<!doctype html><html><head><meta charset=\"utf-8\"><title>Loading...</title>",
    ],    

# Kinsta
# Edge Case
# [""]
# ""
# # Here is the response from kinsta for orphan CNAME.
# # 404 Not Found
# # Content-Length=[33604]
# # Server = kinsta-nginx   

    [
        "Jazzhr",
        "Edge Case",
        ["jazzhr.com"],
        "This account no longer active"
    ],

    [
        "Kinsta",
        "Vulnerable",
        ["kinsta.com"],
        "No Site For Domain"
    ],

    [
        "Smartjob",
        "Vulnerable",
        ["smartjobboard.com", "mysmartjobboard.com"],
        "This job board website is either expired or its domain name is invalid"
    ],

    [
        "Wufoo",
        "Vulnerable",
        ["www.wufoo.com", "subdomain.wufoo.com", "hello.wufoo.com", "pizzapalace.wufoo.com"],
        "Hmmm....something is not right."
    ],

    [
        "Wix",
        "Vulnerable",
        ["wixdns.net"],
        "Error ConnectYourDomain occurred"
    ],

    [
        "Sprintful",
        "Vulnerable",
        ["proxy.sprintful.com", "cname.sprintful.com", "sprintful.com"],
        "This domain name does not have a default page configured."
    ],

    [
        "Short-io",
        "Vulnerable",
        ["cname.short.io"],
        "This domain is not configured on Short.io"
    ],

    [
        "Pagewiz",
        "Vulnerable",
        ["s1.pagewiz.net"],
        "pagewiz"
    ],

    [
        "Netlify",
        "Edge case",
        ["cname.netlify.app", "cname.netlify.com", "netlify.com", "netlify.app"],
        "Not found - Request ID:"
    ],

    [
        "Gitbook",
        "Vulnerable",
        ["gitbook.io"],
        "Domain not found"
    ],

    [
        "Flywheel",
        "vulnerable",
        ["getflywheel.com"],
        "We're sorry, you've landed on a page that is hosted by Flywheel"
    ],

    [
        "Announcekit",
        "Vulnerable",
        ["cname.announcekit.app"],
        "Error 404 - AnnounceKit"
    ],

    [
        "Flexbe",
        "Edge Case",
        ["flexbe.com"],
        "flexbe"
    ],

    [
        "Gemfury",
        "Vulnerable",
        ["furyns.com"],
        "404: This page could not be found.",
    ],

    [
        "Hatenablog",
        "Vulnerable",
        ["hatenablog.com"],
        "404 Blog is not found"
    ],
]

 