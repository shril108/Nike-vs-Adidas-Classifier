from urllib.error import HTTPError
from selenium import webdriver
import time
from tkinter.messagebox import NO
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request



PATH = "C:\Rutgers - Shril\CS Studying\Selenium Drivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)
URL = "https://www.flightclub.com/adidas?size_men=10.0"
imgs = []
driver.get(URL)


i = 1
while True:

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2)")
    time.sleep(3)
    links = driver.find_elements_by_class_name("kpUBOn")
    for img in links:
        if img.get_attribute('src') not in imgs:
            imgs.append(img.get_attribute('src'))
            print(img.get_attribute('src'))
    
    i+=1
    driver.get(f"https://www.flightclub.com/adidas?page={i}size_men=10.0")
    # how many times do you want the scraper to scroll and download images
    if i == 10:
        break
driver.quit()



for i, url in enumerate(imgs):
    try:
        urllib.request.urlretrieve(
        url, "C:\Rutgers - Shril\CS Studying\Projects\WebScraper\shoepics\\adidas\\adidas" + str(i) + ".jpg")
    except HTTPError as e:
        continue
