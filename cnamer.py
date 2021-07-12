import dns.resolver
import requests
from sys import argv
from art import *

tprint("C-NAMER")
print("           Coded by: Ahmed Tareq")

domains = open(argv[1], "r").read().splitlines()

for domain in domains :
    
    try :
    
        cname_domains = dns.resolver.resolve(domain, "CNAME")
        
        print(f"{domain} :")
        
        for cname_domain in cname_domains :
            
            name = cname_domain.target
            
            if "http://" not in name or "https://" not in name :
            
                name  = "http://" + str(name)
            
                try :
            
                    site = requests.get(name)
                
                    print(name + f"  ({site.status_code})")
            
                except requests.exceptions.SSLError :
                    import urllib3
                    
                    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                    
                    site = requests.get(name, verify=False)
                    
                    print(name + f"  ({site.status_code})")
            
            
        print("\n" + "#" * 50)
        
    except dns.resolver.NoAnswer :
    
        print(f"{domain} :")
        print("not found\n\n" + "#" * 50 + "\n")

        
        
