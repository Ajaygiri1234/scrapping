from urllib import request
import requests
from bs4 import BeautifulSoup
import pandas as pd

def spider(search_item):
    url='https://www.google.com/search?tbm=isch&q=' + search_item +'&oq='+ search_item

    sourcecode=requests.get(url)
    plaintext=sourcecode.text
    soup=BeautifulSoup(plaintext,'html.parser')
    #

                 #above two line can be eliminated by one line
                        # not needed plaintext = sourcecode.text
                  #soup = BeautifulSoup(sourcecode.txt, 'html.parser')
    #print(soup.find_all('img')[1].get('src'))
    for link in soup.find_all('img'):
        print(link.get('src'))


spider("appleorange")


#df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
 #                  'mask': ['red', 'purple'],
  #                 'weapon': ['sai', 'bo staff']})
#df.to_csv('ouytg.csv',index=False)
print("hello")