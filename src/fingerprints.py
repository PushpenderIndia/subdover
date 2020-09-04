
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
4. Aha
5. Apigee
6. AWS/S3      
7. Bigcartel
8. Bitbucket
9. Brightcove
10. CampaignMonitor
11. Cargo
12. CargoCollective
13. Cloudfront
14. Desk
15. Fastly
16. Feedpress
17. Freshdesk
18. GetResponse
19. Ghost
20. Github
21. Help Juice
22. Help Scout
23. Heroku
24. Instapage
25. InterCom
26. JetBrains
27. Kajabi
28. Mashery
29. MicrosoftAzure
30. Pantheon
31. Pingdom
32. Proposify
33. Readme.io
34. Shopify
35. SimpleBooklet
36. Smartling
37. Smugmug
38. StatusPage
39. Strikingly
40. Surge.sh
41. Surveygizmo
42. Tave
43. Teamwork
44. Thinkific
45. Tictail
46. Tilda
47. Tumblr
48. Unbounce
49. UptimeRobot
50. UserVoice
51. Vend
52. WebFlow
53. WishPond
54. Wordpress
55. Zendesk
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
		"Aha",
		"Vulnerable",
        ["ideas.aha.io"],  
		"There is no portal here ... sending you back to Aha!"
	]

f5 = [
		"Apigee",
		"Vulnerable",
        ["-portal.apigee.net"],  
		""  #NoResponse_HenceNoFingerprint
	]   

f6 = [
		"AWS/S3",
		"Vulnerable",
        ["amazonaws"],  
		"The specified bucket does not exist"
	]      
    
f7 = [
		"Bigcartel",
		"Vulnerable",
        ["bigcartel.com"],
		"<h1>Oops! We could&#8217;t find that page.</h1>"
    ]

f8 = [
		"Bitbucket",
		"Vulnerable",
        ["bitbucket.io"],
		"Repository not found",

    ] 

f9 = [
		"Brightcove",
		"Vulnerable",
        ["bcvp0rtal.com", "brightcovegallery.com", "gallery.video"],
		"<p class=\"bc-gallery-error-code\">Error Code: 404</p>",

    ]      

f10 = [
		"CampaignMonitor",
		"Vulnerable",
        ["createsend.com", "name.createsend.com"], 
		"Double check the URL or <a href=\"mailto:help@createsend.com"
	]
    
f11 = [
		"Cargo",
		"Vulnerable",
        ["cargocollective.com"], 
		"If you're moving your domain away from Cargo you must make this configuration through your registrar's DNS control panel."
	]

f12 = [
		"CargoCollective",
		"Vulnerable",
        ["subdomain.cargocollective.com"], 
		"404 Not Found",
	]

f13 = [
		"Cloudfront",
		"Edge case ",
        ["cloudfront.net"],
		"Bad Request: ERROR: The request could not be satisfied",
	]    

f14 = [
		"Desk",
		"Not vulnerable",
        ["desk.com"],
		"Please try again or try Desk.com free for 14 days.",
	]

f15 = [
		"Fastly",
		"Edge case ",
        ["fastly.net"],
		"Fastly error: unknown domain:",
	]

f16 = [
		"Feedpress",
		"Vulnerable",
        ["redirect.feedpress.me"],
		"The feed has not been found."
	]
    
f17 = [
		"Freshdesk",
		"Vulnerable",  #NotSure
        ["freshdesk.com"],
		"May be this is still fresh!"
	]    

f18 = [
		"GetResponse",
		"Vulnerable",
        [".gr8.com"],
		"With GetResponse Landing Pages, lead generation has never been easier"
	]

f19 = [
		"Ghost",
		"Vulnerable",
        ["ghost.io"],
		"The thing you were looking for is no longer here, or never was"
	]

f20 = [
		"Github",
		"Vulnerable",
        ["github.io"],
		"There isn't a GitHub Pages site here."
	]

f21 = [
		"Help Juice",
		"Vulnerable",
        ["helpjuice.com"],
		"We could not find what you're looking for"
	]

f22 = [
		"Help Scout",
		"Vulnerable",
        ["helpscoutdocs.com"],
		"No settings were found for this company"
	]

f23 = [
		"Heroku",
		"Edge case ",
        ["herokuapp"],
		"No such app"
	]

f24 = [
		"Instapage",
		"Vulnerable",
        ["pageserve.co", "secure.pageserve.co", "https://instapage.com/"],
		"You've Discovered A Missing Link. Our Apologies!"
	]
    
f25 = [
		"InterCom",
		"Vulnerable",
        ["custom.intercom.help"],
		"<h1 class=\"headline\"Uh oh. That page doesn't exist.</h1>"
	]    

f26 = [
		"JetBrains",
		"Vulnerable",
        ["myjetbrains.com"],
		"is not a registered InCloud YouTrack"
	]

f27 = [
		"Kajabi",
		"Vulnerable",
        ["endpoint.mykajabi.com"],
		"<h1>The page you were looking for doesn't exist.</h1>"
	]
    
f28 = [
		"Mashery",
		"Edge Case ",
        ["mashery.com"],
		"Unrecognized domain"
	]    

f29 = [
		"MicrosoftAzure",
		"Vulnerable",
        [".azurewebsites.net", ".cloudapp.net", ".cloudapp.azure.com", ".trafficmanager.net", ".blob.core.windows.net", ".azure-api.net", ".azurehdinsight.net", ".azureedge.net"],
		"404 Web Site not found"     
	]

f30 = [
		"Pantheon",
		"Vulnerable",
        ["pantheonsite.io"],
		"The gods are wise, but do not know of the site which you seek."
	]
    
