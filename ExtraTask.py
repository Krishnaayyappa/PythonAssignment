#1

x  = [100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

#acesslist1
print(x[5][0:4])
#acesslist2
print(x[6:8])

#acesslist3
print([x[i] for i in range(0,len(x)) if i%2 == 0])

#acesslist4
print([x[::-1]])

#acesslist5
print([x[5][5][0]])

#acesslist6
x.clear()
print(x)


#2
x = range(0,1001)
list1 = list(x)
print(list1)

#Not able to use the xrange() function in python3

#3
#tuples are immutable and takes less memory than the lists

#4
list_1t100 = list(range(0,101))
list2 = []
for i in list_1t100:
    if i % 2 == 0 and i % 3 == 0:
        list2.append(i)

print(list2)

#5
string1 = input("enter a string")
revstring =  string1[::-1]
vowels = []
for i in range(0, len(revstring)):
    if revstring[i] in "aeiou":
        vowels.append((revstring[i], i))

print(vowels)


#6
string1 = input("enter a string")
strlist = string1.split(" ")
for i  in strlist:
    if len(i)%2==0:
        print(i)

#7
x = [1,2,3,4,5,6,7,8,9,-1]
result = 8
def sum_result(x, result):
    for i in range(0, len(x)-1):
        for j in range(i+1, len(x)):
            if x[i] + x[j] == result:
                print(x[i],x[j])
            

sum_result(x,result)


#8
even_list = []
odd_list = []

def evenlist(num1):
    if len(even_list)<5:
        even_list.append(num1)
    elif len(even_list)>=5:
        print("The even list is full please choose odd numbers to complete the odd list")
    
def oddlist(num1):
    if len(odd_list)<5:
        odd_list.append(num1)
    elif len(odd_list)>=5:
        print("The odd list is full please choose even numbers to complete the even list")

def two_lists():
    while(len(even_list)<5 or len(odd_list)<5):
        num = int(input("please enter a number between 1 and 50"))
        if num%2==0:
            evenlist(num)
        elif num%2==1:
            oddlist(num)
    if sum(even_list)>sum(odd_list):
        return sum(even_list)
    else:
        return sum(odd_list)


print(two_lists()) 
    


#9
string1 = "12abcbacbaba344ab"
unqString = list(set(string1))
countList = []

for i in unqString:
    if i not in "0123456789":
        x = string1.count(i)
        countList.append((i,x))

for j in countList:
    print(j[0] + "=" + str(j[1]), end=" ")


#10
tuple1 = (1,2,3,4,5,6,7,8,9,10)
list1 = list(tuple1)
for i in list1:
    if i %2 != 0:
        list1.remove(i)

tuple2 = tuple(list1)
print(tuple2)









