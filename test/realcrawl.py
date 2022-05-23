from urllib import request
import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    print(1)

    page=1
    while (page<= max_pages):
        print(2)
        url='https://www.merriam-webster.com/dictionary/hello'
        print(1)
        sourcecode=requests.get(url)
        plaintext=sourcecode.text
        soup=BeautifulSoup(plaintext,'html.parser')#

                     #above two line can be eliminated by one line
                            # not needed plaintext = sourcecode.text
        print(soup)               #soup = BeautifulSoup(sourcecode.txt, 'html.parser')
        for link in soup.find_all('a'):
            print(link)
            for i in link:
                print(i)


            href=link.get('href')
            for item in href:
                if item=="/":
                    href=str('https://www.merriam-webster.com')+href
                break
            print(href)
        page=page+1

spider(1)

def spider1(max_pages):
    A=True
    while A:
        print(1)

        page=1
        while (page<= max_pages):
            print(2)
            url='http://127.0.0.1:8000/'
            print(1)
            sourcecode=requests.get(url)
            plaintext=sourcecode.text
            soup=BeautifulSoup(plaintext,'html.parser')#
            url = 'http://127.0.0.1:8000/copy/'
            print(1)
            sourcecode1 = requests.get(url)
            plaintext1 = sourcecode1.text
            soup1 = BeautifulSoup(plaintext1, 'html.parser')  #

                         #above two line can be eliminated by one line
                                # not needed plaintext = sourcecode.text


            #soup = BeautifulSoup(sourcecode.txt, 'html.parser')
            a1=b1=""
            print(soup==soup1)
            for link in soup.find_all('a'):

                for i in link:
                    print('a' + i)
                    a1=str(i)
                break
            for link in soup1.find_all('a'):

                for i in link:
                    print("b" + i)
                    b1=str(i)
                break
            if a1!=b1:
                A=True
            else:
                A=False
                #exeute program

            page=page+1


    for i in range(10):
        print(i)



#spider1(1)
