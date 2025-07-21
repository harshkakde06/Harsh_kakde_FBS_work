#Write a program to input two angles from user and find third angle of the triangle.

angle1= int(input("Enter the angle: "))
angle2= int(input("Enter the angle: "))

angle3= 180-(angle1+angle2)

print("Third angle of triangle is: ",angle3)