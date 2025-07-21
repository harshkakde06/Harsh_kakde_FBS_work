x= int(input("Enter the number: "))
n= int(input("Enter the number: "))
sum=0
for i in range(1,n+1):
    term= ((-1) ** (i+1)) * (x**i)/(2*i-1)
    sum+= term
print(sum)