import random


def print_welcome_rules():

    print("""
    
██████╗  ██████╗ ███╗   ███╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔═══██╗████╗ ████║██║████╗  ██║██╔═══██╗
██║  ██║██║   ██║██╔████╔██║██║██╔██╗ ██║██║   ██║
██║  ██║██║   ██║██║╚██╔╝██║██║██║╚██╗██║██║   ██║
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║██║ ╚████║╚██████╔╝
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝       

Hey! It's a simple domino game against your computer!
When it's your turn, make your choice by entering
the number of piece that you have in your stock.

If you want to put this piece on the right side
domino snake - enter a positive number!
If on the left - negative!

Good luck buddy! 
                     
    """)
    _ = input('Press Enter to start game!')


def print_game_condition(stock, computer, snake_pieces, player):
    if len(snake_pieces) > 6:
        print('=' * 70,
              '\nStock size:', len(stock),
              '\nComputer pieces:', len(computer),
              '\n\n', *snake_pieces[:3], '...', *snake_pieces[-3:],
              '\n\nYour pieces:')
    else:
        print('=' * 70,
              '\nStock size:', len(stock),
              '\nComputer pieces:', len(computer),
              '\n\n', *snake_pieces,
              '\n\nYour pieces:')
    for piece in range(len(player)):
        print('{}:{}'.format(piece + 1, player[piece]))


def check_game_status(computer_check, snake_check, player_check, stock):
    if len(player_check) == 0:
        print('\nStatus: The game is over. You won!')
        return True
    if len(computer_check) == 0:
        print('\nStatus: The game is over. The computer won!')
        return True
    if snake_check[0][0] == snake_check[-1][1] and (
            sum(x.count(snake_check[0][0]) for x in snake_check) == 8):
        print('\nStatus: The game is over. It\'s a draw!')
        return True
    if stock == [] and pass_counter >= 2:
        print('\nStatus: The game is over. It\'s a draw!')
        return True


print_welcome_rules()

# Game initialization
while True:
    stock_pieces = [[x, y] for x in range(0, 7) for y in range(x, 7)]
    computer_pieces, player_pieces, snake = [list() for _ in range(0, 3)]
    next_move = ''
    pass_counter = 0

    for _ in range(0, 7):
        n = random.randrange(0, len(stock_pieces), 1)
        computer_pieces.append(stock_pieces[n])
        stock_pieces.remove(stock_pieces[n])

        m = random.randrange(0, len(stock_pieces), 1)
        player_pieces.append(stock_pieces[m])
        stock_pieces.remove(stock_pieces[m])

    for i in range(6, -1, -1):
        if [i, i] in player_pieces:
            snake.append([i, i])
            player_pieces.remove([i, i])
            next_move = 'computer'
            break

        if [i, i] in computer_pieces:
            snake.append([i, i])
            computer_pieces.remove([i, i])
            next_move = 'player'
            break

    if next_move:
        break


print_game_condition(stock_pieces, computer_pieces, snake, player_pieces)

# Interactive game part
while True:

    if check_game_status(computer_pieces, snake, player_pieces, stock_pieces):
        break

    if next_move == 'player':

        move = input("\nStatus: It's your turn to make a move. Enter your command.\n")

        while True:
            if move.lstrip('-').isdigit() and abs(int(move)) <= len(player_pieces):
                move = int(move)

                if int(move) == 0 and stock_pieces == []:
                    next_move = 'computer'
                    pass_counter += 1
                    break

                elif int(move) == 0 and stock_pieces != []:
                    n = random.randrange(0, len(stock_pieces), 1)
                    player_pieces.append(stock_pieces[n])
                    stock_pieces.remove(stock_pieces[n])
                    next_move = 'computer'
                    break

                if move > 0 and snake[-1][1] == player_pieces[move - 1][0]:
                    snake.append(player_pieces[move - 1])
                    player_pieces.remove(player_pieces[move - 1])
                    next_move = 'computer'
                    break

                elif move > 0 and snake[-1][1] == player_pieces[move - 1][1]:
                    snake.append(player_pieces[move - 1][::-1])
                    player_pieces.remove(player_pieces[move - 1])
                    next_move = 'computer'
                    break

                elif move < 0 and snake[0][0] == player_pieces[abs(move) - 1][1]:
                    snake.insert(0, player_pieces[abs(move) - 1])
                    player_pieces.remove(player_pieces[abs(move) - 1])
                    next_move = 'computer'
                    break

                elif move < 0 and snake[0][0] == player_pieces[abs(move) - 1][0]:
                    snake.insert(0, player_pieces[abs(move) - 1][::-1])
                    player_pieces.remove(player_pieces[abs(move) - 1])
                    next_move = 'computer'
                    break

                else:
                    move = input('Illegal move. Please try again.\n')

            else:
                move = input('Invalid input. Please try again.\n')

    else:
        foo = input("\nStatus: Computer is about to make a move. Press Enter to continue...\n")

        sum_list = computer_pieces + snake
        joined_pieces = []
        for i in sum_list:
            for j in i:
                joined_pieces.append(j)

        analysis_mask = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

        for i in joined_pieces:
            analysis_mask[i] += 1

        domino_values = {}

        for i in range(len(computer_pieces)):
            domino_values[computer_pieces.index(computer_pieces[i])] = (
                    analysis_mask[computer_pieces[i][0]] + analysis_mask[computer_pieces[i][1]])

        domino_values = sorted(domino_values.items(), key=lambda x: x[1], reverse=True)
        domino_values = dict(domino_values)
        play_pieces_indexes = [*domino_values]

        for i in play_pieces_indexes:

            move = play_pieces_indexes[i] + 1

            if move == len(play_pieces_indexes) and stock_pieces != []:
                n = random.randrange(0, len(stock_pieces), 1)
                computer_pieces.append(stock_pieces[n])
                stock_pieces.remove(stock_pieces[n])
                next_move = 'player'
                break

            elif move == len(play_pieces_indexes) and stock_pieces == []:
                next_move = 'player'
                pass_counter += 1
                break

            elif move > 0 and snake[-1][1] == computer_pieces[move - 1][0]:
                snake.append(computer_pieces[move - 1])
                computer_pieces.remove(computer_pieces[move - 1])
                next_move = 'player'
                break

            elif move > 0 and snake[-1][1] == computer_pieces[move - 1][1]:
                snake.append(computer_pieces[move - 1][::-1])
                computer_pieces.remove(computer_pieces[move - 1])
                next_move = 'player'
                break

            elif move < 0 and snake[0][0] == computer_pieces[abs(move) - 1][1]:
                snake.insert(0, computer_pieces[abs(move) - 1])
                computer_pieces.remove(computer_pieces[abs(move) - 1])
                next_move = 'player'
                break

            elif move < 0 and snake[0][0] == computer_pieces[abs(move) - 1][0]:
                snake.insert(0, computer_pieces[abs(move) - 1][::-1])
                computer_pieces.remove(computer_pieces[abs(move) - 1])
                next_move = 'player'
                break

    print_game_condition(stock_pieces, computer_pieces, snake, player_pieces)

