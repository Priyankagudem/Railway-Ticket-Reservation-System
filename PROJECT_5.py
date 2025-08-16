import random

users = {}  # Account system

# Train list
trains = [
    {"number": "101", "From": "City A", "To": "City B", "seats": 5},
    {"number": "102", "From": "City C", "To": "City D", "seats": 3},
    {"number": "103", "From": "City E", "To": "City F", "seats": 4},
]

# Login status details
logged_in_user = None

# Creating account
def create_account():
    username = input("Create username: ")
    if username in users:
        print("Username already exists.")
        return
    password = input("Create password: ")
    users[username] = password
    print("Account created successfully!")

# Login details
def login():
    global logged_in_user
    username = input("Username: ")
    password = input("Password: ")
    if users.get(username) == password:
        logged_in_user = username
        print("Login successful!")
    else:
        print("Invalid credentials.")

# Showing train list
def show_trains():
    print("\nAvailable Trains:")
    for train in trains:
        print(f"{train['number']}: {train['source']} -> {train['dest']}, Seats: {train['seats']}")

# Booking tickets
def book_ticket():
    if not logged_in_user:
        print("Please login first.")
        return

    show_trains()
    train_no = input("Enter train number to book: ")

    train = next((t for t in trains if t["number"] == train_no), None)
    if not train:
        print("Invalid train number.")
        return

    try:
        count = int(input("How many tickets? "))
    except:
        print("Enter a valid number.")
        return

    if count > train["seats"]:
        print("Not enough seats available.")
        return

    passengers = []
    for i in range(count):
        print(f"Passenger {i+1}:")
        name = input("Name: ")
        try:
            age = int(input("Age: "))
        except:
            print("Invalid age.")
            return
        gender = input("Gender: ")
        phone = input("Phone (10 digits): ")
        if len(phone) != 10 or not phone.isdigit() or not (0 < age <= 120):
            print("Invalid passenger details.")
            return
        passengers.append((name, age, gender, phone))

    train["seats"] -= count
    pnr = "PNR" + str(random.randint(10000, 99999))
    print("\nTicket Booked Successfully!")
    print(f"PNR: {pnr}")
    print(f"Train: {train['number']} | {train['source']} -> {train['dest']}")
    for p in passengers:
        print(f"- {p[0]}, Age: {p[1]}, Gender: {p[2]}, Phone: {p[3]}")

# Main menu
def menu():
    while True:
        print("\n=== Railway Ticket System ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Book Ticket")
        print("4. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            book_ticket()
        elif choice == "4":
            print("You have been logged out. Thank you for using our system.")
            break
        else:
            print("Invalid choice.")

# Start the program 
menu()
