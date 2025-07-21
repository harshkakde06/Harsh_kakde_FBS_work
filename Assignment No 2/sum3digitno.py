#find the sum of 3 digit number

num= int(input("enter the 3 digit no: "))
a= num%10
num= num//10
b= num%10
c= num//10

sum= a+b+c

print("sum of 3 digit no is: ",sum)


