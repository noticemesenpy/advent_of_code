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

    face = "north"
    visited = [(0, 0)]

    for instruction in path:
        direction = instruction[0]
        steps = int(instruction[1:])

        if face == "north":
            if direction == "L":
                visited = append_coordinates(visited, "west", steps)
                face = "west"
            else:
                visited = append_coordinates(visited, "east", steps)
                face = "east"
        elif face == "east":
            if direction == "L":
                visited = append_coordinates(visited, "north", steps)
                face = "north"
            else:
                visited = append_coordinates(visited, "south", steps)
                face = "south"
        elif face == "south":
            if direction == "L":
                visited = append_coordinates(visited, "east", steps)
                face = "east"
            else:
                visited = append_coordinates(visited, "west", steps)
                face = "west"
        else:
            if direction == "L":
                visited = append_coordinates(visited, "south", steps)
                face = "south"
            else:
                visited = append_coordinates(visited, "north", steps)
                face = "north"

        for coordinates in visited:
            if visited.count(coordinates) > 1:
                print(abs(coordinates[0]) + abs(coordinates[1]))
                return


def append_coordinates(visited, face, steps):
    """Append visited coordinates to "visited"


    Keyword arguments:
    visited -- the list containing the visited coordinates
    face -- the direction we are facing (north, east, south, west)
    steps -- the amount of steps to be taken in that direction
    """

    current_location = visited[-1]
    x = current_location[0]
    y = current_location[1]

    for step in range(steps):
        step = step + 1
        if face == "north":
            visit = (x, y + step)
            visited.append(visit)
        elif face == "east":
            visit = (x + step, y)
            visited.append(visit)
        elif face == "south":
            visit = (x, y - step)
            visited.append(visit)
        else:
            visit = (x - step, y)
            visited.append(visit)

    return visited


if __name__ == "__main__":
    main()

