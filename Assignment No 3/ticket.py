#Accept the age of five people and also per person ticket amount and then calculate total amount of ticket to travel.

person1= int(input("enter the age: "))
person2= int(input("enter the age: "))
person3= int(input("enter the age: "))
person4= int(input("enter the age: "))
person5= int(input("enter the age: "))
amount= int(input("enter the amount: "))

total= 0

if(person1 < 12):
    total+= amount - (amount*0.3)
elif(person1 > 59):
    total+= amount - (amount*0.5)
else:
    total+= amount

if(person2 < 12):
    total+= amount - (amount*0.3)
elif(person2 > 59):
    total+= amount - (amount*0.5)
else:
    total+= amount

if(person3 < 12):
    total+= amount - (amount*0.3)
elif(person3 > 59):
    total+= amount - (amount*0.5)
else:
    total+= amount

if(person4 < 12):
    total+= amount - (amount*0.3)
elif(person4 > 59):
    total+= amount - (amount*0.5)
else:
    total+= amount

if(person5 < 12):
    total+= amount - (amount*0.3)
elif(person5 > 59):
    total+= amount - (amount*0.5)
else:
    total+= amount

print(total)



