from secrets import choice


Board =[" " for i in range (9)]

def print_Board():
    row1="| {} | {} | {} |".format(Board[0],Board[1],Board[2])
    row2="| {} | {} | {} |".format(Board[3],Board[4],Board[5])
    row3="| {} | {} | {} |".format(Board[6],Board[7],Board[8])

    print(row1)
    print(row2)
    print(row3)
    print()

def player(icon):
    if icon=="X":
        number=1
    elif icon=="O":
        number=2 
    print(f"Enter your move {number}")


    choice=int(input("Enter your move(1-9) :").strip())
    if Board[choice-1]==" ":
        Board[choice-1]=icon
    else:
        print()
        print("this place is taken")
    
def victory(icon):
    if(Board[0]==icon and Board[1]==icon and Board[2]==icon) or \
      (Board[3]==icon and Board[4]==icon and Board[5]==icon) or \
      (Board[6]==icon and Board[7]==icon and Board[8]==icon) or \
      (Board[0]==icon and Board[4]==icon and Board[8]==icon) or \
      (Board[2]==icon and Board[4]==icon and Board[6]==icon) or \
      (Board[0]==icon and Board[3]==icon and Board[6]==icon) or \
      (Board[2]==icon and Board[5]==icon and Board[8]==icon) or \
      (Board[1]==icon and Board[4]==icon and Board[7]==icon): 
      return True
    else:
        return False

def Draw():
    if " " not in Board:
        return True
    else:
        return False

while True:
    print_Board()
    player("X")
    print_Board()
    if victory("X"):
        print("X Wins,Hurray!")
        break
    elif Draw():
        print("Match is draw.")
        break
    player("O")
    print_Board()
    if victory("O"):
        print("O wins,Hadippay")
        break
    elif Draw():
        print("Match is draw.")
        break
        