from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--remote-debugging-port=9222')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--remote-debugging-address=0.0.0.0')
options.add_argument('--remote-debugging-port=9222')

driver = webdriver.Chrome(options=options, executable_path='path/to/chromedriver')
driver.get("https://odibets.com/")
print(driver.page_source)

#Website login xpaths
xPathLogin = '//*[@id="login"]'
xPathEmail =  '//*[@id="username"]'
xPathPassword = '//*[@id="password"]'
xPathSubmitLogin = '//*[@id="submit-login"]'

Email = 'porttoace@gmail.com'
Password = 'portto'
#Website login confirmation xpath
xPathMyAccount = '//*[@id="my-account"]'


#Tennis matches xpaths
xPathTennis = '//*[@id="tennis"]'
xPathMatch = '//*[@class="match"]'
xPathOdd = '//*[@class="odds"]'

wait = WebDriverWait(driver, 10)

#Bet placing xpaths
xPath1Dollar = '//*[@id="bet-amount"]'
xPathPlaceBet = '//*[@id="place-bet"]'

#Wait for login to be successful

#Navigate to tennis matches
driver.find_element_by_xpath(xPathTennis).click()

#Find all available tennis matches
matches = driver.find_elements_by_xpath(xPathMatch)

#Iterate through each match
for match in matches:
    odds = match.find_elements_by_xpath(xPathOdd)
    #Iterate through each odd of a match
    for odd in odds:
        if float(odd.text) >= 1.85 and float(odd.text) <= 2.55:
            #Place a 1 dollar bet on the odd
            odd.click()
            driver.find_element_by_xpath(xPath1Dollar).send_keys("1")
            driver.find_element_by_xpath(xPathPlaceBet).click()
            time.sleep(1)

driver.quit()
