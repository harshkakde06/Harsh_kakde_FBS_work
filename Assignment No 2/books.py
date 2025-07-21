#WAP to calculate selling price of book based on cost price and discount.

cost_price= int(input("Enter cost price of book: "))
discount_percent= int(input("Enter the discount percentage: "))

discount_amount= (discount_percent /100) * cost_price

selling_price= cost_price - discount_amount

print("The selling price of the book is: ",selling_price)