#Task One Numbers and Variables

#1
X_int, Y_float, Z_string = 100, 50.50, "krishna";
print(type(X_int), type(Y_float), type(Z_string));

#######################################################################################################

#2
value1 = 3 + 5j;
value2 = 100
value1, value2 = value2, value1;
print(value1, value2);

#######################################################################################################

#3
#with third variable
number1 = 100;
number2 = 200;
temp = number2;
number2 = number1;
number1 = temp;
print(number1, number2); 
#without third variable
num1=3;
num2=5;
num1 = num1 + num2;
num2 = num1 - num2;
num1 = num1 - num2;
print(num1, num2); 

#######################################################################################################

#4
x = input("enter your name");
#python2.X
# print "Hi", x;
#pyhton3.X
print("Hi ", x);

#######################################################################################################

#5
x= int(input("enter number between 1-10"));
y = int(input("enter the number between 1-10"));
z = x + y;
result = 30 + z;
print(result);

#######################################################################################################

#6
x,y,z = 10, 15.5, "hello";
print("the input values are of type: ", type(x), type(y), type(z));

#######################################################################################################

#7
#Upper camel case or pascal case
FirstName = "Krish";
#lower camel case
lastName = "narina"
#snakecase
date_of_birth = 1996;
#uppercase
LOCATION = "montreal";

#######################################################################################################

#8
#Yes, it will change the value without any error.This is because, in python the variables will not be
#predefined with any datatype. The datatype of the variable depends on the value to which it got assigned.
#if the variable is reassigned to a new value of same or diffrent datatype, it will clear the old value
#in the memory and new value will be placed in that location.



