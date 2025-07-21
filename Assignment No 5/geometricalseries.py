num=int(input("Enter the number of term: "))
sum=0
for i in range(1,num):
    term= 2**i
    sum+=term
print(sum)