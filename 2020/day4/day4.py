# https://adventofcode.com/2020/day/4

def create_dict(passport):
    """Takes list of passport fields and returns as a dictionary of key:value
    pairs.
    """
    fields = passport.split()
    passports_dict = {}

    for field in fields:
        key, value = field.split(":")
        passports_dict[key] = value

    return passports_dict


def validate_fields(passport, fields):
    """Verifies if given passport contains the minimum required data."""
    req_fields = set(fields)
    passport_fields = set(passport.keys())

    return req_fields.issubset(passport_fields)


def validate_data(passport, fields):
    """Verifies that data in each required field is valid."""
    for field, req in fields.items():
        if field in ("byr", "iyr", "eyr"):
            if not req[0] <= int(passport[field]) <= req[1]:
                return False

        if field == "hgt":
            units = passport[field][-2:]
            if units not in req.keys():
                return False
            else:
                if not (
                    req[units][0] <= int(passport[field][:-2]) <= req[units][1]
                ):
                    return False

        if field == "hcl":
            if passport[field][0] != "#":
                return False

            hexcode = passport[field][1:]
            if len(hexcode) != req["length"]:
                return False
            else:
                for char in hexcode:
                    if char not in req["chars"]:
                        return False

        if field == "ecl":
            if not passport[field] in req:
                return False

        if field == "pid":
            if len(passport[field]) != req["length"]:
                return False

    return True


if __name__ == "__main__":
    with open("input.txt", "r") as inputf:
        passports = inputf.read().split("\n\n")

    passports = [create_dict(passport) for passport in passports]
    reqs = {
        "byr": (1920, 2002),
        "iyr": (2010, 2020),
        "eyr": (2020, 2030),
        "hgt": {
            "cm": (150, 193),
            "in": (59, 76)
        },
        "hcl": {
            "length": 6,
            "chars": (
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                "a", "b", "c", "d", "e", "f"
            )
        },
        "ecl": ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
        "pid": {
            "length": 9
        }
    }

    valid_passports = [
        passport for passport in passports
        if validate_fields(passport, reqs.keys())
    ]
    print(f"Part 1: {len(valid_passports)}")  # 196

    valid_passports = [
        passport for passport in valid_passports
        if validate_data(passport, reqs)
    ]
    print(f"Part 2: {len(valid_passports)}")  # 114
