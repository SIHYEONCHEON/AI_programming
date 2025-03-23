import random
import os
import time
from collections import deque


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def create_board():
    numbers = list(range(1, 10)) + [0]  # 1~9 숫자와 빈칸(0) 포함
    random.shuffle(numbers)  # 무작위 섞기
    return [numbers[:5], numbers[5:]]  # 2행 5열로 분할


def display_board(board):
    clear_screen()
    for row in board:
        print(" ".join(f"{num:2}" for num in row))
    print()


def find_empty(board):
    for i in range(2):
        for j in range(5):
            if board[i][j] == 0:
                return i, j
    return None


def possible_moves(i, j):
    moves = []
    if i > 0: moves.append(('up', i - 1, j))
    if i < 1: moves.append(('down', i + 1, j))
    if j > 0: moves.append(('left', i, j - 1))
    if j < 4: moves.append(('right', i, j + 1))
    return moves


def move_tile(board, direction):
    i, j = find_empty(board)
    for move, ni, nj in possible_moves(i, j):
        if move == direction:
            board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
            return


def board_to_tuple(board):
    return tuple(tuple(row) for row in board)


def is_solved(board):
    return board == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]


def bfs_solve(board):
    queue = deque([(board, [])])
    visited = set()
    goal = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]

    while queue:
        current_board, path = queue.popleft()
        if is_solved(current_board):
            return path

        state = board_to_tuple(current_board)
        if state in visited:
            continue
        visited.add(state)

        i, j = find_empty(current_board)
        for move, ni, nj in possible_moves(i, j):
            new_board = [row[:] for row in current_board]
            new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
            queue.append((new_board, path + [move]))

    return []


def auto_solve(board):
    solution = bfs_solve(board)
    for move in solution:
        move_tile(board, move)
        display_board(board)
        time.sleep(0.5)


def main():
    board = create_board()
    display_board(board)
    input("Press Enter to start solving...")
    auto_solve(board)
    print("Solved!")


if __name__ == "__main__":
    main()
