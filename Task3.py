#1
list_differentDatatypes = [100, 200, 300, 50.5, 70.25, 3+2j, 7+5j, "hello", "world", "welcome"]

#######################################################################################################

#2
list_5 = [1,2,3,4,5]
print(list_5[2:5])
print(list_5[1:])
print(list_5[-3:-1])

#######################################################################################################

#3
list_num = [2,3,5,7,9,10,12]
sum = 0
mul = 1
for i in list_num:
    sum = sum + i
    mul = mul * i

print("sum", sum)
print("multiply", mul)

#######################################################################################################

#4
list_numbers = [1000, 200, 5, 6000, 70, 985, 1225]
list_numbers.sort()
print("Smallest Number=", list_numbers[0])
print("Largest Number", list_numbers[-1])

#######################################################################################################


#5
list_oddandeven = [1,2,3,4,5,6,7,8,9,10]
new_list = [number for number in list_oddandeven if number%2!=0]
print(new_list)

#######################################################################################################

#6
list_n = []
for i in range(1,31):
    if (i <=5 or i>=26):
        list_n.append(i**2)
    else:
        list_n.append(i)
print(list_n)

#######################################################################################################

#7
list1 = [1,3,5,7,9,10]
list2 = [2,4,6,8]
list1.pop()
list1.extend(list2)
print(list1)

#######################################################################################################

#8
a = {1:10, 2:20}
b={3:30, 4:40}
dict_3 = a | b
print(dict_3)

#######################################################################################################

#9
this_dict = {}
n=5
for i in range(1,n+1):
    this_dict.update({i:i**2})

print(this_dict)

#######################################################################################################

#10
inputValues = input("enter the values seperated by comma")
listString = inputValues.split(",")
tupleString = tuple(listString)
print(listString)
print(tupleString)










