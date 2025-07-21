#program to find minimum no.of notes for given amount.

amount = int(input("enter amount: "))

#500
n500= amount//500
r_amount= amount%500

#200
n200= r_amount//200
r_amount%=200

#n100
n100= r_amount//100
r_amount%=100

#n50
n50= r_amount//50
r_amount%=50

#n20
n20= r_amount//20
r_amount%=20

#n10
n10= r_amount//10
r_amount%=10

print("notes to be paid for amount: ",amount)
print("notes for 500: ",n500)
print("notes for 200: ",n200)
print("notes for 100: ",n100)
print("notes for 50: ",n50)
print("notes for 20: ",n20)
print("notes for 10: ",n10)