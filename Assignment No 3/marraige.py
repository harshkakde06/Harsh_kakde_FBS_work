#Write a program to check if person is eligible to marry or not.

gender= input("Enter the gender(male/female): ")
age= int(input("Enter the age: "))

if(gender =='male'):
    if(age >=21):
        print("You are eligible for marry")
    else:
        print("You are not eligible for marry")
elif(gender =='female'):
    if(age >=18):
        print("You are eligible for marry")
    else:
        print("You are not eligible for marry")    
else:
    print("Invalid gender entered")