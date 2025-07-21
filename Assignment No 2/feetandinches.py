#Convert the distance given in feet and inches into meters and centimeters.

feet= int(input("Enter the distance in feet: "))
inches= int(input("Enter the distance in inches: "))

totalinches= feet*12 + inches
total_cm= totalinches*2.54

meters= total_cm//100
centimeters= total_cm%100

print("meters: ",meters,"centimeters: ",centimeters)