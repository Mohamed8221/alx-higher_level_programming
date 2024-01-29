#!/usr/bin/python3
import sys


def print_board(board):
    """Prints the board solution"""
    print([[i, board[i]] for i in range(len(board))])


def is_safe(board, row, col):
    """Checks if a position is safe from attack"""
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve_nqueens(n, board=[], col=0):
    """Solves the N queens problem"""
    if col == n:
        print_board(board)
        return

    for row in range(n):
        if is_safe(board, row, col):
            board.append(row)
            solve_nqueens(n, board, col + 1)
            board.pop()


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
