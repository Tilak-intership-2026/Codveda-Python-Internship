 N-Queens Solver - Codveda Internship (Level 3)
1. Introduction
This project implements a solution to the classic N-Queens Problem, a fundamental challenge in combinatorial optimization and computer science. As part of the Codveda Technology Python Development Internship (Level 3 - Advanced), this application demonstrates the efficiency of Backtracking Algorithms in solving constraint-satisfaction problems. The program takes an integer 
N
N as input and places 
N
N queens on an 
N
×
N
N×N chessboard such that no two queens threaten each other.
2. Problem Statement
In chess, a queen can move any number of squares vertically, horizontally, or diagonally. The objective is to place 
N
N queens on an 
N
×
N
N×N board so that:
No two queens share the same row.
No two queens share the same column.
No two queens share the same diagonal.
Challenge: A naive brute-force approach would check 
N
N
N 
N
  combinations, which is computationally expensive. We need an optimized approach that prunes invalid paths early.
3.  Solution Approach: Backtracking
We use a Backtracking Algorithm, which builds a solution incrementally. If a partial solution violates the constraints, the algorithm "backtracks" (undoes the last step) and tries a different path.
4. Step-by-Step Breakdown:
Step
Action
Description
1
Start at Column 0
Begin placing queens from the leftmost column.
2
Try All Rows
For the current column, iterate through every row from 
0
0 to 
N
−
1
N−1.
3
Safety Check
Call is_safe() to verify if placing a queen at (row, col) conflicts with any previously placed queens.
4
Place Queen
If safe, mark the position as 1 (Queen) in the 2D board array.
5
Recurse
Move to the next column (col + 1) and repeat the process recursively.
6
Backtrack
If the recursive call returns False (no solution found in subsequent columns), remove the queen (mark as 0) and try the next row in the current column.
7
Base Case
If col >= N, it means all queens are successfully placed. Return True.
4. Code Architecture & Logic Flow
Component Breakdown:
is_safe(board, row, col, n):
Checks the left side of the current row for conflicts.
Checks the upper-left diagonal for conflicts.
Checks the lower-left diagonal for conflicts.
Note: We don't check the right side because we haven't placed queens there yet.
solve_n_queens_util(board, col, n):
The recursive engine. It handles the decision-making process and the backtracking logic (board[i][col] = 0).
solve_n_queens(n):
Initializes the 
N
×
N
N×N board with zeros.
Triggers the utility function and formats the final output using 'Q' and '.'.
main():
Handles user input validation and ensures 
N
≥
4
N≥4 for non-trivial solutions.





Code
Preview
5. Technology Stack & Rationale
Technology
Why We Used It
Python 3.x
Chosen for its clean syntax and efficient handling of recursion and list comprehensions.
2D Lists (Arrays)
Provides an intuitive way to represent the chessboard state with 
O
(
1
)
O(1) access time for cell checks.
Recursion
The most natural way to implement backtracking, allowing the program to explore deep decision trees without manual stack management.
6. Advantages
Optimized Search Space: Reduces complexity from 
O
(
N
N
)
O(N 
N
 ) to roughly 
O
(
N
!
)
O(N!) by pruning invalid branches early.
Dynamic Scalability: Can solve for any 
N
N (limited only by system memory).
Modular Design: Separation of safety logic from the solving logic makes the code easy to debug and extend.
7.Learning Outcomes
Mastery of Recursive Backtracking techniques.
Understanding of Constraint Satisfaction Problems (CSP).
Ability to visualize and implement 2D Array Manipulation.
Optimization of logical flows to reduce computational complexity.
