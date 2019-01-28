#make terminal calculator that allows the user to select the operator and then shows the result

a=float(input("enter the number"))
b=float(input("enter the number"))
print("sum of a and b:",a+b)
print("difference of a and b:",a-b)
print("division of a and b:",a/b)
print("multiplication of a and b:",a*b)
print("remainder of a and b:",a%b)

#write a program to check of the year is leap or not
year=int(input("enter year to be checked"))
if year%4==0:
    print("the year is a leap year")
else:
    print("the year is not a leap year")


#write a program that ask the user to enter name age and mobile number
name=input("name")
if name.isalpha()==True:
    print("valied")
else:
    print("invalied")
age=int(input("age"))
if age>18 and age.isnumeric==True:
    print("valied")
else:
    print("invalied")
mobilenumber=input("mobilenumber")
if mobilenumber.isnumeric()==True:
    print("valied")
else:
    print("invalied")
#write a program to accept the dimensions of polygon as length and breath print if it is a square or a rectangle
length=int(input("enter the length"))
breadth=int(input("enter the breadth"))
if length==breadth:
    print("square")
else:
    print("rectangle")