#1
string_input = "1234abdcd"
string_reverse = string_input[::-1]
print(string_reverse)


#2
def count_type_character(input_string):
    upper_count=0
    lower_count=0
    for i in input_string:
        if i.isupper():
            upper_count+=1
        elif i.islower():
            lower_count+=1
    return [upper_count, lower_count]

inputString = input("Enter the string")
output = count_type_character(inputString)
print("No of uppercase characters:{} No of lowercase characters:{}".format(output[0], output[1]))


#3
def unique_elements(inputList):
    inputSet = set(inputList)
    outputList = list(inputSet)
    return outputList

input_List = [1,2,2,2,2,2,3,3,3,3,3,3,5,5,5,7,7,7,8,8,8,8,9,9,9]
output = unique_elements(input_List)
print(output)

#4
def sort_string(inputString):
    inputList = inputString.split("-")
    inputList.sort()
    outputString = "-".join(inputList)
    return outputString
    
input_string = "w-b-d-a-g-k-v-q"
output = sort_string(input_string)
print(output)

#5
def upper_sentence(sentence):
    return sentence.upper()

sentence = """Hello world welcome to Python
An Object oriented programming language"""
output = upper_sentence(sentence)
print(output)

#6
def addStringNumbers(string1, string2):
    return int(string1) + int(string2)

string1 = "100"
string2="200"
output = addStringNumbers(string1, string2)
print(output)

#7
def largestString(str1, str2):
    if(len(str1)>len(str2)):
        print(str1)
    elif (len(str1)<len(str2)):
        print(str2)
    else:
        print(str1 + "\n" + str2)

string1 = "hello world"
string2 = "Welcome to python"
largestString(string1, string2)

#8
def squareTuple1(n):
    tup1 = ()
    for i in range (1,n+1):
        tup2=(i**2,)
        tup1+=tup2
    print(tup1)

def squareTuple2(n):
    list1=[]
    for i in range(1,n+1):
        list1.append(i**2)
    print(list1)

squareTuple1(20)
squareTuple2(20)

#9
def showNumbers(n):
    for i in range(n+1):
        if(i%2==0):
            print(str(i)+" EVEN")
        elif(i%2==1):
            print(str(i)+" ODD")

showNumbers(10)

#10
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]  
evenNumbers = filter(lambda x: x%2==0, list1)
print(list(evenNumbers))
    

#11
list1 = [1,2,3,4,5,6,7,8,9,10]  
evenNumbers = list(filter(lambda x: x%2==0, list1))
print(evenNumbers)
evenSquares = list(map(lambda x: x**2, evenNumbers))
print(evenSquares)

#12
def division(a,b):
    try:
        c = a/b
    except ZeroDivisionError:
        print("we cannot divide a number by zero")
    except:
        print("some went wrong!please check the code")


division(5,0)


#13
import functools
list1 = [1,2,3,4,5,6,7]
reducedValue = functools.reduce(lambda x,y:str(x)+str(y), list1)
print(reducedValue)

#14
def multiple_7(number):
    list=[]
    for i in range(1,number+1):
        if (i%7==0 and i%3!=0):
            list.append(i)
    return list


print(multiple_7(100))

#15
def multiple_itself(number):
    return number*number

list1=[1,2,3,4,5]
output = list(map(multiple_itself, list1))
print(output)

#16
#i
#output: 
#2

#ii
#output:
# after f
# after f?
# error as f(x,4) is not defined


















    






