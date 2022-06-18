from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
options.headless=False
driver= Edge("C:\\Users\\User\\Downloads\\edgedriver_win64\\msedgedriver.exe",options=options)

result = {}
#this is one way
#######################################################
def search_using_url():
    lis=["i eate rice","i eat cegetable","he is running","he is sleeping"]
    lis=["i eate rice"]
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


#driver.quit()

###################################
#driver= Edge("C:\\Users\\User\\Downloads\\edgedriver_win64\\msedgedriver.exe",options=options)
#
#url="https://translate.google.com"
#driver.get(url)
#element = driver.find_element_by_css_selector("div.D5aOJc.vJwDU")
#driver.execute_script("arguments[0].innerHtml = 'what_you_want_to_show'", element)
#lis=["i eate rice","i eat cegetable","he is running","he is sleeping"]
import json,pickle
with open("captions.pkl","rb") as f:
    orig_caption=pickle.load(f)
url="https://translate.google.com/?sl=en&tl=ne"
nepali_caption={}
driver.get(url)
time.sleep(10)
print("ok")
for count, i in enumerate(orig_caption):
    driver.find_element(By.CLASS_NAME, "er8xn").clear()

    # Enter "webdriver" text and perform "ENTER" keyboard action
    #print(str(orig_caption[i]))
    lis=[]
    for each in orig_caption[i]:
        driver.find_element(By.CLASS_NAME, "er8xn").clear()

        driver.find_element(By.CLASS_NAME, "er8xn").send_keys(str(each+ Keys.ENTER))#sendkey("translating eord")
        time.sleep(2)
        element = driver.find_element_by_css_selector("span.Q4iAWc").text
        lis.append(element)
    nepali_caption[i]=lis
        # Perform action ctrl + A (modifier CONTROL + Alphabet A) to select the page
    #webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()

    print(lis,type(lis))



    print("exit")
    if count==4:
        break


j={1:"er"}