#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, n):
    """
    Utilize backtracking to solve N Queens problem
    """
    if col == n:
        print_solution(board, n)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            res = solve_nqueens_util(board, col + 1, n) or res

            board[i][col] = 0  # backtrack if placing queen at board[i][col] does not lead to a solution

    return res

def print_solution(board, n):
    """
    Print the solution in the required format
    """
    solution = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)

def nqueens(n):
