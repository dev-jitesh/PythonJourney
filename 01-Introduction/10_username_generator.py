first_name = input("First name: ").lower()
last_name = input("Last name: ").lower()
year = input("DOB year: ")

print(first_name[:3], last_name[-2:], year[-2:], sep="")