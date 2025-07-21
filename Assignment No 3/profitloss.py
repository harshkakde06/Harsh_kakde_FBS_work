#Write a program to calculate profit or loss.

costprice= int(input("enter the cost price: "))
sellingprice= int(input("enter the selling price: "))

profit= sellingprice - costprice
loss= costprice - sellingprice

if(sellingprice > costprice):
    print("It is profit of rs. ",profit)
elif(sellingprice < costprice):
    print("It is loss of rs. ",loss)
else:
    print("No profit,No loss")