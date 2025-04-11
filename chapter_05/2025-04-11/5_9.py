# No Users

import time

users = ["Socrates", "Archimedes", "Virgilius", "Cicero", "Augustinus", "Administrator"]
users = []

if users:

    for user in users:
        time.sleep(2)
        if user == "Administrator":
            print(f"It's truly a pleasure to see you, my dear {user}. Would you like to review the state of your Empire?")

        else:
            print(f"What's up {user}?")

else:
    print("We need to find some users!")