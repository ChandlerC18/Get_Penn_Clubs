#---------Imports
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.firefox.options import Options
#---------End of imports

### MAIN FLOW ###
urlpage = 'https://pennclubs.com'

r = requests.get(urlpage)
soup = BeautifulSoup(r.content, 'html.parser') # get html of website
content = soup.find('div', class_='pages__ResultsText-fxyd84-1 hAHPYs')
num = int(content.text.split(' ')[1]) # get number of clubs

options = Options()
options.headless = True # option to show browser or not

driver = webdriver.Firefox(options=options, executable_path='/Users/chandlercheung/Documents/Projects/geckodriver') # start up web driver
print("Started web driver")

driver.get(urlpage) # load website


for i in range(int(num / 15) + 2):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;") # scroll down to bottom of page
    time.sleep(3) # sleep for 3 sec

print("Loaded website")

clubs = driver.find_elements_by_xpath("//*[@class='ClubCard__CardWrapper-qqpg24-0 cKtqOz column is-half-desktop']//*[@class='ClubCard__Card-qqpg24-2 eufSiA card']//*[@class='ClubCard__CardHeader-qqpg24-4 guYdpv']//*[@class='ClubCard__CardTitle-qqpg24-5 igiPKV is-size-5']") # clubs

print("Got clubs")

links = driver.find_elements_by_xpath("//*[@class='ClubCard__CardWrapper-qqpg24-0 cKtqOz column is-half-desktop']//a[@href]") # club websites

print("Got website links")

df = pd.DataFrame(columns=['Club', 'Website'])

for i in range(len(clubs)):
    name = clubs[i].text
    link = links[i].get_attribute('href')
    df.loc[len(df.index)] = [name, link] # add data to csv

df.to_csv('penn_clubs.csv', index=False)
print("Saved csv file")

driver.quit() # close driver