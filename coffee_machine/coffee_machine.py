remainings = {'water': 400,
              'milk': 540,
              'beans': 120,
              'cups': 9,
              'money': 550}


def main():
    while True:
        action = str(input("Write action (buy, fill, take, remaining, exit):"))
        if action == "buy":
            buy()
        elif action == "fill":
            fill()
        elif action == "take":
            take()
        elif action == "remaining":
            status_printer()
        elif action == 'exit':
            exit(0)
        else:
            print("Error, try again")
            main()


def status_printer():

    print("The coffee machine has:")
    print(str(remainings['water']), " of water")
    print(str(remainings['milk']), " of milk")
    print(str(remainings['beans']), " of coffee beans")
    print(str(remainings['cups']), " of disposable cups")
    print(str(remainings['money']), " of money")


def buy():
    cup_choice = input("What do you want to buy? 1 - espresso, 2 - latte, "
                       "3 - cappuccino, back - to main menu:")
    if cup_choice == 'back':
        main()
    else:
        coffee_maker(int(cup_choice))


def fill():

    add_water = int(input("Write how many ml of water do you want to add:"))
    remainings['water'] += add_water
    add_milk = int(input("Write how many ml of milk do you want to add:"))
    remainings['milk'] += add_milk
    add_beans = int(input("Write how many grams of coffee beans "
                          "do you want to add:"))
    remainings['beans'] += add_beans
    add_cups = int(input("Write how many cups "
                         "do you want to add:"))
    remainings['cups'] += add_cups


def take():

    print("I gave you $", remainings['money'])
    remainings['money'] = 0


def amount_checker(cup):

    if cup == 1:
        if remainings['water'] < 250:
            return 'water'
        elif remainings['beans'] < 16:
            return 'beans'
        elif remainings['cups'] < 1:
            return 'cups'
        else:
            return True

    if cup == 2:
        if remainings['water'] < 350:
            return 'water'
        elif remainings['milk'] < 75:
            return 'milk'
        elif remainings['beans'] < 20:
            return 'beans'
        elif remainings['cups'] < 1:
            return 'cups'
        else:
            return True

    if cup == 3:
        if remainings['water'] < 200:
            return 'water'
        elif remainings['milk'] < 100:
            return 'milk'
        elif remainings['beans'] < 12:
            return 'beans'
        elif remainings['cups'] < 1:
            return 'cups'
        else:
            return True


def coffee_maker(cup):

    status = amount_checker(cup)
    # espresso
    if cup == 1 and status is True:
        print('I have enough resources, making you a coffee!')
        remainings['water'] -= 250
        remainings['beans'] -= 16
        remainings['cups'] -= 1
        remainings['money'] += 4
        main()
    elif cup == 1 and status is not True:
        print('Sorry, not enough ' + str(status))

    # latte
    if cup == 2 and status is True:
        print('I have enough resources, making you a coffee!')
        remainings['water'] -= 350
        remainings['milk'] -= 75
        remainings['beans'] -= 20
        remainings['cups'] -= 1
        remainings['money'] += 7
        main()
    elif cup == 2 and status is not True:
        print('Sorry, not enough ' + str(status))

    # cappuccino
    if cup == 3 and status is True:
        print('I have enough resources, making you a coffee!')
        remainings['water'] -= 200
        remainings['milk'] -= 100
        remainings['beans'] -= 12
        remainings['cups'] -= 1
        remainings['money'] += 6
        main()
    elif cup == 3 and status is not True:
        print('Sorry, not enough ' + str(status))


main()

