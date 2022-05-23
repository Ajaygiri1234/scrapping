import random
from urllib import request
import urllib.request
def  download(url):
    name= random.randrange(1,100)
    fullname=str(name) + ".jpg"
    urllib.request.urlretrieve(url,fullname  )


download("https://th.bing.com/th/id/OIP.AvUZJkFRu60sN2FGvV0srAHaEK?w=300&h=168&c=7&o=5&dpr=1.25&pid=1.7")
