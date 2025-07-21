#Write a program to enter P,T,R and calculate compound interest.

p= int(input("enter the principal amount: "))
rate= float(input("enter the rate of interest: "))
n= int(input("enter the no. of times: "))
t= int(input("enter no. of years: "))

interest= p*(1*rate/n)**n*t

print("compound interest is: ",interest)