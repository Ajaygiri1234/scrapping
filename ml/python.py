dn=[[1,2,3,4],[2,1,3,4],[2,3,1,4],[2,3,4,1]]
def square(s):
    return s**2

n=[1,2,3,4]
print(list(map(square,n)))
s=[[i**2 for i in j]for j in dn]
print(s)
null=[[] for i in range(0,6)]
print(null)


num=[1,2,3,3,4,5,6,7,8,9,10,11,1,2]

a=[i for i in num if i%2==0]
print(a)

print(list(i for i in range(0,20) if i%2!=0))