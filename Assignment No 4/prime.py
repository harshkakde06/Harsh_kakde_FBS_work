num = int(input("Enter the number: "))
for i in range(2 , num):
    if(num % 2 == 0):
        print("It is not prime number")
        break
else:
    print("It is prime number")