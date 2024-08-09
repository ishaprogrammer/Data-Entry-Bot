from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

zellow_website="https://appbrewery.github.io/Zillow-Clone/"
response=requests.get(zellow_website)
web_page=response.text
soup=BeautifulSoup(web_page,"html.parser")
price_find=soup.find_all("span",class_="PropertyCardWrapper__StyledPriceLine")
prices=[]
for all_prices in price_find:
    price_text=all_prices.get_text(strip=True)
    prices.append(price_text.replace("+/mo","").replace("/mo","").replace("+ 1bd","").replace("+ 1 bd",""))
link_find=soup.find_all("a",class_="StyledPropertyCardDataArea-anchor")
links=[]
for all_links in link_find:
    link_text=all_links["href"]
    links.append(link_text)
address_find = soup.find_all("address")
addresses = []
for all_addresses in address_find:
    address_text=all_addresses.get_text(strip=True)
    addresses.append(address_text.replace("|",""))
driver=webdriver.Chrome()
for n in range(len(links)):
    driver.get("https://forms.gle/tzZrogTTs3PmY14j9")
    time.sleep(5)
    fill_address=driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    fill_price=driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    fill_link=driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button=driver.find_element(by=By.CSS_SELECTOR,value=".NPEfkd.RveJvd.snByac")
    fill_address.send_keys(addresses[n])
    fill_price.send_keys(prices[n])
    fill_link.send_keys(links[n])
    submit_button.click()

   


  