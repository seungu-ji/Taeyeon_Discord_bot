# google crawller

from urllib.request import urlretrieve
from urllib.parse import quote_plus    # korean support
from bs4 import BeautifulSoup as BS    # Essential module
from selenium import webdriver         # Google crolling

keyword = input("Input keyword: ")
i_URL = f'https://www.google.com/search?q={quote_plus(keyword)}&sxsrf=ALeKk00OQamJ34t56QSInnMzwcC5gC344w:1594968011157&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjXs-7t1tPqAhVF7GEKHfM4DqsQ_AUoAXoECBoQAw&biw=1536&bih=754'

driver= webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver.get(i_URL)

html = driver.page_source
soup = BS(html,features="html.parser")

img = soup.select('img')

i_list = []
count = 51

print("Searching...")
for i in img:
   try:
      i_list.append(i.attrs["src"])
   except KeyError:
      i_list.append(i.attrs["data-src"])

print("Downloading...")
for i in i_list:
   urlretrieve(i,"img/"+keyword+str(count)+".jpg")
   count+=1

driver.close()
print("FINISH")