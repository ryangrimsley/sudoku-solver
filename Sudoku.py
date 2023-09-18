
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
    ]

def print_board(board):
    #print board
    for i in range(len(board)):
        #if we are on the third row, print a horizontal line
        if i % 3 == 0 and i != 0:
            print("-"*23)

        for j in range(len(board[0])):
            #if we are on third column, print a vertical line
            if j % 3 == 0 and j != 0:
                print(" |",end="")

            if j != len(board)-1:
                print("",board[i][j],end="")
            else:
                print("",board[i][j])

def find_empty(board):
    #return row,col of empty space in board
    for i in range(len(board)):

        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) #row,col
    return None
            

def isValid(board, value, position):
    #return True if value passed is a valid value at the position passed
    for i in range(len(board)):
        #(only can do both in the same for loop because sudoku box is a square)
        #loop through rows and check if any number is the same as our number vertically
        if board[i][position[1]] == value and position[0] != i:
            return False
        #loop through columns and check if any number is the same as our number horizontally
        if board[position[0]][i] == value and position[1] != i:
            return False
    
    #find what quadrarnt of box the position is in
    box_x = position[1] // 3
    box_y = position[0] // 3

    #loop through the 9 values in that box
    for i in range(3):
        for j in range(3):
            if board[i+(3*box_y)][j+(3*box_x)] == value and (i+(3*box_y),j+(3*box_x)) != position:
                return False

    return True

def solve(board):
    #return True if the board is solved, False if not
    find = find_empty(board)
    #if there are no empty squares, return True
    if not find:
        return True
    
    row,col = find
    for i in range(1,10):
        #try all numbers in the open square, if one is valid, set it as new value in the square
        if isValid(board,i,find):
            board[row][col] = i
            #after setting valid value as the empty square, solve again, and if it can, return true, 
            # setting off function again, until the if not find statement returns true
            # if the next call of solve does not return true(a valid solution is not found), then reset this iterations position and try again
            if solve(board):
                return True
        
            board[row][col] = 0

    return False

def main():
    print_board(board)
    solve(board)
    print("    ")
    print_board(board)

if __name__ == "__main__":
    main()
