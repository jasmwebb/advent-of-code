# https://adventofcode.com/2020/day/18

from collections import deque
from operator import add, mul
from re import findall


def safe_eval1(expr):
    """Evalutaes given mathematical expression with new rules.
    Returns answer.
    """
    acc = 0
    ops = {"+": add, "*": mul}
    op = ops["+"]

    # While loop allows us to modify iterator
    while expr:
        part = expr.popleft()

        if part.isdigit():
            num = int(part)
            acc = op(acc, num)
        elif part in ops:
            op = ops[part]
        elif part == "(":
            num = safe_eval1(expr)
            acc = op(acc, num)
        else:  # part == ")"
            break

    return acc


def safe_eval2(expr):
    """Evalutaes given mathematical expression with new rules in which addition
    takes precedence over multiplication, using the distributive property.
    Returns answer.
    """
    acc = 0
    mulr = 1

    # While loop allows us to modify iterator
    while expr:
        part = expr.popleft()

        if part.isdigit():
            num = mul(mulr, int(part))
            acc += num
        elif part == "*":
            mulr = acc
            acc = 0
        elif part == "(":
            num = mul(mulr, safe_eval2(expr))
            acc += num
        elif part == ")":
            break

    return acc


if __name__ == "__main__":
    with open("input.txt", "r") as inputf:
        # Tokenize each expression into individual digits and operations
        expressions = [findall(r'\d+|[+*()]', line) for line in inputf]

    # map is faster than for loop
    answers = map(safe_eval1, map(deque, expressions))
    print("Part 1:", sum(answers))  # 98621258158412

    answers = map(safe_eval2, map(deque, expressions))
    print("Part 2:", sum(answers))  # 241216538527890
