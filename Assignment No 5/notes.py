amount= int(input("Enter the amount: "))
notes= (500,200,100,50,20,10)

for i in notes:
    if(amount >= i):
        count= amount//i
        amount= amount %i
        print(f"{i} x {count}")