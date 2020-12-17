# https://adventofcode.com/2020/day/15

if __name__ == "__main__":
    # game = (0, 3, 6)
    game = (8, 0, 17, 4, 1, 12)

    nums = {num: [i + 1, 0] for i, num in enumerate(game)}
    turn = len(game) + 1
    # max_turn = 2020
    max_turn = 30000000
    last = game[-1]

    while turn <= max_turn:
        recent, previous = nums[last]
        last = recent - previous if previous > 0 else 0
        try:
            previous = nums[last][0]
        except KeyError:
            previous = 0
        nums[last] = [turn, previous]
        turn += 1

    print(last)  # Part 1: 981, Part 2: 164878
