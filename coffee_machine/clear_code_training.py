stock_values_container = {'water': 400,
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
            replenish_stock()
        elif action == "take":
            collect_money()
        elif action == "remaining":
            status_printer()
        elif action == 'exit':
            exit(0)
        else:
            print("Error, try again")
            main()


def status_printer():
    print("The coffee machine has:")
    print(str(stock_values_container['water']), " of water")
    print(str(stock_values_container['milk']), " of milk")
    print(str(stock_values_container['beans']), " of coffee beans")
    print(str(stock_values_container['cups']), " of disposable cups")
    print(str(stock_values_container['money']), " of money")


def buy():
    cup_choice = input("What do you want to buy? 1 - espresso, 2 - latte, "
                       "3 - cappuccino, back - to main menu:")
    if cup_choice == 'back':
        main()
    else:
        coffee_maker(int(cup_choice))


def replenish_stock():
    water_supplement = int(input("Write how many ml of water do you want to add:"))
    stock_values_container['water'] += water_supplement

    milk_supplement = int(input("Write how many ml of milk do you want to add:"))
    stock_values_container['milk'] += milk_supplement

    beans_supplement = int(input("Write how many grams of coffee beans "
                                 "do you want to add:"))
    stock_values_container['beans'] += beans_supplement

    cups_supplement = int(input("Write how many cups "
                                "do you want to add:"))
    stock_values_container['cups'] += cups_supplement


def collect_money():
    print("I gave you $", stock_values_container['money'])
    stock_values_container['money'] = 0


def is_ingredients_in_stock(product_id):
    if product_id == 1:
        if stock_values_container['water'] < 250:
            return 'water'
        elif stock_values_container['beans'] < 16:
            return 'beans'
        elif stock_values_container['cups'] < 1:
            return 'cups'
        else:
            return True

    if product_id == 2:
        if stock_values_container['water'] < 350:
            return 'water'
        elif stock_values_container['milk'] < 75:
            return 'milk'
        elif stock_values_container['beans'] < 20:
            return 'beans'
        elif stock_values_container['cups'] < 1:
            return 'cups'
        else:
            return True

    if product_id == 3:
        if stock_values_container['water'] < 200:
            return 'water'
        elif stock_values_container['milk'] < 100:
            return 'milk'
        elif stock_values_container['beans'] < 12:
            return 'beans'
        elif stock_values_container['cups'] < 1:
            return 'cups'
        else:
            return True


def coffee_maker(product_id):
    order_status = is_ingredients_in_stock(product_id)
    # espresso
    if product_id == 1 and order_status is True:
        print('I have enough resources, making you a coffee!')
        stock_values_container['water'] -= 250
        stock_values_container['beans'] -= 16
        stock_values_container['cups'] -= 1
        stock_values_container['money'] += 4
        main()
    elif product_id == 1 and order_status is not True:
        print('Sorry, not enough ' + str(order_status))

    # latte
    if product_id == 2 and order_status is True:
        print('I have enough resources, making you a coffee!')
        stock_values_container['water'] -= 350
        stock_values_container['milk'] -= 75
        stock_values_container['beans'] -= 20
        stock_values_container['cups'] -= 1
        stock_values_container['money'] += 7
        main()
    elif product_id == 2 and order_status is not True:
        print('Sorry, not enough ' + str(order_status))

    # cappuccino
    if product_id == 3 and order_status is True:
        print('I have enough resources, making you a coffee!')
        stock_values_container['water'] -= 200
        stock_values_container['milk'] -= 100
        stock_values_container['beans'] -= 12
        stock_values_container['cups'] -= 1
        stock_values_container['money'] += 6
        main()
    elif product_id == 3 and order_status is not True:
        print('Sorry, not enough ' + str(order_status))


if __name__ == "__main__":
    main()
