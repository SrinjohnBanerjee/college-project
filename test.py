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
def main():
    url=input("enter the url:")
    a=formcount(url)
    print(a)

if __name__ == "__main__":
    main()