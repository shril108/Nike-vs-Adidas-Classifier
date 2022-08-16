from bs4 import BeautifulSoup
import requests
import base64


def getHtml(url):
    html = requests.get(url)
    return html.text


site_text = requests.get("https://www.nike.com/w/mens-shoes-nik1zy7ok")
soup = BeautifulSoup(site_text.content, 'html.parser')
products = soup.find_all('div', class_="product-card css-1v1uza4 css-z5nr6i css-11ziap1 css-14d76vy css-dpr2cn product-grid__card")
print(products[0])
# x = 1
# for product in products:
#     pic = product.find('img')
#     if x < 10:
#         print(f"Number {x}: {pic['src']}")
#         x += 1

# pict = ''
# response = requests.get(pict)
# num = 0
# if response.status_code == 200:
#     with open("/Users/apple/Desktop/sample{num}.jpg", 'wb') as f:
#         f.write(response.content)
#         num+=1