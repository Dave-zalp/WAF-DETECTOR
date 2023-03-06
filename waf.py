import requests
import re
import time

banner = """  _____   _    _     ____   _    ____  _   _ ____  
|__  /  / \  | |   |  _ \ / \  |  _ \| | | / ___| 
  / /  / _ \ | |   | |_) / _ \ | |_) | | | \___ \ 
 / /_ / ___ \| |___|  __/ ___ \|  _ <| |_| |___) |
/____/_/   \_\_____|_| /_/   \_\_| \_\\___/|____/                    """

print(banner)
time.sleep(5)

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
        f = open('content.txt' , 'w')
        f.write(str(r.content))
        f.close()
        print('[+] File written to context.txt Successfully')
    except requests.exceptions.ConnectionError:
        print("[-] An error Occured trying to access the page")
        pass

inp1 = inputurl(url1)
inp2 = validate(inp1)
inp3 = readcontent(inp2)



