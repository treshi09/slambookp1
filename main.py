print("Welcome to My Slambook!")

slambook = []

while True:
    name = input("What is your name? ")
    age = input("How old are you? ")
    phone = input("What is your phone number? ")
    fav_color = input("What is your favourite colour? ")
    best_memory = input("What is your best memory with me? ")

    entry = {
        "Name": name,
        "Age": age,
        "Phone": phone,
        "Favourite Colour": fav_color,
        "Best Memory": best_memory
    }

    print("\nSLAMBOOK ENTRY")
    print("Name:", name)
    print("Age:", age)
    print("Phone:", phone)
    print("Favourite Colour:", fav_color)
    print("Best Memory:", best_memory)

    slambook.append(entry)

    more = input("Do you want to add another entry? (yes/no): ").lower()
    if more != "yes":
        break

print("\n--- ALL SLAMBOOK ENTRIES ---")
for i, friend in enumerate(slambook, start=1):
    print(f"\nFriend #{i}")
    for key, value in friend.items():
        print(f"{key}: {value}")
print("\nThank you for filling my slambook")