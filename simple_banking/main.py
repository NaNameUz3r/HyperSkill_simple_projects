import random
import sqlite3
import itertools

db_container = sqlite3.connect('card.s3db')


def check_and_create_db():
    try:
        db_cursor = db_container.cursor()
        db_cursor.execute("CREATE TABLE card("
                          "id INTEGER, "
                          "number TEXT, "
                          "pin TEXT, "
                          "balance INTEGER DEFAULT 0);")
    except sqlite3.OperationalError:
        pass


def take_user_command():
    print("1. Create an account\n"
          "2. Log into account\n"
          "0. Exit\n")

    command = input()
    return command


def create_user_account():

    card_number = generate_new_card_number()
    pin_code = generate_new_pin_code()

    db_cursor = db_container.cursor()
    db_cursor.execute("INSERT INTO card(id, number, pin) VALUES " + "("
                      + str(random.randint(0, 999999)) + ", "
                      + str(card_number) + ", "
                      + str(pin_code)
                      + ");")

    db_cursor.execute("COMMIT;")

    print("Your card has been created\n"
          "Your card number:\n" +
          str(card_number) +
          "\nYour card PIN:\n" +
          str(pin_code) + "\n")


def generate_new_card_number():

    db_cursor = db_container.cursor()
    db_cursor.execute("SELECT number FROM card")
    results = db_cursor.fetchall()
    results = [i for i in itertools.chain(*results)]

    bank_identification_number = '400000'

    while True:
        card_template = bank_identification_number + \
                        str(format(random.randint(000000000, 999999999), '09d'))

        number_to_check = [int(digit) for digit in card_template]

        for digit in range(0, len(number_to_check), 2):
            number_to_check[digit] *= 2

        for digit in range(len(number_to_check)):
            if number_to_check[digit] > 9:
                number_to_check[digit] -= 9
        checksum = sum(number_to_check)

        if checksum % 10 == 0:
            appendix = 0
        else:
            appendix = 10 - checksum % 10
        if card_template + str(appendix) in results:
            continue
        else:
            card_number = card_template + str(appendix)
            return card_number


def generate_new_pin_code():

    pin_code = str(format(random.randint(0000, 9999), '04d'))
    return pin_code


def is_account_exist_and_pin_correct(user_number, user_pin):

    db_cursor = db_container.cursor()
    db_cursor.execute("SELECT number, pin FROM card")
    results = db_cursor.fetchall()
    results = [i for i in itertools.chain(*results)]
    return user_number in results and (
            results[results.index(user_number) + 1] == user_pin)


def processing_logged_user(user_number):

    print("You have successfully logged in!\n")
    current_card = user_number
    while True:
        print("1. Balance\n"
              "2. Log out\n"
              "0. Exit\n")
        account_command = input()
        if account_command.isdigit() and account_command == "1":
            fetch_and_print_user_balance(current_card)

        elif account_command.isdigit() and account_command == "2":
            print("You have successfully logged out!\n")
            break
        elif account_command.isdigit() and account_command == "0":
            exit(0)


def fetch_and_print_user_balance(card_number):

    db_cursor = db_container.cursor()
    db_cursor.execute("SELECT balance FROM card WHERE number = '" + card_number + "';")
    balance = db_cursor.fetchone()

    print("Balance: " + str(balance[0]) + "\n")


def main():
    while True:

        command = take_user_command()

        if command.isdigit() and command == "1":
            create_user_account()

        elif command.isdigit() and command == "2":

            user_number = input("Enter your card number:\n")
            user_pin = input("Enter your PIN:\n")

            if is_account_exist_and_pin_correct(user_number, user_pin):

                processing_logged_user(user_number)

            else:
                print("Wrong card number or PIN!\n")

        elif command.isdigit() and command == "0":
            exit(0)


check_and_create_db()
main()

