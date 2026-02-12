print("hello buddy")
#python is dinamic programming language so we dont need to declare the variable type
var=10
print(var)
name="python"
print(name)
#Multiple Assignment
a,b,c=10,20,30
print(a)
#Swapping using multiple assignment:
x = 5
y = 10
x, y = y, x
print(x)
print(y)
#assign same value to multiple variables
a= b = c = 100
print(a)
#type() function is used to check the type of variable
x= 10
print(type(x))
#delating a variable
x=25
del x
#Variable scope means the region (area) where a variable is accessible.
name="guyat"
def marks():
    print(name)#global variable can be accessed inside the function
marks()
print(name)#local variable cannot be accessed outside the function
print("thanks buddy")