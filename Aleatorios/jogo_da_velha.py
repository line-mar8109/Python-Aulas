board = [' ' for x in range(10)]


# peguei esse codigo no sit -> https://copyassignment.com/tic-tac-toe-python/
def insert_letter(letter, pos):
    board[pos] = letter


def space_is_free(pos):
    return board[pos] == " "


def print_board(boarda):
    print(" " + boarda[1] + "| " + boarda[2] + "| " + boarda[3])
    print("---------")
    print(" " + boarda[4] + "| " + boarda[5] + "| " + boarda[6])
    print("---------")
    print(" " + boarda[7] + "| " + boarda[8] + "| " + boarda[9])


def is_winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le))


def play_move():
    run = True
    while run:
        move = input("Please select a position to place an 'X' (1-9): ")
        try:
            move = int(move)
            if 0 < move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter("x", move)
                else:
                    print("Sorry this space is occupied")
            else:
                print("Please type the number within the range")
        except IndexError:
            print("Please type a number. ")


def comp_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    for let in ['o', 'x']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move
    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)
    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move
    if 5 in possible_moves:
        move = 5
        return move
    edges_open = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)
    if len(edges_open) > 0:
        move = select_random(edges_open)
    return move


def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def is_board_full(boarda):
    if boarda.count(" ") > 1:
        return False
    else:
        return True


def main():
    print("welcome tic tac toe")
    print_board(board)
    while not (is_board_full(board)):
        if not (is_winner(board, "o")):
            play_move()
            print_board(board)
        else:
            print("Sorry, O's won this time! ")
            break
        if not (is_winner(board, "x")):
            move = comp_move()
            if move == 0:
                print("Tie game")
            else:
                insert_letter("o", move)
                print("Computer placed an 'o' in position", move, ":")
                print_board(board)
        else:
            print("X's won this time! Good job")
            break
    if is_board_full(board):
        print("Tie game")


main()
