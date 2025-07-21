num=int(input("Enter the number: "))
temp=num
count=0
while(num!=0):
    a= num% 10
    num=num//10
    count+=1

print(count)
num=temp
sum=0

while(num!=0):
    a=num%10
    num=num//10
    sum=sum+(a**count)
if(sum==temp):
    print("Yes, It is armstrong number")
else:
    print("No,It is not armstrong number")