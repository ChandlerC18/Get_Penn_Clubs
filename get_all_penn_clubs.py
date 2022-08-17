#---------Imports
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.firefox.options import Options
#---------End of imports

### FUNCTIONS ###

### MAIN FLOW ###
urlpage = 'https://pennclubs.com'

r = requests.get(urlpage)
soup = BeautifulSoup(r.content, 'html.parser')
content = soup.find('div', class_='pages__ResultsText-fxyd84-1 hAHPYs')
num = int(content.text.split(' ')[1])

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options, executable_path='/Users/chandlercheung/Documents/Projects/geckodriver')

driver.get(urlpage)

for i in range(int(num / 15) + 2):
    # execute script to scroll down the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

    # sleep for 30s
    time.sleep(2)

clubs = driver.find_elements_by_xpath("//*[@class='ClubCard__CardWrapper-qqpg24-0 cKtqOz column is-half-desktop']//*[@class='ClubCard__Card-qqpg24-2 eufSiA card']//*[@class='ClubCard__CardHeader-qqpg24-4 guYdpv']//*[@class='ClubCard__CardTitle-qqpg24-5 igiPKV is-size-5']")

links = driver.find_elements_by_xpath("//*[@class='ClubCard__CardWrapper-qqpg24-0 cKtqOz column is-half-desktop']//a[@href]")

df = pd.DataFrame(columns=['Club', 'Website'])

for i in range(len(clubs)):
    name = clubs[i].text
    link = links[i].get_attribute('href')
    df.loc[len(df.index)] = [name, link]

print(len(clubs))
print('________')

# close driver
driver.quit()
if __name__ == '__main__':
    pass