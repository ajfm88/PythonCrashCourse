#Do the following to create a program that simulates how websites ensure that everone has
#a unique username.
#Make a list of five or ore usernames called current_users.
#Make another list of five usernames called new_users. Make sure one or two of the new
#Usernames are also in the current_users list.
#Loop through the new_users list to see if each new username has already been used.
#If it has, print a message that the person will need to enter a new username.
#If a username has not been used, print a message saying that the username is available.
#Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not
#be accepted. (To do this, you'll need to make a copy of current_users containing the
#lowercase versions of all existing users.)

current_users = ['AJFM88', 'ejfoucault', 'AJFoucault', 'ammonterrey', 'zinedine']

new_users = ['figo', 'pele', 'EJFoucault', 'ajfm88', 'ajfoucault']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"\nSorry, but the username {user} is already taken.")
        print("Please select a different username")
    else:
        print(f"\nThe username {user} is available!")

print("\nThank you for using our login system")