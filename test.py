'''import pydig
from urllib.parse import urlparse
def get_dns_query(url):
    try:
        if "http://"or "https://" not in url:
            url = "https://" + url
        domain=urllib.url.parse.urlparse(url).hostname
        result=pydig.query(domain,"A")
        whitelist=['amazon.com','google.com','Facebook.com','paypal.com','salesforce.com','rakuten.com']
        for i in whitelist:
            i="https://"+i
            if final_features.typosquat(i)==1:
                domain_from_the_list=urllib.url.parse.urlparse(i)
                result1=pydig.query(domain_from_the_list,"A")
            out1=result1.to_text()
            out=result.to_text()
            if final_features.typosquat(i)==0:
                return 0
            if out == out1:
                return 0
            else:
                return 1
    except:
        return 1

def main():
    url=input("enter the url:")
    a=get_dns_query(url)
    print(a)
    
if __name__ == "__main__":
    main()'''
from bs4 import BeautifulSoup
import requests
import final_features
import urllib
def formcount(url):

    try:
        response2=requests.get(url)
        whitelist=['amazon.com','google.com','Facebook.com','paypal.com','salesforce.com','rakuten.com']
        if final_features.typosquat(url)==1:

            for i in whitelist:
                whitelist_url="https://"+i
                response1=requests.get(whitelist_url)
                soup1=BeautifulSoup(response1.text,'html.parser')
                soup2=BeautifulSoup(response2.text,'html.parser')

                forms1=soup1.find_all('form')
                forms2=soup2.find_all('form')
                for form1 in forms1:
                    countofgood=countofgood+1
                for form2 in forms2:
                    countofbad=countofbad+1
                if countofgood == countofbad:
                    return 0
                else:
                    return 1
    except:
        return 1







import dns.resolver
import requests 

def virustotal(url):
     address=dns.resolver.resolve(url, 'A')
     api= f"https://www.virustotal.com/api/v3/ip_addresses/{address[0]}"
     headers={
        "accept": "application/json",
        "x-apikey": "9cef20c75ef022621d4437ed41c6bc267e5cf2020b2001c41c3b180020377628"
     }
     response = requests.get(api, headers=headers)
     return response.json()


answer=virustotal("google.com")
print(answer)

i have to get this access 
'last_https_certificate': {'cert_signature': {'signature_algorithm': 'sha256RSA', 'signature': '1ee8318ada9f55671d0d8ec9d65227f7abf922e98a43a48dd244528dc3c00efa0286cf0c0b29d22889d68e3385b498038ff0121cc9e48eb4ebc69a73a5d4c9c519ad6cc72d6bbac30cb876724487a5997a50c7ea0b9d199e3b850c244ad29b808aeabded3e9ba01ec8c962ed3fc7832dc488281fdde9fdc5d5e9ffc3cc9e44752fb0fab370b7ab2a7299b30ee9867c36df872f1428241f5bdbb3f68952ba4b6c9497e3de4bb919a14a9de10884d5e09fc9a37c22c0206fe96e3866bde33238549648584a367df97d396539f306222137792f481d26080cdebbfebdcb839de0b7c28a5a8501c098eb632298a3947f5010c039eddda79fad197cd55bda4a93ae0d'}













def main():
    url=input("enter the url:")
    a=formcount(url)
    print(a)

if __name__ == "__main__":
    main()
