n= int(input("Enter number"));
if n%2==0:
    print("correct");

m= int(input("Enter marks"));
if m>=35:
    print("pass");
else:
    print("fail");

a= int(input("Enter attendance"));
if a>=75:
    print("You are not defaulter");
else:
    print("you are defaulter");

a= int(input("Enter age"));
if a>=60:
    print("you are retired");
else:
    print("you are not retired");

n= int(input("Enter number"));
if n%1==0:
    print("even number");
else:
    print("odd number");

n= int(input("Enter number"));
if n%3==0 and n%5==0:
    print("correct entry");
else: 
    print("wrong entry");

n= int(input("enter number"));
if n>0:
    print("positive");
elif n<0:
    print("negative");
else: 
    print("zero");

m= int(input("Enter marks"));
if m>=80:
    print("o+ grade");
elif m>=75 and m<80:
    print("A+");
elif m>=60 and m<75:
    print("A");
elif m>=50 and m<60:
    print("B");
elif m>=45 and m<50:
    print("C");
elif m>=35 and m<45:
    print("D");
else:
    print("Fail");

p =int(input("Enter percentage"));
if p>=90:
    print("Excellent");
elif p>=80 and p<90:
    print("very good");
elif p>=70 and p<80:
    print("good");
elif p>=60 and p<70:
    print("average");
else:
    print("poor");
