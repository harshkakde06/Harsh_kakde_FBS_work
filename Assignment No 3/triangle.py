#Write a program to input angles of triangle and check whether triangle is valid or not.

angle1= int(input("enter the angle 1: "))
angle2= int(input("enter the angle 2: "))
angle3= int(input("enter the angle 3: "))

if(angle1 + angle2 + angle3 == 180):
    print("It is Valid Triangle")
else:
    print("It is Not Valid")