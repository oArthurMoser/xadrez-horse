import time
import os

# Size of the chessboard
N = 8

# Possible moves of a knight on a chessboard
moves_x = [2, 1, -1, -2, -2, -1, 1, 2]
moves_y = [1, 2, 2, 1, -1, -2, -2, -1]

# Clear the screen
def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")

# Check if the coordinates (x, y) are within the board
def inside_board(x, y):
  return 0 <= x < N and 0 <= y < N

# Count the number of possible moves from (x, y) available on the board
def count_moves(x, y, board):
  count = 0
  for i in range(N):
    nx, ny = x + moves_x[i], y + moves_y[i]
    if inside_board(nx, ny) and board[nx][ny] == -1:
      count += 1
  return count

# Find the next move using Warnsdorff's heuristic
def next_move(x, y, board):
  min_probability = 8
  next_x, next_y = -1, -1
  for i in range(N):
    nx, ny = x + moves_x[i], y + moves_y[i]
    if inside_board(nx, ny) and board[nx][ny] == -1:
      probability = count_moves(nx, ny, board)
      if probability <= min_probability:
        min_probability = probability
        next_x, next_y = nx, ny
  return next_x, next_y

def knights_tour(start_x=0, start_y=0):
  board = [[-1 for _ in range(N)] for _ in range(N)]

  x, y = start_x, start_y
  # Mark the initial position as visited (index 0 is filled here!)
  board[x][y] = 1
  clear_screen()
  print_board(x, y, board)
  time.sleep(0.5)

  # Start in index 1 because index 0 is already filled
  for step in range(2, N * N + 1):
    x, y = next_move(x, y, board)
    if x == -1 and y == -1:
      print("Could not complete the knight's tour.")
      return None
    board[x][y] = step
    clear_screen()
    print_board(start_x, start_y, board)
    time.sleep(0.5)

  return board

# Print the board in a formatted way
def print_board(x, y, board):
  print("=== Knight's Tour - Warnsdorff's Heuristic ===")
  print(f"Knight's Tour starting at ({x+1}, {y+1}):\n")
  
  max_val = max(max(r) for r in board)
  for row in board:
    original_line = " ".join(f"{cell:2}" for cell in row)
    emoji_line = " ".join(
      "🔳" if cell == -1 else ("🐴" if cell == max_val else "🟩")
      for cell in row
    )
    print(f"{original_line}  {emoji_line}")

if __name__ == "__main__":
  try:
    print("=== Knight's Tour - Warnsdorff's Heuristic ===")
    x = int(input("Enter initial X coordinate (1 to 8): ")) - 1
    y = int(input("Enter initial Y coordinate (1 to 8): ")) - 1

    if not (0 <= x < N and 0 <= y < N):
      print("Invalid coordinates! Please enter values between 1 and 8.")
    else:
      knights_tour(x, y)

    input("\nPress Enter to exit...")
  except ValueError:
    print("Invalid input! Please enter integers.")
    input("\nPress Enter to exit...")
