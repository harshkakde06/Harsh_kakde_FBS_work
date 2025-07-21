start= int(input("Enter the start no: "))
stop= int(input("Enter the stop no: "))

for i in range(start,stop):
    temp= i
    num= i
    sum= 0
    count= 0

    while(num != 0):
        a = num % 10
        num = num // 10
        count += 1

    num = i  

    
    while(num != 0):
        a = num % 10
        sum += a ** count
        num = num // 10

    
    if(sum == temp):
        print(temp)

