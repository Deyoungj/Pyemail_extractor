import requests, re
from bs4 import BeautifulSoup


class Extaract:
    def __init__(self, url:list=[]):
        self.url = url
        self.email_rex = r'[\w\.]+@[\w\.]+'
    
    def get_email(self):
        pass

    def get_phone(self):
        pass
    


EMAIL_REX = r'[\w\.]+@[\w\.]+'

url = "https://www.google.com/search?q=requests+hhas+no+attribute+status&oq=requests+hhas+no+attribute+status&aqs=chrome..69i57j0i22i30l4.38788j0j4&sourceid=chrome&ie=UTF-8"

r = requests.get(url)


print(BeautifulSoup(r.text).prettify())

