import random
from urllib import request

def  download(url):
    print("no1w")
    responses=request.urlopen(url)
    read=str(responses.read())
    print(read)
    lines= read.split("\\n")
    for line in lines:
        print(line)





download("https://www.facebook.com/exam.ioe.edu.np/")