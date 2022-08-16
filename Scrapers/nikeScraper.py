from selenium import webdriver
from tkinter.messagebox import NO
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import urllib



PATH = "C:\Rutgers - Shril\CS Studying\Selenium Drivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)
URL = "https://www.nike.com/w/mens-shoes-nik1zy7ok"
imgs = []
driver.get(URL)


SCROLL_PAUSE_TIME = 0.5
i = 0
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)

    #scrolling
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

    #how many times do you want the scraper to scroll and download images
    # i += 1
    # if i == 40:
    #     break
elems = driver.find_elements_by_class_name('product-card__hero-image')
for img in elems:
    if img.get_attribute('src') not in imgs:
        imgs.append(img.get_attribute('src'))
driver.quit()



try:
    for i, url in enumerate(imgs):
        urllib.request.urlretrieve(url, "C:\Rutgers - Shril\CS Studying\Projects\WebScraper\shoepics\\nike\\nike"+ str(i) +".jpg")
except Exception as e:
    print("Failed to download: ", e)
else:
    print("you have all your nike shoe pics now!")
