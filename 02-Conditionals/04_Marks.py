marks = int(input("Enter marks: "))

if marks >= 90:
    print("Excellent")
elif 75 <= marks <= 89:
    print("Good")
elif 40 <= marks <= 74:
    print("Passed")
else:
    print("Failed")