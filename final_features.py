import tldextract
import urllib
import re
from fuzzywuzzy import fuzz
import ipaddress
def extract_features(url):
    ext=tldextract.extract(url)
    list = ['com', 'net', 'org', 'info', 'io', 'co', 'online', 'site', 'store', 'tech', 'club', 'cn', 'uk', 'de', 'ru', 'br', 'in', 'jp', 'fr', 'ca', 'au', 'us']
    if ext.suffix in list:
        return 0
    else:
        return 40

def havingat(url):
    if '@' in url:
        return 10
    else:
        return 0

def havingdash(url):
    if 'https://' or 'https://' not in  url:
            url='http://'+ url       
    hostname=urllib.parse.urlparse(url).hostname
    if '-' in hostname:
        return 10
    else:
        return 0

def emergencywords(url):
    if 'https://' or 'https://' not in  url:
            url='http://'+ url       
    pathe=urllib.parse.urlparse(url).path
    a=pathe.strip('/')
    segment=a.split('/')
    depth=len(segment)
    keywords = ['login.html', 'pay.html', 'update.html', 'otp.html']
    if any(s in segment for s in keywords):
        return 10
    else:
        return 0

def depthhave(url):
    try:
        if 'https://' or 'https://' not in  url:
            url='http://'+ url        
        pathe=urllib.parse.urlparse(url).path
        a=pathe.strip('/')
        segment=a.split('/')
        depth=len(segment)
        if depth<=1:
            return 10
        else:
            return 0
    except:
        return 1

def numbr(url):
    list=['1','2','3','4','5','6','7','8','9','0']
    if any(u in url for u in list):
        return 20
    else:
        return 0

def platformabuse(url):
    hosting_platforms = [
    '.vercel.app',
    '.netlify.app',
    '.surge.sh',
    '.pages.dev',      
    '.github.io',  
    '.gitlab.io',      
    '.herokuapp.com',  
    '.run.app',        
    '.azurewebsites.net',
    '.blogspot.com',   
    '.tumblr.com',
    '.repl.co',        
    '.replit.app',     
    '.glitch.me',
    '.firebaseapp.com' 
]
    if 'https://' or 'https://' not in  url:
            url='http://'+ url        
    netloc=urllib.parse.urlparse(url).netloc
    final_netloc=netloc.lower()
    if any(s in final_netloc for s in hosting_platforms):
        return 20
    else:
        return 0

def brandassubdirectory(url):
    if 'https://' or 'https://' not in  url:
            url='http://'+ url     
    netloc=urllib.parse.urlparse(url).netloc
    pathe=urllib.parse.urlparse(url).path
    list = ['microsoft', 'google', 'apple', 'amazon', 'facebook', 'instagram', 'netflix', 'spotify', 'paypal', 'venmo', 'zelle', 'cashapp', 'visa', 'mastercard', 'americanexpress', 'chase', 'bankofamerica', 'wellsfargo', 'ups', 'fedex', 'dhl', 'usps', 'flipkart', 'myntra', 'zouk', 'meesho', 'irs', 'hmrc', 'cra']
    flag1=2
    flag=0
    if any(s in netloc for s in list):
        flag = 1
    else:
        flag=0
    if any(a in pathe for a in list):
        flag1=2    
    else:
        flag1=0
    
    if flag==1 and flag1==0:
        return 0
    elif flag==0 and flag1==2:
        return 20
    else:
        return 0
#1 is in netloc
#2 is in path

def typosquat(url):
    if 'https://' or 'https://' not in  url:
            url='http://'+ url        
    hostname=urllib.parse.urlparse(url).hostname
    path=urllib.parse.urlparse(url).path
    list=['microsoft.com', 'google.com', 'apple.com', 'amazon.com', 'facebook.com', 'instagram.com', 'netflix.com', 'spotify.com', 'paypal.com', 'venmo.com', 'zelle.com', 'cashapp.com', 'visa.com', 'mastercard.com', 'americanexpress.com', 'chase.com', 'bankofamerica.com', 'wellsfargo.com', 'ups.com', 'fedex.com', 'dhl.com', 'usps.com', 'flipkart.com', 'myntra.com', 'zouk.com', 'meesho.com', 'irs.gov', 'hmrc.gov.uk', 'cra-arc.gc.ca']
    highestratio =0
    for i in list:
        i=i+"https://"
        ratio=fuzz.ratio(hostname,i)
        ratio2=fuzz.ratio(path,i)
        if ratio >=80 and ratio!=100:
            if ratio>highestratio:
                highestratio=ratio
    if highestratio > 80 and highestratio!=100:
        return 10
    else:
        return 0

def ipinurl(url):
    if 'https://' or 'https://' not in  url:
            url='http://'+ url       
    netloc=urllib.parse.urlparse(url).hostname
    try:
        ipaddress.ip_address(netloc)
        return 10
    except:
        return 0

def httpinurl(url):
    try:
        scheme=urllib.parse.urlparse(url).scheme().lower()
        if scheme == 'http':
            return 10
        else:
            return 0
    except:
        return 20

def main():
        url=input()
        a=extract_features(url)
        b=havingat(url)
        c=havingdash(url)
        d=emergencywords(url)
        e=depthhave(url)
        f=numbr(url)
        g=platformabuse(url)
        h=brandassubdirectory(url)
        i=typosquat(url)
        j=ipinurl(url)
        k=httpinurl(url)
        sum=a+b+c+d+e+f+g+h+i+j+k
        #print(sum)
        return sum
if __name__ == "__main__":
    main()