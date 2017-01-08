#!/usr/bin/env python3
"""
day02_a.py

copyright 2017 noticemesen.py

gitlab: gitlab.com/noticemesenpy
github: github.com/noticemesenpy

********************************************************************************

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


********************************************************************************
"""

def main():
    """the main function"""
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    x = 1
    y = 1

    with open("input.txt", "r") as instructions:
        for line in instructions.readlines():
            current = find_button(keypad, x, y, line)
            x = current[1]
            y = current[0]


def find_button(keypad, x, y, line):
    """finds the button to be pressed



    Keyword arguments:
    keypad -- the 3x3 matrix of the keypad
    x -- the x (horizontal) coordinate ont the keypad
    y -- the y (vertical) coordinate on the keypad
    line -- the line of instructions in input.txt
    """

    for instruction in line:
        if instruction == "U":
            if y == 0:
                pass
            else:
                y -= 1
        elif instruction == "D":
            if y == 2:
                pass
            else:
                y += 1
        elif instruction == "R":
            if x == 2:
                pass
            else:
                x += 1
        elif instruction == "L":
            if x == 0:
                pass
            else:
                x -= 1
    print(keypad[y][x])
    return (y, x)



if __name__ == "__main__":
    main()
