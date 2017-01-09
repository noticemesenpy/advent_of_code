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
    keypad = [[0, 0, 1, 0, 0],
              [0, 2, 3, 4, 0],
              [5, 6, 7, 8, 9],
              [0, "A", "B", "C", 0],
              [0, 0, "D", 0, 0]]
    x = 0
    y = 2

    with open("input.txt", "r") as instructions:
        for line in instructions.readlines():
            current = find_button(keypad, x, y, line)
            x = current[1]
            y = current[0]


def find_button(keypad, x, y, line):
    """finds the button to be pressed

    I filled the blank spaces in the matrix with zeros
    and raise an exception when an index is zero.
    That way I get around the difficulty of indices
    not lining up properly (index 0 of the top most list
    is index 1 of the one below, etc)



    Keyword arguments:
    keypad -- the matrix of the keypad
    x -- the x (horizontal) coordinate ont the keypad
    y -- the y (vertical) coordinate on the keypad
    line -- the line of instructions in input.txt
    """

    for instruction in line:
        if instruction == "U":
            try:
                if keypad[y - 1][x] == 0:
                    raise Exception
                try_var = keypad[y - 1][x]
            except IndexError:
                pass
            except Exception:
                pass
            else:
                y -= 1
        elif instruction == "D":
            try:
                if keypad[y + 1][x] == 0:
                    raise Exception
                try_var = keypad[y + 1][x]
            except IndexError:
                pass
            except Exception:
                pass
            else:
                y += 1
        elif instruction == "R":
            try:
                if keypad[y][x + 1] == 0:
                    raise Exception
                try_var = keypad[y][x + 1]
            except IndexError:
                pass
            except Exception:
                pass
            else:
                x += 1
        elif instruction == "L":
            try:
                if keypad[y][x - 1] == 0:
                    raise Exception
                try_var = keypad[y][x - 1]
            except IndexError:
                pass
            except Exception:
                pass
            else:
                x -= 1
    print(keypad[y][x])
    return (y, x)



if __name__ == "__main__":
    main()
