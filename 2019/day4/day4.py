password_range = list(map(int, "193651-649729".split("-")))


def check_pass(password):
    """Determines if given password (integer) satisfies requirements."""
    digits = str(password)

    # Check: going left to right, digits never decrease (increase or same)
    for digit1, digit2 in zip(digits[0::1], digits[1::1]):
        if int(digit2) < int(digit1):
            return False

    for digit1, digit2 in zip(digits[0::1], digits[1::1]):
        # Check: two adjacent digits are the same
        if digit1 == digit2:
            # Check: matching digits only occur twice
            if digits.count(digit1) == 2:
                return True

    return False


possible_passwords = 0

for password in range(password_range[0], password_range[1]):
    if not check_pass(password):
        continue
    else:
        possible_passwords += 1

print(possible_passwords)
# Part 1: 1605, Part 2: 1102
