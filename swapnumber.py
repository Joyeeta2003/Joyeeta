x = int(input("enter first number:"))
y = int(input("enter second number:"))

print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)

x=x+y
y=x-y
x=x-y

print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)
