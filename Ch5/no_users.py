#If the list is empty, print the message "We need to find some users!"


usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello there, {username}, I hope you are well today!")

else:
    print("We need to find some users!!!")