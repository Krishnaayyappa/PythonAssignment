#1
def add(a,b):
    try:
        sum = a + c
    except:
        print("Some thing went wrong. Please check the code")


add (1,2)

#2
import sys
def openfile(filename):
    try:
        f = open(fileName+".txt")
        print(f.read())
    except:
        print("please enter valid filename")

fileName = sys.argv[1]
openfile(fileName)

#3
def lenumber(num):
    try:
        if(len(str(num))!=4):
            raise Exception("The length is too long/short!please provide only four digits")
        else:
            print("Valid number")
    except Exception as ex:
        print(ex)

lenumber(1234)

#4
print("Login Page")
username = input("Username:")
password = input("password")
count = 3
while(count>0):
    confirmpasssword = input("Reenter password")
    if (password == confirmpasssword):
        print("Valid password")
        break
    else:
        count-=1
        if(count>=1):
            print("Password not matching.{} attempts left".format(count))
            continue
        if(count==0):
            print("password not matching. Zero attempts left")


#5
#checked the given link

#6
f = open("doc.txt", "r")
for x in f:
    if((len(x)+1)%2==0):
        print(x)










