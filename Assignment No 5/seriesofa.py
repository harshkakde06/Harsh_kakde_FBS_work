num=int(input("Enter the number: "))
sum=0
for i in range(1,11):
    term= (num**i)/i
    print(term)
    sum+= term
print(sum)
