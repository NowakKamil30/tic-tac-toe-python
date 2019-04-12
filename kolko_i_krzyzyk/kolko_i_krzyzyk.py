game_board={"top_l":" ","top_m":" ","top_r":" ","mid_l":" ","mid_m":" ","mid_r":" ",
            "low_l":" ","low_m":" ","low_r":" ",}
turn="X"
def draw_board(board):
    print("|"+board["top_l"]+"|"+board["top_m"]+"|"+board["top_r"]+"|")
    print("|"+board["mid_l"]+"|"+board["mid_m"]+"|"+board["mid_r"]+"|")
    print("|"+board["low_l"]+"|"+board["low_m"]+"|"+board["low_r"]+"|")
    print("\n")
def make_move(game_board,turn):
    key=input("Wybierz pole: ")
    key=key.lower()
    if key in game_board:
        if game_board[key]==" ":
            game_board[key]=turn
            if turn=="X":
                return "O"
            else:
               return "X"
        else:
            print("pole jest zajete")
    else:
        print("nie ma takiego pola")
    return turn
def check_board(board,turn):
        if board["top_l"]!=" " and (board["top_l"]==board["top_m"] and board["top_m"]==board["top_r"])\
        or board["top_l"]!=" " and (board["top_l"]==board["mid_m"] and board["top_l"]==board["low_r"])\
        or board["top_l"]!=" " and (board["top_l"]==board["mid_l"] and board["top_l"]==board["low_l"])\
        or board["mid_l"]!=" " and (board["mid_l"]==board["mid_m"] and board["mid_m"]==board["mid_r"])\
        or board["low_l"]!=" " and (board["low_l"]==board["low_m"] and board["low_m"]==board["low_r"])\
        or board["top_m"]!=" " and (board["top_m"]==board["mid_m"] and board["top_m"]==board["low_m"])\
        or board["top_r"]!=" " and ( board["top_r"]==board["mid_r"] and board["top_r"]==board["low_r"])\
        or board["top_r"]!=" " and  (board["top_r"]==board["mid_m"] and board["top_r"]==board["low_l"]):
            if turn=="X":
                return 1;
            else:
                return 2;
        return 0;

while True:
    draw_board(game_board)
    turn= make_move(game_board,turn)
    check=check_board(game_board,turn)
    if check:
        draw_board(game_board)
        if check==1:
            print("wygrało O")
            break
        elif check==2:
            print("wygrało X")
            break

