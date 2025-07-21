#captcha program.

import random
user_id= input("Enter user_id: ")
password= input("Enter password: ")

if(user_id== "harsh" and password== "harsh123"):
    captcha= random.randint(1000,9999)
    print("Captcha: ",captcha)
    input= int(input("Enter captcha: "))
    if(input==captcha):
        print("Login Successful")
    else:
        print("Wrong Captcha")
else:
    print("Unsuccessful login")
