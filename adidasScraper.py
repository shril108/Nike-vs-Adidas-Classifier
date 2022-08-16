from email.policy import HTTP
from urllib.error import HTTPError
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from tkinter.messagebox import NO
from selenium.webdriver.common.by import By
from PIL import Image
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request



# PATH = "C:\Rutgers - Shril\CS Studying\Selenium Drivers\chromedriver.exe"
# driver = webdriver.Chrome(PATH)
# URL = "https://www.flightclub.com/adidas?size_men=10.0"
# imgs = []
# driver.get(URL)


# i = 1
# while True:

#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2)")
#     time.sleep(3)
#     links = driver.find_elements_by_class_name("kpUBOn")
#     for img in links:
#         if img.get_attribute('src') not in imgs:
#             imgs.append(img.get_attribute('src'))
#             print(img.get_attribute('src'))


    
#     i+=1
#     driver.get(f"https://www.flightclub.com/adidas?page={i}size_men=10.0")
#     # how many times do you want the scraper to scroll and download images
#     if i == 10:
#         break
# driver.quit()


# # try:
# #     while True:
# #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #         time.sleep(2)
# #         new_height = driver.execute_script("return document.body.scrollHeight")
# #         if new_height == last_height:
# #             break
# #         last_height = new_height
# #     maain = driver.find_element_by_tag_name("html")
# #     maain.send_keys(Keys.DOWN)
# #     time.sleep(0.5)
# #     maain.send_keys(Keys.DOWN)
# #     time.sleep(0.5)
# #     maain.send_keys(Keys.DOWN)
# #     links = driver.find_elements_by_class_name("kpUBOn")
# #     counter = 0
# #     for link in links:
# #         counter +=1
# #         print(counter, ". ", link.get_attribute('src'))
# #     counter = 0
# #     while counter < len(links):
# #         print(links[counter].get_attribute('src'))
# #         print(counter)
# #         counter +=1
# #     print(len(links))
# #     print('printed!')
# # except StaleElementReferenceException as e:
# #     # print("did not save?")
# #     links = driver.find_elements_by_class_name("kpUBOn")
# #     print(links[0].get_attribute("src"))
# #     print(e)
# #     driver.quit()
# # else:
# #     print("found them")
# #     driver.quit()

# counter2 = 0
# try:
#     for i, url in enumerate(imgs):
#         counter2+=1
#         urllib.request.urlretrieve(
#             url, "C:\Rutgers - Shril\CS Studying\Projects\WebScraper\shoepics\\adidas\\adidas" + str(i) + ".jpg")
# except HTTPError as e:
#     print("Failed to download: ", e, counter2)
#     for i, url in enumerate(imgs):
#         counter2+=1
#         urllib.request.urlretrieve(
#             url, "C:\Rutgers - Shril\CS Studying\Projects\WebScraper\shoepics\\adidas\\adidas" + str(i) + ".jpg")
# else:
#     print("you have all your adidas shoe pics now!")

links = ["https://cdn.flightclub.com/750/TEMPLATE/260121/1.jpg"
"https://cdn.flightclub.com/750/TEMPLATE/299064/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/299000/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/294745/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/253215/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/299066/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/305826/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/282137/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/286378/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/274477/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/296154/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/302898/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/307403/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/800502/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/802501/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/307513/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/296150/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/293584/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/260872/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/800389/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/312938/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/201519/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/291329/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/299345/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/302897/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/289333/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/269628/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/305621/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/803137/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/267256/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/802390/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/296985/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/266127/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/291210/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/277780/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/304927/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/273421/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/260878/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/278504/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/260875/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/805206/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/260879/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/800801/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/260871/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/255869/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/263700/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/802389/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/143102/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/280135/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/160140/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/262762/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/804366/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/186406/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/296514/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/259110/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/312789/1.jpg",
"https://cdn.flightclub.com/placeholders/dash.png?w=360",
"https://cdn.flightclub.com/750/TEMPLATE/193990/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/312199/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/143710/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/272676/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/159148/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/266530/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/291147/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/260881/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/246720/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/156799/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/260874/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/192798/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/135739/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/260876/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/167253/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/175730/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/285936/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/139789/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/281433/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/266589/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/188715/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/266134/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/277985/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/281247/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/168056/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/313453/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/269205/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/275109/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/299271/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/275105/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/279430/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/805264/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/260880/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/305433/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/161894/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/276020/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/250402/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/296146/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/265354/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/149298/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/201536/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/279130/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/805204/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/263709/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/264635/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/250721/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/304080/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/802388/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/186201/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/279591/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/149021/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/144281/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/283772/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/254031/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/251736/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/296153/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/188714/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/168022/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/253224/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/260882/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/245218/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/149165/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/261690/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/201422/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/284335/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/263701/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/189775/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/253590/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/151876/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/805220/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/245931/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/136354/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/253591/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/168053/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/253227/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/201114/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/804276/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/138422/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/314012/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/296156/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/805205/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/182203/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/165419/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/277287/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/288140/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/303798/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/266688/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/295119/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/160139/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/303522/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/253223/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/149161/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/266539/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/138978/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/144646/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/135276/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/161337/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/161333/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/142204/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/140232/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/292495/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/248947/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/191047/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/286338/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/191577/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/153830/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/149295/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/800743/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/292828/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/159161/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/273196/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/151564/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/285928/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/279613/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/260127/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/296987/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/803499/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/154709/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/313006/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/288373/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/176597/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/296151/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/259560/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/160081/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/180437/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/285041/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/803261/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/136913/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/800826/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/201189/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/304077/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/805221/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/162300/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/143598/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/280980/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/165280/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/157936/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/160138/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/307514/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/206883/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/311830/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/262409/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/163753/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/177360/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/250399/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/164756/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/276358/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/802801/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/291211/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/314084/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/149779/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/161166/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/155611/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/250575/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/201074/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/201538/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/287545/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/277286/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/291212/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/260870/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/148389/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/286343/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/284993/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/312824/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/246921/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/311839/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/314088/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/201172/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/201539/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/249937/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/296152/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/201122/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/284569/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/154518/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/246162/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/185409/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/158173/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/312823/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/156787/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/250403/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/273586/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/136468/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/303854/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/311101/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/803790/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/164192/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/260489/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/149854/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/201153/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/312825/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/244666/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/206884/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/139927/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/312949/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/244667/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/284994/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/260877/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/164053/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/299585/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/263703/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/279341/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/305932/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/280877/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/262615/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/290580/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/160846/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/244665/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/161119/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/157338/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/201296/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/273345/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/296942/1.jpg",
"https://cdn.flightclub.com/750/TEMPLATE/251729/1.jpg"]
for i, url in enumerate(links):
    try:
        urllib.request.urlretrieve(
        url, "C:\Rutgers - Shril\CS Studying\Projects\WebScraper\shoepics\\adidas\\adidas" + str(i) + ".jpg")
    except HTTPError as e:
        continue