#1
string1 = "HeLLo worlD"
listUpper = [x for x in string1 if x.isupper()==True]  
print(listUpper)


#2
#using dictionary comprehension and loops
students = ['Smit', 'Jaya', 'Rayyan'] 
subjects = ['CSE', 'Networking', 'Operating System']
dict1 = {students[i]:subjects[j] for i in (0,len(students)) for j in (0,len(subjects)) if i == j }
print(dict1)

#using Zip dunction
students = ['Smit', 'Jaya', 'Rayyan'] 
subjects = ['CSE', 'Networking', 'Operating System']
dict1 = dict(zip(students, subjects))
print(dict1)

#3
#Learned about yield, next and generators

#4
def reverse_string(str1):
    for i in range(len(str1)-1, -1, -1):
        yield str1[i]

string1 = "Consultadd Training"
revString = ""
for i in reverse_string(string1):
    revString = revString + i

print(revString)


#5
def add(num1, num2):
    return num1 + num2

def mul(num1, num2):
    return num1 * num2

def sub(num1, num2):
    return num1 - num2

def div(num1, num2):
    return num1 / num2

def artihmeticOperations(operation):
    n1 = int(input("Enter first number"))
    n2 = int(input("Enter second number"))
    output = operation(n1,n2)  
    print(output)

artihmeticOperations(add)
artihmeticOperations(mul)
artihmeticOperations(sub)
artihmeticOperations(div)








