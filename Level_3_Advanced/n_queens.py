def is_safe(board, row, col, n):
    """Check if a queen can be placed at board[row][col]"""

    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, n):
    """Use backtracking to find all solutions"""
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_n_queens_util(board, col + 1, n):
                return True

            board[i][col] = 0  # Backtrack

    return False


def solve_n_queens(n):
    """Initialize board and start the solving process"""
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
        return False

    print(f"✅ Solution for {n}-Queens Problem:")
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    return True


def main():
    print("--- Codveda Level 3: N-Queens Problem ---")
    try:
        n = int(input("Enter the number of Queens (N): "))
        if n < 4:
            print("⚠️ For N < 4, no solution exists or it's trivial.")
        else:
            solve_n_queens(n)
    except ValueError:
        print("❌ Invalid input! Please enter an integer.")


if __name__ == "__main__":
    main()