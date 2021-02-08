#Write a program that asks the user how many people are in their dinner group.
#If the answer is more than eight, print a message saying they'll have to wait for a table.
#Otherwise, report that their table is ready.

guests = input("How many people are there in your dinner group?: ")
guests = int(guests)

if guests > 8:
    print(f"You have {guests} people in your party. You'll have to wait for a table.")
else:
    print(f"You have {guests} people in your party. Your table is ready.")