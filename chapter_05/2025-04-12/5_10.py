# Checking Usernames

# List of current users
current_users = ["Aristophanes", "Aesopus", "Ptolomeus", "Diogenes", "Cleopatra"]

# List of current users in lowercase
current_users = [user.lower() for user in current_users]

# List of new users
new_users = ["Menelaus", "Aesopus", "Horatius", "Ovidius", "Cleopatra"]

# Check if the new user is in the list of current_users
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"You're not original enough: {new_user.title()} is already in use.")
    else:
        print(f"The username {new_user.title()} is available.")
