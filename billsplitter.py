def define_dinner_party():
    print("Enter the number of friends joining (including you):")
    nb_people = int(input())
    print()
    guests = dict()
    if nb_people <= 0:
        print("No one is joining for the party")
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        for _ in range(nb_people):
            person = input()
            guests.setdefault(person, 0)
            if len(person) == 0:
                break
        print()
        print(guests)


define_dinner_party()
