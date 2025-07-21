#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

side1= int(input("Enter the side: "))
side2= int(input("Enter the side: "))
side3= int(input("Enter the side: "))

if(side1==side2==side3):
    print("It is equilateral triangle")
elif(side1==side2 or side2==side3 or side1==side3):
    print("It is isosceles triangle")
else:
    print("It is scalene triangle")