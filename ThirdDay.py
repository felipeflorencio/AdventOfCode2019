#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# two wires
# they connect to a central port
# one wire per line of text (puzzle input)
# eventually they cross paths
# find intersetion point closest to the central port
# the start point does not count as cross paths

class CrossedWires:
    
    input = ["R75","D30","R83","U83","L12","D49","R71","U7","L72","U62","R66","U55","R34","D71","R55","D58","R83"]

    matrix = []

    def __init__(self):
        self.close_distance()
        

    def generate_position_in_the_matrix(self, lastPosition, newPosition):
        letter = newPosition[0]
        number = int(newPosition[1:])
        x, y = 0, 0
        
        # Just check if is not the empty one, that is our first start
        if len(lastPosition) != 0:
            x = lastPosition[0]
            y = lastPosition[1]

        if letter == "R" or letter == "L":
            if letter == "R":
                # sum
                self.matrix.append([number+x,y])
            else:
                # sub
                self.matrix.append([x-abs(number),y])
        else:
            if letter == "U":
                # sum
                self.matrix.append([x,number+y])
            else:
                # sub
                self.matrix.append([x,y-abs(number)])


    def close_distance(self):

        # start the first position
        self.generate_position_in_the_matrix([], self.input[0])

        for position, item in enumerate(self.input[1:], start=1):
            self.generate_position_in_the_matrix(self.matrix[position-1], item)

        print(self.matrix)

if __name__ == "__main__":
    CrossedWires()
