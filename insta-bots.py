from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from time import sleep

"""
Before starting to code, i've changed the name of the variable starting with clc_ in the chromedriver 
executable file to prevent bot detection software from detecting selenium since it is a global variable
defined by the webdriver, so the browser and the detection software often search for it to tell if 
it's a selenium automation or not. So after changing the name of this variable to another name of the
same length, selenium is not detected anymore. 
"""

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-extensions')
options.add_argument('--profile-directory=Default')
options.add_argument("--disable-plugins-discovery")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


# enter the url of instagram and login to the account specified
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    driver.get("https://www.instagram.com/")
    driver.find_element(by=By.CSS_SELECTOR, value="button.aOOlW.bIiDR").click()  # cookies btn
    sleep(4)
    driver.find_elements(by=By.CSS_SELECTOR, value="input._2hvTZ.pexuQ.zyHYP")[0].send_keys(username)  # user input
    sleep(2)
    driver.find_elements(by=By.CSS_SELECTOR, value="input._2hvTZ.pexuQ.zyHYP")[1].send_keys(password)  # password input
    sleep(5)
    driver.find_element(by=By.CSS_SELECTOR, value="button.sqdOP.L3NKy.y3zKF").click()  # submit button
    sleep(5)


# randomly follows followers of a page passed as an argument
def random_follows_to_page_followers():
    page = input("Enter page username: ")
    driver.get("https://www.instagram.com/" + page)
    sleep(3)
    driver.find_elements(by=By.CSS_SELECTOR, value="div._7UhW9.vy6Bb.MMzan.KV-D4.uL8Hv.T0kll")[1].click()
    sleep(2)
    i = 0
    while driver.find_elements(by=By.CSS_SELECTOR, value="button.sqdOP.L3NKy.y3zKF")[i]:  # follow button
        driver.find_elements(by=By.CSS_SELECTOR, value="button.sqdOP.L3NKy.y3zKF")[i].click()
        sleep(1)
        i += 1
        driver.execute_script("document.getElementsByClassName('isgrP')[0].scrollBy(0,54)")


# likes user posts in a location passed as an argument
def likes_to_posts_in_location():
    country = input("Enter country: ")
    city = input("Enter city: ")
    location = input("Enter location: ")
    driver.get("https://www.instagram.com/explore/locations/")
    sleep(2)
    driver.find_element(by=By.LINK_TEXT, value=country).click()
    sleep(2)
    driver.find_element(by=By.LINK_TEXT, value=city).click()
    sleep(2)
    driver.find_element(by=By.LINK_TEXT, value=location).click()
    sleep(45)
    driver.find_elements(by=By.CSS_SELECTOR, value="div.v1Nh3.kIKUG._bz0w")[1].click()
    while True:
        sleep(random.randint(4, 7))
        driver.find_elements(by=By.CSS_SELECTOR, value=".wpO6b")[5].click() # like button
        sleep(random.randint(1, 2))
        driver.find_elements(by=By.CSS_SELECTOR, value=".wpO6b")[3].click() # next button


login()
random_follows_to_page_followers()
likes_to_posts_in_location()
