#---------Imports
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.firefox.options import Options
#---------End of imports

### FUNCTIONS ###

### MAIN FLOW ###
options = Options()
options.headless = False

urlpage = 'https://pennclubs.com'

driver = webdriver.Firefox(options=options, executable_path='/Users/chandlercheung/Documents/Projects/geckodriver')

driver.get(urlpage)

results = driver.find_elements_by_xpath("//*[@class='ClubCard__CardWrapper-qqpg24-0 cKtqOz column is-half-desktop']//*[@class='ClubCard__Card-qqpg24-2 eufSiA card']//*[@class='ClubCard__CardHeader-qqpg24-4 guYdpv']//*[@class='ClubCard__CardTitle-qqpg24-5 igiPKV is-size-5']")

print('________')
print(len(results))

for i in range(len(results)):
    print(results[i].text)

print('________')
if __name__ == '__main__':
    pass