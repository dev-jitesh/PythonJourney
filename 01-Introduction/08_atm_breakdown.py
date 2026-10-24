amount = int(input("Enter amount to withdraw: "))

notes_500 = amount // 500
amount = amount % 500

notes_200 = amount // 200
amount = amount % 200

notes_100 = amount // 100
amount = amount % 100

notes_50 = amount // 50
amount = amount % 50

notes_20 = amount // 20
amount = amount % 20

notes_10 = amount // 10
amount = amount % 10

print("\n--- Cash Breakdown ---")
print(f"500 Rupee notes: {notes_500}")
print(f"200 Rupee notes: {notes_200}")
print(f"100 Rupee notes: {notes_100}")
print(f"50 Rupee notes: {notes_50}")
print(f"20 Rupee notes: {notes_20}")
print(f"10 Rupee notes: {notes_10}")
print(f"Remaining loose change: {amount}")