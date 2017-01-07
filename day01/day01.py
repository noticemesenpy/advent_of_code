#!/usr/bin/env python3
"""
day01.py

Day one of the 2016 Advent of Code.
Instructions: http://adventofcode.com/2016/day/1

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
    path = ["L4", "L3", "R1", "L4", "R2", "R2", "L1", "L2", "R1", "R1", "L3",
            "R5", "L2", "R5", "L4", "L3", "R2", "R2", "L5", "L1", "R4", "L1",
            "R3", "L3", "R5", "R2", "L5", "R2", "R1", "R1", "L5", "R1", "L3",
            "L2", "L5", "R4", "R4", "L2", "L1", "L1", "R1", "R1", "L185", "R4",
            "L1", "L1", "R5", "R1", "L1", "L3", "L2", "L1", "R2", "R2", "R2",
            "L1", "L1", "R4", "R5", "R53", "L1", "R1", "R78", "R3", "R4", "L1",
            "R5", "L1", "L4", "R3", "R3", "L3", "L3", "R191", "R4", "R1", "L4",
            "L1", "R3", "L1", "L2", "R3", "R2", "R4", "R5", "R5", "L3", "L5",
            "R2", "R3", "L1", "L1", "L3", "R1", "R4", "R1", "R3", "R4", "R4",
            "R4", "R5", "R2", "L5", "R1", "R2", "R5", "L3", "L4", "R1", "L5",
            "R1", "L4", "L3", "R5", "R5", "L3", "L4", "L4", "R2", "R2", "L5",
            "R3", "R1", "R2", "R5", "L5", "L3", "R4", "L5", "R5", "L3", "R1",
            "L1", "R4", "R4", "L3", "R2", "R5", "R1", "R2", "L1", "R4", "R1",
            "L3", "L3", "L5", "R2", "R5", "L1", "L4", "R3", "R3", "L3", "R2",
            "L5", "R1", "R3", "L3", "R2", "L1", "R4", "R3", "L4", "R5", "L2",
            "L2", "R5", "R1", "R2", "L4", "L4", "L5", "R3", "L4"]

    walk(path)


def walk(path):
    """walks the path as per the instructions"""
    face = "north"
    distance = 0

    for instruction in path:
        direction = instruction[0]
        steps = int(instruction[1:])
        if face == "north":
            if direction == "L":
                face = "west"
                distance = distance - steps
            else:
                face = "east"
                distance = distance + steps
        elif face == "east":
            if direction == "L":
                face = "north"
                distance = distance + steps
            else:
                face = "south"
                distance = distance - steps
        elif face == "south":
            if direction == "L":
                face = "east"
                distance = distance + steps
            else:
                face = "west"
                distance = distance - steps
        else:
            if direction == "L":
                face = "south"
                distance = distance - steps
            else:
                face = "north"
                distance = distance + steps

    print(abs(distance))


if __name__ == "__main__":
    main()

