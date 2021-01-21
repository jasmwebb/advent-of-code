[Advent of Code](https://adventofcode.com/)

Solutions are organized by `year/day#`. In each directory you'll find, at minimum, the solution file (`day#.py`) alongside `.txt` files that contain my input data and the example data given in the prompts (used for testing). In some cases there may also be a test suite (`tests.py`).

Each of the solution files contain the solutions for both parts 1 and 2, and the answers that I submitted to earn a star are commented on the same line as the corresponding `print` statement.  For example, from `2020/day21/day21.py`:

```
print("Part 1:", occurences)  # 2659
print("Part 2:", unsafe)  # rcqb,cltx,nrl,qjvvcvz,tsqpn,xhnk,tfqsb,zqzmzl
```

However, and this is especially true of the earlier days, functions that led to part 1's answer may have been refactored to get part 2's answer. In those cases, to see the code that led to part 1's answer, you'd need to rollback to a previous commit, typically with the message *Add solution for `year` Day `number` Part 1*.
