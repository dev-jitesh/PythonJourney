principal = float(input("Principal amount = "))
rate = float(input("Annual interest rate = "))
time = float(input("Time(in years) = "))

amount = principal * (1 + rate/100) ** time

print(f"The final amount will be ={amount:.2f}")