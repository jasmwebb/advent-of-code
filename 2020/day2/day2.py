# https://adventofcode.com/2020/day/2

def validate_char_count(passwords) -> int:
    """Iterates through passwords and their requirements (policy).
    Verifies given character count falls within given range.
    Returns number of valid passwords.
    """
    valid_passwords = 0

    for policy, password in passwords:
        min_count, max_count = policy[:-2].split("-")

        if int(min_count) <= password.count(policy[-1]) <= int(max_count):
            valid_passwords += 1

    return valid_passwords


def validate_char_position(passwords) -> int:
    """Iterates through passwords and their requirements (policy).
    Verifies given character is in only one of given positions, index 1.
    Returns number of valid passwords.
    """
    valid_passwords = 0

    for policy, password in passwords:
        pos1, pos2 = policy[:-2].split("-")
        pos1 = int(pos1) - 1
        pos2 = int(pos2) - 1
        char = policy[-1]

        if password[pos1] == char and password[pos2] != char:
            valid_passwords += 1
        elif password[pos2] == char and password[pos1] != char:
            valid_passwords += 1

    return valid_passwords


if __name__ == "__main__":
    with open("input.txt", "r") as inputf:
        passwords = [line.rstrip("\n").split(": ") for line in inputf]
        print(f"Part 1: {validate_char_count(passwords)}")
        print(f"Part 2: {validate_char_position(passwords)}")
