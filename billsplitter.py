import random

bill_value, bill, people, nb_people = 0, dict(), set(), 0


def print_divided_bill():
    print()
    print(bill)


def split_bill():
    global bill

    people_part = round(bill_value / nb_people, 2)
    for guest in people:
        bill[guest] = people_part


def is_someone_lucky():
    global bill, people, nb_people
    print()
    while True:
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        answer = input()
        if answer in ["Yes", "No"]:
            break
    print()
    if answer == "Yes":
        lucky_one = random.choice([key for key in bill.keys()])

        print(lucky_one, "is the lucky one!")
        bill[lucky_one] = 0
        nb_people -= 1
        people.remove(lucky_one)
        split_bill()

    elif answer == "No":
        print("No one is going to be lucky")


def define_dinner_party():
    global bill_value, bill, nb_people, people
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
            people.add(person)
            bill.setdefault(person, 0)
            if len(person) == 0:
                break
        print()
        print("Enter the total bill value:")
        bill_value = int(input())


define_dinner_party()
if nb_people > 0:
    split_bill()
    is_someone_lucky()
    print_divided_bill()
