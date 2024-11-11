tuple1= (10000,20000,30000,40000,50000)
for i in tuple1:
    print("salary of the employees: ",i)

tuple1= (154.5,180.6,175.9,190.1,165.3,176.8,159.9)
for i in tuple1:
    print("height of the students",i)

def unpack(a,b,c):
    print(a,b,c)
unpack(*[1,2,3])

marks= (23,27,36,38,49,53,67,74,89,98)
print("the highest marks are: ",max(marks),"the lowest marks are: ",min(marks))

emptytuple=()
print(emptytuple)

onevaluetuple=(45)
print(onevaluetuple)

tuple1= ("red","green","blue","yellow","1234")
tuple2= (7538,3437,2736)
print("tuple[0]:",tuple[0])
print("tuple[2]:",tuple2[2])
print("first 3 values of tuple: ",tuple[0:3])

a= (1,2,3,4,5)
print(a)
al= list(a)
del al[2]
b= tuple(al)
print(b)

a=9
b=3
temp= a
a=b
b= temp
print(a,b)

def allnum(*args):
    print(args)
allnum(3,2.0,"4")
