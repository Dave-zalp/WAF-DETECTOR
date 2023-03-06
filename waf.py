import requests
import re

url1 = input('Enter Url of the website("https://example.com")')
def inputurl (url1):
       pattern = r"^https://"
       if re.match(pattern, url1):
           url = url1
           return url
       else:
           nourl = f'https://{url1}'
           url = nourl
           return url


def validate(validated_url):
    return validated_url

def readcontent(par):
    try:
        r = requests.get(par)
        print(r.status_code)
    except requests.exceptions.ConnectionError:
        print("[-] An error Occured trying to access the page")
        pass

inp1 = inputurl(url1)
inp2 = validate(inp1)
inp3 = readcontent(inp2)



