import requests, json
import sys
from colorama import init, Fore
init(autoreset=True)
bold = '\033[01m'
print (Fore.RED+"""
               _________________________________        		                    
              |                                 |	
              |                                 |
                           BORDELIQUE                                      	
              |                                 |		
              |_________________________________|		
		                                                  
                                                              v1.0
                                                   CREATED By WALIDBORDELIQUE :)
""")
print(Fore.GREEN+bold+"(1) IP ADDRESS ")
print(Fore.GREEN+bold+"(2) IP IP ADDRESS INFO")
print(Fore.GREEN+bold+"(3) Phone Number Info ")
print(Fore.GREEN+bold+"(4) Email INFO ")
print(Fore.GREEN+bold+"(5) Exit ")
inpt = str(input(Fore.RED+"[+] " ))
info = (Fore.RED+bold+ "GETTING INFO....."+bold)
if inpt == "1":
  print("*If this field remains empty it will show your geolocation!")
  ip = str(input(Fore.BLUE+ "ENTER THE IP : "))
  api = "http://ip-api.com/json/"
  print(info)
  try:
    data = requests.get(api+ip).json()	
    print(Fore.WHITE+bold+ "Result :",data['status'])
    print(Fore.WHITE+bold+"ISP :",data['isp'])
    print(Fore.WHITE+bold+"City :",data['city'])
    print(Fore.WHITE+bold+"Region :",data['regionName'])
    print(Fore.WHITE+bold+"Country :",data['country'])
    print(Fore.WHITE+bold+"Country Code :",data['countryCode'])
    print(Fore.WHITE+bold+"Postal :",data['zip'])
    print(Fore.WHITE+bold+"Timezone :",data['timezone'])
  except requests.exceptions.ConnectionError as e:
    print (Fore.RED+bold+"Please check your internet connection!")
  except:
    print (Fore.RED+bold+"PLEASE TRY AGAIN")
elif inpt == "2":
  api = "http://ip-api.com/json/"
  print(info)
  try:
    data = requests.get(api).json()	
    print(Fore.WHITE+bold+ "Result :",data['status'])
    print(Fore.WHITE+bold+"ISP :",data['isp'])
    print(Fore.WHITE+bold+"City :",data['city'])
    print(Fore.WHITE+bold+"Region :",data['regionName'])
    print(Fore.WHITE+bold+"Country :",data['country'])
    print(Fore.WHITE+bold+"Country Code :",data['countryCode'])
    print(Fore.WHITE+bold+"Postal :",data['zip'])
    print(Fore.WHITE+bold+"Timezone :",data['timezone'])
           
  except requests.exceptions.ConnectionError as e:
    print(Fore.RED+bold+"Please check your internet connection!")
  except:
    print (Fore.RED+bold+"PLEASE TRY AGAIN")
elif inpt == "3":
  print("*Use upper case for country code!") 
  code = str(input(Fore.BLUE+ "ENTER COUNTRY CODE : ")) 
  number = (input("ENTER THE NUMBER : "))
  api = "http://apilayer.net/api/validate?access_key=62cc0533d5b4f9966528d3c104353993&number="
  mid = "&country_code="
  last = "&format=1"
  print(info)
  try:
    data = requests.get(api+number+mid+code+last).json()
    print(Fore.WHITE+bold+"Operation STATUS :",data['valid'])
    print(Fore.WHITE+bold+"Prifix :",data['country_prefix'])
    print(Fore.WHITE+bold+"Country Code :",data['country_code'])
    print(Fore.WHITE+bold+"Country Name :",data['country_name'])
    print(Fore.WHITE+bold+"Region :",data['location'])
    print(Fore.WHITE+bold+"Carrier :",data['carrier'])
    print(Fore.WHITE+bold+"Line Type :",data['line_type'])
  except requests.exceptions.ConnectionError as e:
    print(Fore.RED+bold+"Please check your internet connection!")
  except:
    print (Fore.RED+bold+"PLEASE TRY AGAIN")

elif inpt == "4":
  inp = (input(Fore.BLUE+bold+"ENTER THE EMAIL : "))
  api3 = "http://apilayer.net/api/check?access_key=5ff3c15f0f2d9227a166ed95b051d83f"
  api3l = "&email="
  print(info)
  try:
    data = requests.get(api3+api3l+inp).json()
    print(Fore.WHITE+"Email : ",data ['email'])
    print(Fore.WHITE+bold+"User :",data['user'])
    print(Fore.WHITE+bold+"Domain :",data['domain'])
    print(Fore.WHITE+bold+"Format :",data['format_valid'])
    print(Fore.WHITE+bold+"SMTP :",data['smtp_check'])
  except requests.exceptions.ConnectionError as e:
    print(Fore.RED+bold+"Please check your internet connection!")
  except:
    print (Fore.RED+bold+"PLEASE TRY AGAIN")

if inpt == "5":
  print(Fore.RED+"Exiting...")
  sys.exit()
