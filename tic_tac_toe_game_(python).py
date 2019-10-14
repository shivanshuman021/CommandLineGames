from IPython.display import clear_output

print("_______  ___  _____    _______   /\    _____    _______  _____   ____      ")
print("   |      |   |           |     /  \   |           |    |     | |          ") 
print("   |      |   |           |    /----\  |           |    |     | |---   ")
print("   |      |   |____       |   /      \ |____       |    |_____| |____\n\n")

y=input("Press X to continue...")
clear_output()

print("Follow the following instructions :")
print("\t First decide who is player 1 amongst yourselves \n\n\n\n")
print("\t Decided ,eh ? ")
Y=input("Press C to continue..")
if Y=="C":
    
    print("The board will be shown in following manner")
    print("\t  [7]  |  [8]  |  [9]")
    print("\t-----------------")
    print("\t  [4]  |  [5]  |  [6]")
    print("\t-----------------")
    print("\t  [1]  |  [2]  |  [3]\n")
    
    
    print("Suppose you want to put your mark at position 7 , enter this number in the dialog box when computer asks \n")

board = [" "," "," "," "," "," "," "," "," "," "]

def display_board(board):
    clear_output()
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print(f"-----------------")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print(f"-----------------")
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")


x=input(" Player 1 please choose your symbol -- X or O " )

if x== "X":
    while True:
        i=int(input("Enter the place index to input "))
        board[i]=input("WHAT IS YOUR SYMBOL ,Hmmm , I FORGOT :) ? ENTER IT HERE ")
        display_board(board)
        if board[7]==board[8]==board[9]=="X":
            print("Player 1 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[7]==board[8]==board[9]=="O":    
            print("Player 2 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[6]==board[4]==board[5]=="X":
            print("Player 1 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif  board[6]==board[4]==board[5]=="O":   
            print("Player 2 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[1]==board[2]==board[3]=="X":
            print("Player 1 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[1]==board[2]==board[3]=="O":   
            print("Player 2 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[7]==board[8]==board[9]=="X":
            print("Player 1 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[7]==board[8]==board[9]=="O":    
            print("Player 2 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[1]==board[4]==board[7]=="X":
            print("Player 1 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[1]==board[4]==board[7]=="O":   
            print("Player 2 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[2]==board[5]==board[8]=="X":
            print("sPlayer 1 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[2]==board[5]==board[8]=="O":   
            print("Player 2 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[3]==board[6]==board[9]=="X":
            print("Player 1 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[3]==board[6]==board[9]=="O":   
            print("Player 2 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[3]==board[5]==board[7]=="X":
            print("Player 1 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[3]==board[5]==board[7]=="O":  
            print("Player 2 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[1]==board[5]==board[9]=="X":
            print("Player 1 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[1]==board[5]==board[9]=="O":   
            print("Player 2 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        else:
            continue
            
if x=="O":
    while True:
        i=int(input("Enter the place index to input "))
        board[i]=input("Player 1's turn ")
        display_board(board)
        if board[7]==board[8]==board[9]=="X":
            print("Player 1 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[7]==board[8]==board[9]=="O":    
            print("Player 2 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[6]==board[4]==board[5]=="X":
            print("Player 1 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif  board[6]==board[4]==board[5]=="O":   
            print("Player 2 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[1]==board[2]==board[3]=="X":
            print("Player 1 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[1]==board[2]==board[3]=="O":   
            print("Player 2 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[7]==board[8]==board[9]=="X":
            print("Player 1 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[7]==board[8]==board[9]=="O":    
            print("Player 2 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[1]==board[4]==board[7]=="X":
            print("Player 1 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[1]==board[4]==board[7]=="O":   
            print("Player 2 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[2]==board[5]==board[8]=="X":
            print("sPlayer 1 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[2]==board[5]==board[8]=="O":   
            print("Player 2 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[3]==board[6]==board[9]=="X":
            print("Player 1 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[3]==board[6]==board[9]=="O":   
            print("Player 2 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[3]==board[5]==board[7]=="X":
            print("Player 1 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[3]==board[5]==board[7]=="O":   
            print("Player 2 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[1]==board[5]==board[9]=="X":
            print("Player 1 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        elif board[1]==board[5]==board[9]=="O":   
            print("Player 2 won")
            print("Don't give input in below box , hi hi hi hi , you can't cheat on computer")
        else:
            continue