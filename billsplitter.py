import random

bill_value, guests, nb_people = 0, dict(), 0


def print_divided_bill():
    print()
    print(guests)


def split_bill():
    global guests

    people_part = round(bill_value / nb_people, 2)
    for guest in guests:
        guests[guest] = people_part


def is_someone_lucky():
    print()
    while True:
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        answer = input()
        if answer in ["Yes", "No"]:
            break
    print()
    if answer == "Yes":
        lucky_one = random.choice([key for key in guests.keys()])
        print(lucky_one, "is the lucky one!")
    elif answer == "No":
        print("No one is going to be lucky")


def define_dinner_party():
    global bill_value, guests, nb_people
    print("Enter the number of friends joining (including you):")
    nb_people = int(input())
    print()
    try:
        message = "No one is joining for the party"
        assert nb_people > 0, message
    except AssertionError as err:
        print(err)
        nb_people = 0
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        for _ in range(nb_people):
            person = input()
            guests.setdefault(person, 0)
            if len(person) == 0:
                break
        print()
        print("Enter the total bill value:")
        bill_value = int(input())


define_dinner_party()
if nb_people > 0:
    split_bill()
    #    print_divided_bill()
    is_someone_lucky()
