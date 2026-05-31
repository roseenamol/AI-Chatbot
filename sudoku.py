# Efficient Sudoku Solver using Backtracking + Sets

def solve_sudoku(board):

    # Track used numbers
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    empty_cells = []

    # Initialize sets
    for i in range(9):
        for j in range(9):

            if board[i][j] == 0:
                empty_cells.append((i, j))
            else:
                num = board[i][j]

                rows[i].add(num)
                cols[j].add(num)

                box_id = (i // 3) * 3 + (j // 3)
                boxes[box_id].add(num)

    # Backtracking function
    def backtrack(index):

        if index == len(empty_cells):
            return True   # Solved

        r, c = empty_cells[index]
        box_id = (r // 3) * 3 + (c // 3)

        for num in range(1, 10):

            if (num not in rows[r] and
                num not in cols[c] and
                num not in boxes[box_id]):

                # Place number
                board[r][c] = num

                rows[r].add(num)
                cols[c].add(num)
                boxes[box_id].add(num)

                # Recursive call
                if backtrack(index + 1):
                    return True

                # Undo (Backtrack)
                board[r][c] = 0

                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box_id].remove(num)

        return False

    backtrack(0)


# Function to print board nicely
def print_board(board):

    for i in range(9):

        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(9):

            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            print(board[i][j], end=" ")

        print()


# Example Sudoku (0 = empty)
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],

    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],

    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

print("Before Solving:\n")
print_board(board)

solve_sudoku(board)

print("\nAfter Solving:\n")
print_board(board)