f31 = [
		"Pingdom",
		"Vulnerable",
        ["stats.pingdom.com"],
		"This public report page has not been activated by the user"
	]

f32 = [
		"Proposify",
		"Vulnerable",
        ["proposify.biz"],
		"If you need immediate assistance, please contact <a href=\"mailto:support@proposify.biz"
	]

f33 = [
		"Readme.io",
		"Vulnerable",
        ["readme.io"],
		"Project doesnt exist... yet!"
	]    

f34 = [
		"Shopify",
		"Edge Case ",
        ["myshopify.com"],
		"Sorry, this shop is currently unavailable"
	]

f35 = [
		"SimpleBooklet",
		"Vulnerable",
        ["simplebooklet.com"],
		"We can't find this <a href=\"https://simplebooklet.com"
	]
    
f36 = [
		"Smartling",
		"Vulnerable",
        ["smartling.com"],
		"Domain is not configured"
	]

f37 = [
		"Smugmug",
		"Vulnerable",
        ["domains.smugmug.com"],
		""  #NotAvailable
    ]      

f38 = [
		"StatusPage",
		"Vulnerable",
        ["statuspage.io"],
		"You are being <a href=\"https://www.statuspage.io\">redirected"
	]

f39 = [
		"Strikingly",
		"Vulnerable",
        [".s.strikinglydns.com"],
		"But if you're looking to build your own website,"
	]

f40 = [
		"Surge.sh",
		"Vulnerable",
        ["surge.sh"],
		"project not found"
	]    

f41 = [
		"Surveygizmo",
		"Vulnerable",
        ["privatedomain.sgizmo.com", "privatedomain.surveygizmo.eu", "privatedomain.sgizmoca.com"],
		"data-html-name"
	] 

f42 = [
		"Tave",
		"Vulnerable",
        ["clientaccess.tave.com"],
		"<h1>Error 404: Page Not Found</h1>"
	]
    
f43 = [
		"Teamwork",
		"Vulnerable",
        ["teamwork.com"],
		"Oops - We didn't find your site."
	]

f44 = [
		"Thinkific",
		"Vulnerable",
        ["thinkific.com"],
		"You may have mistyped the address or the page may have moved."
	]

f45 = [
		"Tictail",
		"Vulnerable",
        ["domains.tictail.com"],
		"to target URL: <a href=\"https://tictail.com", "Start selling on Tictail."
	]

f46 = [
		"Tilda",
		"Edge Case ",
        ["tilda.ws"],
		"Please renew your subscription"
	]

f47 = [
		"Tumblr",
		"Vulnerable",
        ["domains.tumblr.com"],
		"Whatever you were looking for doesn't currently exist at this address"
	]    

f48 = [
		"Unbounce",
		"Edge Case ",
        ["unbouncepages.com"],
		"The requested URL was not found on this server"
	]

f49 = [
		"UptimeRobot",
		"Vulnerable",
        ["stats.uptimerobot.com"],
		"This public status page <b>does not seem to exist</b>."
	]

f50 = [
		"UserVoice",
		"Vulnerable",
        ["uservoice.com"],
		"This UserVoice subdomain is currently available"
	]

f51 = [
		"Vend",
		"Vulnerable",
        ["vendecommerce.com"],
		"Looks like you've traveled too far into cyberspace"
	]
    
f52 = [
		"WebFlow",
		"Vulnerable",
        ["proxy.webflow.com", "proxy-ssl.webflow.com"],
		"<p class=\"description\">The page you are looking for doesn't exist or has been moved.</p>"
	]

f53 = [
		"WishPond",
		"Vulnerable",
        ["wishpond.com"],
		"https://www.wishpond.com/404?campaign=true"
	]

f54 = [
		"Wordpress",
		"Vulnerable",
        ["wordpress.com"],
		"Do you want to register "
	]    

f55 = [
		"Zendesk",
		"Not Vulnerable",
        ["zendesk.com"],
		"Help Center Closed"
	]
    

    
"""
Newly Added Fingerprints
""" 

f56 = [
        "Hubspot",
        "Vulnerable",   ##Not Sure
        ["sites.hubspot.net"],
        "Domain Not found",
    ]    

f57 = [
        "ReadTheDocs.org",
        "Vulnerable",
        ["readthedocs.io"],
        "is unknown to Read the Docs"
    ] 

f58 = [
        "LeadPages.com",
        "Vulnerable",
        ["custom-proxy.leadpages.net", "leadpages.net"],
        "Double check that you have the right web address and give it another go!</p>"
    ] 

f59 = [
        "Worksites.net",
        "Vulnerable",
        ["NOT_AVAILABLE"],
        "Hello! Sorry, but the website you&rsquo;re looking for doesn&rsquo;t exist."
        ## A Record IP ==> 69.164.223.206
    ] 

f60 = [
        "AgileCRM",
        "Vulnerable",
        ["cname.agilecrm.com", "agilecrm.com"],
        "Sorry, this page is no longer available."
    ] 

f61 = [
        "ElasticBeanstalk_AWS_service",
        "Vulnerable",
        ["elasticbeanstalk.com"],
        "" #No Fingerprint Available
    ] 

f62 = [
        "Uberflip",
        "Vulnerable",
        ["read.uberflip.com", "uberflip.com"],
        "Non-hub domain, The URL you've accessed does not provide a hub. Please check the URL and try again."
    ]     
    

fingerprints_list = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,f27,f28,f29,f30,f31,f32,f33,f34,f35,f36,f37,f38,f39,f40,f41,f42,f43,f44,f45,f46,f47,f48,f49,f50,f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62]