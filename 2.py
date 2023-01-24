from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains
import time
from time import sleep
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=options)

#Website login xpaths
xPathLogin = '//*[@id="login"]'
xPathEmail =  '//*[@id="username"]'
xPathPassword = '//*[@id="password"]'
xPathSubmitLogin = '//*[@id="submit-login"]'

#Website login confirmation xpath
xPathMyAccount = '//*[@id="my-account"]'

#Tennis matches xpaths
xPathTennis = '//*[@id="tennis"]'
xPathMatch = '//*[@class="match"]'
xPathOdd = '//*[@class="odds"]'

#Bet placing xpaths
xPath1Dollar = '//*[@id="bet-amount"]'
xPathPlaceBet = '//*[@id="place-bet"]'

#Wait for login to be successful
wait.until(EC.presence_of_element_located((By.XPATH, xPathMyAccount)))

#Navigate to tennis matches
browser.find_element_by_xpath(xPathTennis).click()

#Find all available tennis matches
matches = browser.find_elements_by_xpath(xPathMatch)

#Iterate through each match
for match in matches:
    odds = match.find_elements_by_xpath(xPathOdd)
    #Iterate through each odd of a match
    for odd in odds:
        if float(odd.text) >= 1.85 and float(odd.text) <= 2.55:
            #Place a 1 dollar bet on the odd
            odd.click()
            browser.find_element_by_xpath(xPath1Dollar).send_keys("1")
            browser.find_element_by_xpath(xPathPlaceBet).click()
            sleep(1)

browser.quit()
