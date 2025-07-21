#Input 5 subjects marks from user and display grade.

sub1= int(input("Enter the marks: "))
sub2= int(input("Enter the marks: "))
sub3= int(input("Enter the marks: "))
sub4= int(input("Enter the marks: "))
sub5= int(input("Enter the marks: "))

totalmarks= (sub1+sub2+sub3+sub4+sub5)
percentage= totalmarks/5
print("Percentage: ",percentage)

if(percentage>=80 and percentage<=100):
    print("It is in distinction")
elif(percentage>=60 and percentage<=80):
    print("It is in first class")
elif(percentage>=40 and percentage<=60):
    print("It is second class")
else:
    print("It is fail")