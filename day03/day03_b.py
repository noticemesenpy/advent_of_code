#!/usr/bin/env python3
"""
day03.py

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

import re


def main():
    """the main function"""
    counter = 0
    digitsRegex = re.compile(r"\d+")
    a_list = []
    b_list = []
    c_list = []

    with open("input.txt", "r") as infile:
        for line in infile.readlines():
            if len(digitsRegex.findall(line)) > 0:
                a = int(digitsRegex.findall(line)[0])
                b = int(digitsRegex.findall(line)[1])
                c = int(digitsRegex.findall(line)[2])
                a_list.append(a)
                b_list.append(b)
                c_list.append(c)
        joined_list = a_list + b_list + c_list

    for i in range(0, len(joined_list), 3):
        if is_triangle(joined_list[i], joined_list[i + 1], joined_list[i + 2]):
            counter += 1

    print(counter)


def is_triangle(a, b, c):
    """checks if the three argument integers can form a triangle"""
    if (a + b) > c and (a + c) > b and (c + b) > a:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
