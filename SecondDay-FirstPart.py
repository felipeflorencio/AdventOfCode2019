#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Intcode = [Int] // list of integers
# Look into first integer, (called position 0)
# Position = opcode (Always start at position 0)
# opcode = 1 - 99
# opcode indicate what to do
# 99 = finished and immediately halt
# unknown opcode = something went wrong
#
# opcode 1 means = means adds / sum
# 3 digits immediately after the opcode tell the position to look into
# Doing this sum((from opcode position 2 get the value), (from opcode position 3 get the value))
# Add to the third opcode position the result, if has value on third override
#
# opcode 2 means = the same as opcode 1 but instead multiply
#
# After process one opcode move to the next stepping forward 4 positions (position + 4)
#
#
# Before start replace the position 1 with value 12 and replace position 2 with value 2
# Result: What is the value at position 0 after the program halts?


class ProgramAlarm:

    input = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 9, 1, 19, 1, 19, 5, 23, 1, 9, 23, 27, 2, 27, 6, 31, 1, 5, 31, 35, 2, 9, 35, 39, 2, 6, 39, 43, 2, 43, 13, 47, 2, 13, 47, 51, 1, 10, 51, 55, 1, 9, 55, 59, 1, 6, 59, 63, 2, 63, 9, 67, 1, 67, 6, 71, 1, 71, 13, 75, 1, 6, 75, 79,
             1, 9, 79, 83, 2, 9, 83, 87, 1, 87, 6, 91, 1, 91, 13, 95, 2, 6, 95, 99, 1, 10, 99, 103, 2, 103, 9, 107, 1, 6, 107, 111, 1, 10, 111, 115, 2, 6, 115, 119, 1, 5, 119, 123, 1, 123, 13, 127, 1, 127, 5, 131, 1, 6, 131, 135, 2, 135, 13, 139, 1, 139, 2, 143, 1, 143, 10, 0, 99, 2, 0, 14, 0]

    opcodeSum = 1
    opcodeMultiply = 2
    opcodeHalts = 99

    def __init__(self):
        result = self.program_alarm()
        print(result)

    def calculate_sum(self, position1, position2):
        return int(position1 + position2)

    def calculate_multiply(self, position1, position2):
        return int(position1 * position2)

    def program_alarm(self):
        self.input[1] = 12
        self.input[2] = 2

        adjusted_input = self.input

        jump_evaluation = 0
        for position, value in enumerate(adjusted_input):

            if position >= jump_evaluation:
                if value == 99:
                    break

                if value in range(1, 99):
                    try:
                        if value == 1:
                            position1 = adjusted_input[position+1]
                            position2 = adjusted_input[position+2]
                            result = self.calculate_sum(
                                adjusted_input[position1], adjusted_input[position2])
                            position3 = adjusted_input[position + 3]
                            adjusted_input[position3] = result
                            jump_evaluation = position+4

                        if value == 2:
                            position1 = adjusted_input[position+1]
                            position2 = adjusted_input[position+2]
                            result = self.calculate_multiply(
                                adjusted_input[position1], adjusted_input[position2])
                            position3 = adjusted_input[position + 3]
                            adjusted_input[position3] = result
                            jump_evaluation = position + 4

                    except:
                        continue

        return adjusted_input[0]


if __name__ == "__main__":
    ProgramAlarm()
