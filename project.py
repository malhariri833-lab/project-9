
print("==============================")
print("   Holiday Activity Planner")
print("==============================")

print("Choose your holiday type:")
print("1. Beach Holiday")
print("2. Mountain Holiday")

choice = input("Enter 1 or 2: ")

if choice == "1":
    print("\nWelcome to the Beach Holiday!")

    print("Choose your activity:")
    print("1. Swimming")
    print("2. Sandcastle Building")

    activity = input("Enter 1 or 2: ")

    if activity == "1":
        print("Activity: Swimming")
        print("Enjoy swimming in the sea!")
    else:
        print("Activity: Sandcastle Building")
        print("Have fun building a sandcastle!")

elif choice == "2":
    print("\nWelcome to the Mountain Holiday!")

    print("Choose your activity:")
    print("1. Hiking")
    print("2. Camping")

    activity = input("Enter 1 or 2: ")

    if activity == "1":
        print("Activity: Hiking")
        print("Enjoy exploring the mountain trails!")
    else:
        print("Activity: Camping")
        print("Enjoy camping under the stars!")

else:
    print("Invalid choice. Please enter 1 or 2.")

print("\nThank you for using the Holiday Activity Planner!")
