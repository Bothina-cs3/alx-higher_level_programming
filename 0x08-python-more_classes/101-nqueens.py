#!/usr/bin/python3
"""
N Queens problem solver using backtracking.
"""

import sys

def print_solution(solution):
    """Prints the solution in the specified format."""
    for position in solution:
        print(position, end="")
    print()

def is_safe(board, row, col):
    """Check if it's safe to place a queen at a given position."""
    # Check left side of the row
    for i in range(col):
        if board[i] == row or board[i] - i == row - col or board[i] + i == row + col:
            return False
    return True

def solve_nqueens_util(n, board, col, solutions):
    """Recursive utility function to solve N Queens problem."""
    if col == n:
        solutions.append(board[:])
        return

    for row in range(n):
        if is_safe(board, row, col):
            board[col] = row
            solve_nqueens_util(n, board, col + 1, solutions)

def solve_nqueens(n):
    """Solves the N Queens problem and prints the solutions."""
    board = [-1] * n
    solutions = []
    solve_nqueens_util(n, board, 0, solutions)
    
    for solution in solutions:
        print_solution([[i, solution[i]] for i in range(n)])

def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    solve_nqueens(N)

if __name__ == "__main__":
    main()
