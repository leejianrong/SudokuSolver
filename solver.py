import math

board1 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def solve(board):

    # find empty square
    find = find_empty(board)

    # sudoku is solved if we can't find an empty square
    # provide row and col of empty square if one is found
    if not find:
        return True
    else:
        row, col = find

    # iterate over the 9 digits
    for i in range(1, 10):

        if valid(board, i, row, col): # if we find a valid digit, insert it

            board[row][col] = i

            if solve(board): # recursively call solve function
                return True
            
            # code reaches this line when solve() returns False
            # this occurs when all 9 digits are invalid
            board[row][col] = 0

    return False

def valid(board, num, row, col):

    for i in range(len(board)): # check column for duplicates by going over each row
        if board[i][col] == num and i != row: # check for duplicates; skip over the current position
            return False
        
    for i in range(len(board[0])): # check row for dupes
        if board[row][i] == num and i != col:
            return False
    
    # check box
    s_length = int(math.sqrt(len(board)))
    box_row = row // s_length
    box_col = col // s_length
    start_row = box_row * s_length
    start_col = box_col * s_length

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num and i != row and j != col:
                return False
            
    # if we make it to the end, attempted number is valid       
    return True



def print_board(board):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j # row, col
            
    return None

print("Before: ")
print_board(board1)
print("")
solve(board1)
print("After:")
print_board(board1)


