import json,pickle
import ast
stringlist = '[ "A","B","C" , " D"]'
print(type(ast.literal_eval(stringlist)))

with open("captions.pkl","rb") as f:
    js=pickle.load(f)

for count, i in enumerate(js):
    b=str(js[i])
    a=ast.literal_eval(b)


    print(a)

    print(type(a))

    if count==2:
        break
