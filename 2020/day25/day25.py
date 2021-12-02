# https://adventofcode.com/2020/day/25

def parse_input(filename):
    """Parses given input for each device's public key."""
    with open(filename, "r") as inputf:
        return tuple(map(int, inputf))


def find_loop(public_key):
    """Finds the loop size used to transform the subject number, 7, into a
    given public key.
    """
    v = 1
    loop_size = 0

    while v != public_key:
        v = v * 7 % 20201227
        loop_size += 1

    return loop_size


def transform_key(public_key, loop_size):
    """Transforms a given device's public key with a given loop size and
    returns the resulting encryption key.
    """
    v = 1

    for _ in range(loop_size):
        v = v * public_key % 20201227

    return v


if __name__ == "__main__":
    card_pub, door_pub = parse_input("input.txt")
    card_loop = find_loop(card_pub)
    door_loop = find_loop(door_pub)

    card_encryption = transform_key(door_pub, card_loop)
    door_encryption = transform_key(card_pub, door_loop)

    if card_encryption == door_encryption:
        print("Part 1:", card_encryption)  # 545789
    else:
        print("Encryption keys don't match.")
