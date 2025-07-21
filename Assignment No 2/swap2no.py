#swap two number using third variable

num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))

print("Before swapping num1: ",num1 ,"num2: ",num2)

temp= num1
num1= num2
num2= temp

print("After swapping num1: ",num1 ,"num2: ",num2)