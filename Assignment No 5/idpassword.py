user_id= "Harsh"
password= "Harsh123"

for i in range(1,4):
    user_id= input("Enter user_id: ")
    password= input("Enter the password: ")
    if(user_id=="Harsh" and password=="Harsh123"):
        print("successful Login")
        break
    else:
        print("Re-enter user_id Password")
    i+=3

