

alpha=0.1
def output(x1,x2,w1,w2,c):

    if x1*w1+x2*w2-c<0:

        return 0
    else:

        return 1
def calcwt(x,weight,error):
    global alpha
    return (weight+ 0.1* x *error)



w1=0.3
w2=-0.1
input=[(0,0,0),(0,1,1),(1,0,1),(1,1,0)]
#input=[(0,0,0),(0,1,1),(1,0,1),(1,1,1)]

for i in range(0,20):
    print(i+1)
    for j in input:
        print("",j[0], "\t",j[1],"\t",j[2],"\t",round(w1,3),"\t",round(w2,3),end="\t")
        actual =output(j[0],j[1],round(w1,3),round(w2,3),0.2)

        error=(j[2]-actual)
      #  if error<0:
       #     actual=actual-1
        #    print(actual, end="\t")
         #   error = (j[2] - actual)
          #  print(error, end="\t")

        print(round(j[0]*round(w1,3)+j[1]*round(w2,3)-0.2,2), end="\t")
        print(actual, end="\t")
        print(error, end="\t")
        w1=calcwt(j[0],w1,error)
        w2=calcwt(j[1],w2,error)
        print(round(w1,3),"\t", round(w2,3))
    print("\n")





