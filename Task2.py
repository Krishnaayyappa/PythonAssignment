#1
number = 5
if (number%3==0 and number%5==0):
    print("Consultadd-Python Training")
elif (number%5==0):
    print("Python Training")
elif (number%3==0):
    print("Consultadd")


#######################################################################################################


#2
print(" 1-addition \n 2-subtraction \n 3-multiplication \n 4-division \n 5-Average")
userChoice =  int(input("Please select one of above options"))
if (userChoice in [1,2,3,4]):
    num1, num2 = [int(x) for x in input("Please enter two numbers: ").split()]
    if (userChoice == 1):
        result = num1+num2
        print(result)
        if (result<0): print("Negative") 
    elif (userChoice == 2):
        result = num1-num2
        print(result)
        if (result<0): print("Negative") 
    elif (userChoice == 3): 
        result = num1 * num2
        print(result)
        if (result<0): print("Negative") 
    elif (userChoice == 4):
        result = num1 / num2
        print(result)
        if (result<0): print("Negative") 
elif (userChoice == 5):
    first, second = [int(x) for x in input("Please enter two numbers: ").split()]
    result = (first+second)/2
    print(result)
    if (result<0): print("Negative") 
else:
    print("The value entered is not in the options")


#######################################################################################################


#3
a = 10
b = 20
c = 30
sum = a + b + c
avg = (sum/3)
print ("avg=", avg)
if (avg > a and avg > b and avg > c):
    print("Avg is higher than a, b, c")
elif (avg > a and avg > b):
    print("Avg is higher than a, b")
elif (avg > b and avg > c):
    print("Avg is higher than b, c")
elif (avg > a and avg > c):
    print("Avg is higher than a, c")
elif (avg > a):
    print("Avg is higher than a")
elif (avg > b):
    print("Avg is higher than b")
elif (avg > c):
    print("Avg is higher than c")


#######################################################################################################


#4
while(1):
    num = int(input("please enter a number"))
    if (num>=0):
        print("Good Going")
        continue
    else:
        print("It's Over")
        break

#######################################################################################################


#5 
for i in range(2001, 3200):
    if (i % 7 == 0):
        if (i % 5 != 0):
            print (i)

#######################################################################################################



#6
#first code:
# Type error. 'int" objects are not iterable

#second code:
# 0
# error 
# 1
# error 
# 2 


#third code:
# 0
# 1
# 2
# 3
# 4

#######################################################################################################

#7
count = 0
while (count < 7):
    if (count in [3,6]):
        count+=1
        continue;
    else:
        print(count)
        count+=1

#######################################################################################################

#8
letters  = 0
digits = 0
input = input("enter a alphanumeric value")
for i in input:
    if i.lower() in 'abcdefghijklmnopqrstuvwxyz':
        letters+=1
    elif i in '0123456789':
        digits+=1

print("letters {}   digits {}".format(letters, digits))

#######################################################################################################

#9
#without modification
luckyNumber = 10
while(1):
    number = int(input("Guess the lucky number"))
    if (number == luckyNumber):
        break
    else:
        continue


# with modification
luckyNumber = 10
while(1):
    number = int(input("Guess the lucky number"))
    if (number == luckyNumber):
        print("correct Guess")
        break
    else:
        answer = input("Wrong Guess! please press yes to continue no to quit ")
        if (answer == "no"):
            break
        else:
            continue

#######################################################################################################

#10
luckyNumber = 10
counter=1
while(counter<=5):
    number = int(input("guess the luck number"))
    if (number == luckyNumber):
        print("Good guess!")
        counter+=1
        continue
    else:
        if (counter<5):
            print("Try again!")
            print(5-counter, "chance left")
            counter+=1
        else:
            print(5-counter, "chance left")
            counter+=1
print("Game over")

#######################################################################################################

#11
luckyNumber = 10
counter=1
while(counter<=5):
    number = int(input("guess the luck number"))
    if (number == luckyNumber):
        print("Good guess!")
        break
    else:
        if (counter<5):
            print("Try again!")
            print(5-counter, "chance left")
            counter+=1
        else:
            print(5-counter, "chance left")
            counter+=1

if (counter>5): print("Sorry that was not very sucessful")
    

    








