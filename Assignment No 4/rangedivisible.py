start = int(input("Enter the start number: "))
stop = int(input("Enter the stop number: "))
divi = int(input("Enter the divisible number: "))

for i in range(start , stop + 1):
    if(i % divi ==0):
        print(i)