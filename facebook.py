from selenium import webdriver
from getpass import getpass
from webdriver_manager.chrome import ChromeDriverManager

username = input('P1 Enter YOUR Facebook username, email or phone no,;')
passwd = getpass('Enter your Facebook password')

driver = webdriver.Chrome(ChromeDriverManager().install)

driver.get('https;//www.fabebook.com')

txtUsername = driver.find_element_by_id('email')
txtUsername.send_keys(username)

txtpasswd = driver.find_element_by_id('pass')
