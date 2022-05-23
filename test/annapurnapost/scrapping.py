import time
import webbrowser
from bs4 import BeautifulSoup
import requests
import json
chrome="C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver.exe"


list_of_items=["जीत",'शेरबहादुर','दर्ता']
#list_of_items=["जीत",'शेरबहादुर','दर्ता',"मोरङ","हत्या","मृत्यु","महिला"]

from selenium.webdriver import Chrome,Edge,EdgeOptions

options=EdgeOptions()
options.headless=False
driver= Edge("C:\\Users\\User\\Downloads\\edgedriver_win64\\msedgedriver.exe",options=options)

result = {}

def get_article_using_bs4(url):
    sourcecode = requests.get(url)
    plaintext = sourcecode.text
    soup = BeautifulSoup(plaintext, 'html.parser')  #

    # above two line can be eliminated by one line
    # not needed plaintext = sourcecode.text
    # soup = BeautifulSoup(sourcecode.txt, 'html.parser')
    article = soup.find("p").text
    return article

def get_article_using_selenium(url):
    driver_article.get(url)
    time.sleep(1)
    elements = driver_article.find_elements_by_css_selector("div.news-content")

    for count,i in enumerate(elements):
        if count==1:
            return (i.text)



def search_information(item):
    item_full="https://www.annapurnapost.com/search/news?query="+item
    driver.get(item_full)
    #driver.quit()


    #to load the search

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 0)")
    ##soup=BeautifulSoup(driver.page_source,'lxml')
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")


    while True:
        elements = driver.find_elements_by_css_selector("Div.media.wide-media>li>div.media-right")
        print(len(elements))

        if len(elements)>=30:
            break
        else:
            driver.execute_script("window.scrollTo(0, 0)")
            ##soup=BeautifulSoup(driver.page_source,'lxml')
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")




    result[item]=[]
    for count ,i in enumerate(elements):
       # print(i.text)
       if count<30:
            heading=i.find_element_by_css_selector("div>h3").text
            description=i.find_element_by_css_selector("div>p").text
            date=i.find_element_by_css_selector("small").text
            link = i.find_element_by_css_selector("div>h3>a").get_attribute("href")
            #print(count,heading,date,description,link)
            result[item].append({ 'heading': heading, 'date':date, 'description':description, 'link':link})
       else:
           break
        #print(count,i.get_attribute("href"))
        #print(i.text)
        #get_fulldescription(link)
for item in list_of_items:
    search_information(item)
    #breakfor 1 item



print(result)

driver.quit()
driver_article= Edge("C:\\Users\\User\\Downloads\\edgedriver_win64\\msedgedriver.exe",options=options)

#print(elements[0].get_attribute("a"))
for i in (result):
    print("ajay",len(result[i]))
    for count, j in enumerate(result[i]):
        #both works
        #article=get_article_using_selenium(result[i][count]["link"])
        article=get_article_using_bs4(result[i][count]["link"])
        result[i][count]["article"]=article
        print(count)


print(result)
driver_article.quit()


result = json.dumps(result, indent = 3,ensure_ascii=False)
print(result)

with open("sample.json", "w") as outfile:
    json.dump(result,outfile)

with open('sample.json') as json_file:
    data = json.load(json_file)
print("="*50)
print("="*50)
print(data)