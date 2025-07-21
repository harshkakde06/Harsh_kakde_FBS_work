start = int(input("Enter the start num: "))
stop = int(input("Enter the stop num: "))
for i in range(start , stop+1):
    if(i % 7== 0 and i % 5 == 0):
        print(i)
    