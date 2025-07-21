#Write a program to check if user has entered correct userid and password.

userid= input("enter the userid: ")
password= input("enter the password: ")

if(userid== "abcd" and password== "abc123"):
    print("Successful Login")
else:
    print("Wrong userid or password")