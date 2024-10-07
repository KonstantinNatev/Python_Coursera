bill_total = 54
discount_up_than_hundred = 20
discount_down_than_hundred = 10

if bill_total > 100:
    print("Bill total is greater than 100")
    bill_total = bill_total - discount_up_than_hundred
elif 100 > bill_total > 50:
    print("Bill total is less than 100")
    bill_total = bill_total - discount_down_than_hundred
else:
    print("Bill total is less than 50")

print("Bill total is " + str(bill_total))
