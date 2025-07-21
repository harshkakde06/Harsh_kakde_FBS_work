no_of_passengers= int(input("Enter the no.of passengers: "))
ticket_cost= int(input("Enter the cost of ticket: "))

total_amount=0
for i in range(1,no_of_passengers+1):
    age= int(input("Enter the age: "))
    if(age<12):
        discount=0.30
    elif(age>59):
        discount=0.50
    else:
        discount=0.0

    final_cost= ticket_cost* (1-discount)
    total_amount+=final_cost

print("The cost of all passengers is: ",total_amount)
