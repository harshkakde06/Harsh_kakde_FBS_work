#to find reverse of a 2 digit number

num= int(input("enter the 2 digit number: "))
a= num//10
b= num%10
c= b*10+a

print("reverse number is: ",c)