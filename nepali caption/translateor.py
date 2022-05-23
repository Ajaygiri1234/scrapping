import time
import webbrowser
from bs4 import BeautifulSoup
import requests
import json
chrome="C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver.exe"


list_of_items=["i am reading book"]
#list_of_items=["जीत",'शेरबहादुर','दर्ता',"मोरङ","हत्या","मृत्यु","महिला"]
#div class="D5aOJc vJwDU"
from selenium.webdriver import Chrome,Edge,EdgeOptions

options=EdgeOptions()
options.headless=True
driver= Edge("C:\\Users\\User\\Downloads\\edgedriver_win64\\msedgedriver.exe",options=options)

result = {}
#this is one way
#######################################################
lis=["i eate rice","i eat cegetable","he is running","he is sleeping"]
for i in lis:
    url="https://translate.google.com/?sl=auto&tl=ne&text="+i+"&op=translate"
    print(str(url))
    driver.get(url)

    while True:
        try:
            element=driver.find_element_by_css_selector("span.Q4iAWc").text
            break
        except:
            pass

    print(element)


driver.quit()

###################################
#driver= Edge("C:\\Users\\User\\Downloads\\edgedriver_win64\\msedgedriver.exe",options=options)

url="https://translate.google.com"
driver.get(url)
element = driver.find_element_by_css_selector("div.D5aOJc.vJwDU")
driver.execute_script("arguments[0].innerHtml = 'what_you_want_to_show'", element)