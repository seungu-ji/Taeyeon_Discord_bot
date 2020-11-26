# google crawling
from urllib.request import urlretrieve
from urllib.parse import quote_plus    # korean support
from bs4 import BeautifulSoup          # Essential module
from selenium import webdriver         # Google crolling

def crawl_google_image(keyword):
   url = f'https://www.google.com/search?q={quote_plus(keyword)}&sxsrf=ALeKk00OQamJ34t56QSInnMzwcC5gC344w:1594968011157&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjXs-7t1tPqAhVF7GEKHfM4DqsQ_AUoAXoECBoQAw&biw=1536&bih=754'

   driver= webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
   driver.get(url)
   for i in range(500):
      driver.execute_script("window.scrollBy(0,10000)")

   html = driver.page_source
   soup = BeautifulSoup(html)
   img = soup.select('img')
   n = 51
   imgurl = []

   for i in img:
      try:
         imgurl.append(i.attrs["src"])
      except KeyError:
         imgurl.append(i.attrs["data-src"])

   for i in imgurl:
      urlretrieve(i, "./img/"+keyword+str(n)+".jpg")
      n += 1

   driver.close()
   print("finish")