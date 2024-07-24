known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "George", "Harry"]

while True:
    print("Hi! I am a security robot.")
    name = input("What is your name? ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system? (Y/N)").lower()

        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No problem.")

    else:
        print("Hmm... I don't think I have met you yet, {}".format(name))
        add_me = input("Would you like to be added to the system? (Y/N)").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("No problem, see you around!")
