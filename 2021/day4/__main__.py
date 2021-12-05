# https://adventofcode.com/2021/day/4

import sys

from copy import deepcopy


def get_input():
    try:
        if sys.argv[1] == "-t":
            filename = "test"
        else:
            sys.exit(
                "\n\033[0;33mInvalid flag\033[0;0m, ya dingus."
                "\n🌼 \033[3;37mDid you mean"
                f"\033[1;35;40m python3 {sys.argv[0]} -t \033[0;0m \033[3;37m"
                "?\033[0;0m\n"
            )
    except IndexError:
        filename = "input"

    return f"{sys.argv[0]}/{filename}.txt"


def setup_boards(raw_boards, board_size):
    boards_rows = [
        raw_boards[i:i + board_size]
        for i in range(0, len(raw_boards), board_size)
    ]

    boards_cols = [
        [list(col) for col in zip(*board)]
        for board in boards_rows
    ]

    return boards_rows, boards_cols


def mark_boards(drawn_num, boards):
    boards = boards

    for board in boards:
        for line in board:
            if drawn_num in line:
                line.remove(drawn_num)

    return boards


def check_winners(boards):
    winners = []

    for board_id, board in enumerate(boards):
        if not all(board):
            winners.append({"unmarked": board, "id": board_id})

    return winners


def play_round(drawn_num, boards):
    boards = mark_boards(drawn_num, boards)

    return check_winners(boards)


def play_bingo(numbers, boards):
    boards_rows, boards_cols = boards
    winners = []

    for drawn_num in (num for num in numbers):
        winners += [winner for winner in play_round(drawn_num, boards_rows)]
        winners += [winner for winner in play_round(drawn_num, boards_cols)]

        if winners:
            return drawn_num, winners


def calc_final_score(winning_num, winning_board):
    unmarked_nums = [
        int(num) for line in winning_board[0]["unmarked"]
        for num in line
        if line
    ]

    return int(winning_num) * sum(unmarked_nums)


def play_to_last(numbers, boards_in_play):
    numbers_start = 0
    winning_num = None

    while len(boards_in_play[0]):
        numbers = numbers[numbers_start:]

        winning_num, winning_boards = play_bingo(numbers, boards_in_play)

        numbers_start = numbers.index(winning_num) + 1

        if len(boards_in_play[0]) > 1:
            winning_boards.sort(reverse=True, key=lambda board: board["id"])

            for board in winning_boards:
                del boards_in_play[0][board["id"]]  # Rows matrix
                del boards_in_play[1][board["id"]]  # Columns matrix
        else:
            return winning_num, winning_boards


if __name__ == "__main__":
    input_path = get_input()

    with open(input_path, "r") as inputf:
        drawn_numbers = inputf.readline().rstrip().split(",")
        raw_boards = [
            line.split() for line in inputf.readlines()[1:]
            if line.split()
        ]

    boards = setup_boards(raw_boards, 5)

    winning_num, winning_board = play_bingo(drawn_numbers, deepcopy(boards))

    print(
        f"Part 1: {calc_final_score(winning_num, winning_board)}"
    )  # 58374

    winning_num, board = play_to_last(drawn_numbers, deepcopy(boards))

    print(f"Part 2: {calc_final_score(winning_num, board)}")  # 11377
