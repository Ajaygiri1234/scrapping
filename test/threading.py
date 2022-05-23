import threading
class Bulkey(threading.Thread):
    def run(self):
        for i in range(0,10):
            print("hello           ")

x=Bulkey()
x.start()
for i in range(0,10):
    print(i)