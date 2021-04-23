import random


def message(stock, computer, snake_pieces, player):
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


def winner(computer_check, snake_check, player_check):
    if len(player_check) == 0:
        print('\nStatus: The game is over. You won!')
        return True
    if len(computer_check) == 0:
        print('\nStatus: The game is over. The computer won!')
        return True
    if snake_check[0][0] == snake_check[-1][1] and sum(x.count(snake_check[0][0]) for x in snake_check) == 8:
        print('\nStatus: The game is over. It\'s a draw!')
        return True


while True:
    stock_pieces = [[x, y] for x in range(0, 7) for y in range(x, 7)]
    computer_pieces, player_pieces, snake = [list() for _ in range(0, 3)]
    next_move = ''

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

message(stock_pieces, computer_pieces, snake, player_pieces)

while True:

    if winner(computer_pieces, snake, player_pieces):
        break

    if next_move == 'player':

        move = input("\nStatus: It's your turn to make a move. Enter your command.\n")

        while True:
            if move.lstrip('-').isdigit() and abs(int(move)) <= len(player_pieces):
                move = int(move)

                if int(move) == 0 and stock_pieces == []:
                    next_move = 'computer'
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
        move = input("\nStatus: Computer is about to make a move. Press Enter to continue...\n")

        while True:

            move = random.randrange(-len(computer_pieces), len(computer_pieces), 1)

            if move == 0 and stock_pieces != []:
                n = random.randrange(0, len(stock_pieces), 1)
                computer_pieces.append(stock_pieces[n])
                stock_pieces.remove(stock_pieces[n])
                next_move = 'player'
                break

            elif move == 0 and stock_pieces == []:
                next_move = 'player'
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

    message(stock_pieces, computer_pieces, snake, player_pieces)

