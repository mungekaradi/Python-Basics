def add(x,y):
    print("the sum of the number is: ",x+y)
def subtract(x,y):
    print("the subtraction of the number is: ",x-y)
def multiply(x,y):
    print("the product of the number is: ",x*y)
def divide(x,y):
    print("the divide of the number is: ",x/y)
n= int(input("enter a number: "))
n1= int(input("enter a number: "))
add(n,n1)
subtract(n,n1)
multiply(n,n1)
divide(n,n1)

def even_odd(x):
    if x%2==0:
        print("the number is even")
    else:
        print("the number is odd")
n= int(input("enter a number: "))
even_odd(n)

def swap():
    x= int(input("enter: "))
    y= int(input("enter: "))
    temp=0
    temp=x
    x=y
    y= temp
    print("After swapping:\n The value of x is", x,"The value of y is", y)
swap()

def armstrong():
    x= int(input("enter a number: "))
    strx=str(x)
    lenstrx=len(strx)
    sum_powers= sum(int(digit)**lenstrx for digit in strx)
    if sum_powers==0:
        print("this is a armstrong number")
    else:
        print("this is not a armstrong number")
armstrong()

def get_factors():
    x= int(input("enter a number: "))
    i=1
    print("factors of",x,"are:")
    while i<=x:
        if x%i==0:
            print(i)
            i= i+1
get_factors()

def palindrome():
    x= input("enter a word: ")
    if x[::-1]==x:
        print("this is a palindrome")
    else:
        print("this is not a palindrome")
palindrome()