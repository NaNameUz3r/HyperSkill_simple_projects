ingredients_stock = {'water': 400,
              'milk': 540,
              'beans': 120,
              'cups': 9,
              'money': 550}


def main():
    while True:
        action = str(input("Write action (buy, fill, take, remaining, exit):"))
        if action == "buy":
            process_user_choice()
        elif action == "fill":
            replenish_stock()
        elif action == "take":
            extract_money()
        elif action == "remaining":
            status_printer()
        elif action == 'exit':
            exit(0)
        else:
            print("Error, try again")
            main()


def show_stock_values():

    print("The coffee machine has:")
    print(str(ingredients_stock['water']), " of water")
    print(str(ingredients_stock['milk']), " of milk")
    print(str(ingredients_stock['beans']), " of coffee beans")
    print(str(ingredients_stock['cups']), " of disposable cups")
    print(str(ingredients_stock['money']), " of money")


def process_user_choice():
    cup_choice = input("What do you want to buy? 1 - espresso, 2 - latte, "
                       "3 - cappuccino, back - to main menu:")
    if cup_choice == 'back':
        main()
    else:
        make_coffee(int(cup_choice))


def replenish_stock():

    add_water = int(input("Write how many ml of water do you want to add:"))
    ingredients_stock['water'] += add_water
    add_milk = int(input("Write how many ml of milk do you want to add:"))
    ingredients_stock['milk'] += add_milk
    add_beans = int(input("Write how many grams of coffee beans "
                          "do you want to add:"))
    ingredients_stock['beans'] += add_beans
    add_cups = int(input("Write how many cups "
                         "do you want to add:"))
    ingredients_stock['cups'] += add_cups


def extract_money():

    print("I gave you $", ingredients_stock['money'])
    ingredients_stock['money'] = 0


def is_stock_enough(cup):

    if cup == 1:
        if ingredients_stock['water'] < 250:
            return 'water'
        elif ingredients_stock['beans'] < 16:
            return 'beans'
        elif ingredients_stock['cups'] < 1:
            return 'cups'
        else:
            return True

    if cup == 2:
        if ingredients_stock['water'] < 350:
            return 'water'
        elif ingredients_stock['milk'] < 75:
            return 'milk'
        elif ingredients_stock['beans'] < 20:
            return 'beans'
        elif ingredients_stock['cups'] < 1:
            return 'cups'
        else:
            return True

    if cup == 3:
        if ingredients_stock['water'] < 200:
            return 'water'
        elif ingredients_stock['milk'] < 100:
            return 'milk'
        elif ingredients_stock['beans'] < 12:
            return 'beans'
        elif ingredients_stock['cups'] < 1:
            return 'cups'
        else:
            return True


def make_coffee(cup):

    status = is_stock_enough(cup)
    # espresso
    if cup == 1 and status is True:
        print('I have enough resources, making you a coffee!')
        ingredients_stock['water'] -= 250
        ingredients_stock['beans'] -= 16
        ingredients_stock['cups'] -= 1
        ingredients_stock['money'] += 4
        main()
    elif cup == 1 and status is not True:
        print('Sorry, not enough ' + str(status))

    # latte
    if cup == 2 and status is True:
        print('I have enough resources, making you a coffee!')
        ingredients_stock['water'] -= 350
        ingredients_stock['milk'] -= 75
        ingredients_stock['beans'] -= 20
        ingredients_stock['cups'] -= 1
        ingredients_stock['money'] += 7
        main()
    elif cup == 2 and status is not True:
        print('Sorry, not enough ' + str(status))

    # cappuccino
    if cup == 3 and status is True:
        print('I have enough resources, making you a coffee!')
        ingredients_stock['water'] -= 200
        ingredients_stock['milk'] -= 100
        ingredients_stock['beans'] -= 12
        ingredients_stock['cups'] -= 1
        ingredients_stock['money'] += 6
        main()
    elif cup == 3 and status is not True:
        print('Sorry, not enough ' + str(status))


main()

