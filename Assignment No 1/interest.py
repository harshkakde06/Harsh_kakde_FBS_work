#Write a program to enter P,T,R and calculate simple interest.

p= int(input("enter the principal amount: "))
years= int(input("enter the years: "))
rate= float(input("enter the rate of interest: "))

interest= p*years*rate/100

print("simple interest is: ",interest)