#Algorithm for Tic Tac Toe

#Board
#players
#handle turns
#check who is the winner
#check row
#check col
#check dia
#tie

board=["-","-","-",
       "-","-","-",
       "-","-","-"]

current_player="X"
game_is_playing=True
winner=None



def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def trun_specified():
    global current_player
    if current_player == "O":
        print("Its O's Turn...!")
    elif current_player == "X":
        print("Its X's Turn...!")

def handle_turn():
            global current_player
            position = int(input("Enter the position of your choice from 0 to 8:"))

            if position <= 8:
                board[position] = current_player
            elif position >8:
                print("Enter Valid Position...")
                position = int(input("Enter the position of your choice from 0 to 8:"))
                board[position] = current_player


def swap_player():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"



def check_the_winner():
    global winner
    #check row
    #check col
    #check dia
    row_winner=check_row()
    if row_winner:
        winner=row_winner

    col_winner=check_col()
    if col_winner:
        winner=col_winner

    dia_winner=check_dia()
    if dia_winner:
        winner=dia_winner



def check_row():
    global game_is_playing
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_is_playing=False

    if row_1:
        return board[2]
    elif row_2:
        return board[4]
    elif row_3:
        return board[6]

def check_col():
    global game_is_playing
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_is_playing = False

    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[5]

def check_dia():
    global game_is_playing
    dia_1 = board[0] == board[4] == board[8] != "-"
    dia_2 = board[2] == board[4] == board[6] != "-"


    if dia_1 or dia_2:
        game_is_playing = False

    if dia_1:
        return board[0]
    elif dia_2:
        return board[4]

def check_tie():
    global game_is_playing
    if "-" not in board:
        print("Match ended with a tie....!")
        game_is_playing=False



def play_game():

    while game_is_playing:#while False:


        display_board()
        print()

        trun_specified()

        handle_turn()

        #position_valid()

        swap_player()

        check_the_winner()

        check_tie()


    global winner
    if winner=="X" or winner=="O":
        print("Ewww.!!! winner is",winner)

play_game()