#Write a program to check if given 3 digit number is a palindrome or not.

num= int(input("Enter the 3 digit number: "))

if(num >=100 and num <=999):
    reverse= (num%10)*100 + ((num//10)%10)*10 +(num//100)
    print('reverse',reverse)

    if(num== reverse):
        print("It is palindrome number")
    else:
        print("It is not palindrome number")
else:
    print("It is not 3 digit number")