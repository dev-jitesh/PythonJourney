units = float(input("Ynits of electricity consumed: "))

if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units - 100) * 5
else:
    bill = 500 + ((units - 200) * 100)

print(f"Total bill: {bill} rupees")