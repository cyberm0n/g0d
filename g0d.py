import requests
from bs4 import BeautifulSoup

banner = """
         .d8888b.      888 
        d88P  Y88b     888 
        888    888     888 
 .d88b. 888    888 .d88888 
d88P"88b888    888d88" 888 
888  888888    888888  888 
Y88b 888Y88b  d88PY88b 888  v0.76
 "Y88888 "Y8888P"  "Y88888 
     888                   
Y8b d88P                   
 "Y88P"   

"""

a = input("[*] User Name > ")

url = 'https://github.com/'+a
page = requests.get(url)


soup = BeautifulSoup(page.text, 'html.parser')

name = soup.find_all('span',class_="p-name vcard-fullname d-block overflow-hidden")[0].get_text().strip()
username = soup.find_all('span',class_="p-nickname vcard-username d-block")[0].get_text().strip()

flwrs = soup.find_all('span',class_="text-bold color-fg-default")[0].get_text().strip()
flwing = soup.find_all('span',class_="text-bold color-fg-default")[1].get_text().strip()
repo = soup.find_all('span',class_="Counter")[0].get_text().strip()

print("")
print("Name : "+name)
print("Userame : "+username)
print("Followers : "+flwrs)
print("Following : "+flwing)
print("Repo : "+repo)
