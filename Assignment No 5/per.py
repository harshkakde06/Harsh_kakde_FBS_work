students= int(input("Enter the no.of students: "))
total_per= 0
for i in range(1,students+1):
    print("Enter marks for students",i)
    total_marks=0

    for j in range(1,6):
        marks= int(input("Enter marks: "))
        total_marks+=marks
        print()
    per=total_marks/500*100
    total_per+=per
    print("Percentage for students",i)

    print(per)
average= total_per/students
print("Average percentage of students",average)