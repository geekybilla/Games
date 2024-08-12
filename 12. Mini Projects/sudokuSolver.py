#creating a Sudoku Solver using the concept of Backtracking:

#validation fucntion -- to check if a certain try is valid or not
def is_valid_move(grid, row, col, number):

    #same number not in same row
    for x in range(9):
        if grid[row][x]==number:
            return False

    #same number not in same column
    for x in range(9):
        if grid[x][col]==number:
            return False
        
    #same number not in same corner
    corner_row= row - row % 3
    corner_col=col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False
            
    return True


#Recursive solving Function
def solve(grid, row, col):

    #base condition
    #checking Completion of Sudoku
    if col== 9: #overdone colum
        if row == 8: #last row
            return True
        row +=1 #go to the next row
        col = 0 #start with the 1st column
    
    if grid[row][col] > 0: #if the cell is empty
        return solve(grid, row, col+1) #in further recursive calls the value of columns will increase as col in the parameter will be passed as col + 1 as the recursive argument 
    
    #checking for all indivisual possibiities
    for num in range(1,10):

        if is_valid_move(grid, row, col, num): #if valid

            grid[row][col] = num

            if solve(grid, row, col +1): 
                return True
        
        grid[row][col]= 0
    
    return False

#assuming the initial Sudoku entries would be valid
#assuming value 0 means the cell is empty
grid= [[0, 0, 0, 0, 0, 0 , 0, 0, 0],
       [0, 0, 0, 0, 0, 0 , 0, 0, 0],
       [0, 0, 0, 0, 0, 0 , 0, 0, 0],
       [0, 0, 0, 0, 0, 0 , 0, 0, 0],
       [0, 0, 0, 0, 0, 0 , 0, 0, 0],
       [0, 0, 0, 0, 0, 0 , 0, 0, 0],
       [0, 0, 0, 0, 0, 0 , 0, 0, 0],
       [0, 0, 0, 0, 0, 0 , 0, 0, 0],
       [0, 0, 0, 0, 0, 0 , 0, 0, 0]]




if solve(grid, 0, 0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
else:
    print("no solution for This Sudoku")


# Backtracking --  backtracking is an algorithmic technique that uses brute force to find all solutions to a problem. It involves gradually building a set of all possible solutions, and then removing any solutions that don't meet certain constraints. Backtracking is based on the Depth First Search (DFS) approach. 