def read_codes(ints):
    """ Reads through intcode program, yielding one instruction at a time.
    Moves instruction pointer by number of parameters in the instruction.
    """
    i = 0
    while i < len(ints):
        opcode = ints[i]

        # Determine number of parameters depending on opcode
        if opcode in (3, 4):
            len_instruction = 2
        elif opcode in (1, 2):
            len_instruction = 4

        instruction = ints[i:i + len_instruction]
        i += len_instruction

        yield instruction


def process_codes(instruction):
    """ Read opcode and processes values accordingly.
    -- Opcodes --
    1: addition, takes 3 parameters that specify addresses of values (addend,
       addend, sum)
    2: multiplication, same parameters as 1 (multiplicand, multiplier, product)
    3: input, 1 parameter that specifies address to store input value
    4: output, 1 parameter that specifies address of value to output
    99: terminate program
    """
    # Determine opcode
    opcode = str(instruction[0]).zfill(5)
    opcode_type = opcode[-1]

    if opcode_type in ("1", "2"):
        # Determine if paramaters are in position mode (0 - default) or
        # immediate/value mode (1)
        params = []

        for i, digit in enumerate(opcode[-3::-1]):
            if digit == "1":
                params.append(instruction[i])
            else:
                params.append(intcode[instruction[i + 1]])

        if opcode_type == "1":
            intcode[params[2]] = params[0] + params[1]
        else:
            intcode[params[2]] = params[0] * params[1]
    elif opcode_type == "3":
        # Provide it 1, the ID for the ship's air conditioner unit
        intcode[instruction[1]] = 1
    elif opcode_type == "4":
        print(instruction[1])


# Initialize memory to program's values
with open("input.txt", "r") as inputf:
    intcode = list(map(int, inputf.read().split(",")))

for instruction in read_codes(intcode):
    process_codes(instruction)
