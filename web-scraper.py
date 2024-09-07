import requests
from bs4 import BeautifulSoup
import json


url = "https://deafzworld.com/"
page = requests.get(url)

soup = BeautifulSoup(page.content,"html.parser")

card_elements = soup.find_all("div",class_="wpspeedo-team--single")

creators = []

for card in card_elements:

    creator = {}

    print("-"*50)

    creator["name"] = card.h3.text 

    links = card.find_all("a") #All socials

    for link in links:#Differentiate between links
        link_href = link["href"]
        if "facebook" in link_href:
            creator["fb_link"] = link_href
        elif "instagram" in link_href:
            creator["insta_link"] = link_href
        elif "tiktok" in link_href:
            creator["tt_link"] = link_href

    creator["cover"] = card.find("div",class_="team-member--thumbnail").img["src"] #Background

    creator["contentType"] = card.find("h4",class_="wps-team--member-desig wps-team--member-element").text
    
    creators.append(creator)

with open("./deaf-worldz/src/python-data.json", 'w') as output_file:
	json.dump(creators, output_file, indent=2)
    
    