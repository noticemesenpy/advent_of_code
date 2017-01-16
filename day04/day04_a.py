#!/usr/bin/env python3
"""
day04_a.py

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

from collections import Counter


def main():
    """the main function"""
    sum_of_sector_IDs = 0
    rooms = []

    with open("input.txt", "r") as infile:
        lines = infile.readlines()
        for line in lines:
            rooms.append(line.strip())

    for room in rooms:
        sectorID = int(room[-10:-7])
        checksum = room[-6:-1]
        charlist = []

        # get a raw list of all chars in room name
        for char in room:
            if char == "[":
                break
            elif char.isalpha():
                charlist.append(char)

        # sort that list by count
        char_counts = Counter(charlist)
        top_chars = char_counts.most_common(len(charlist))

        # sort ties alphabetically
        final_sorted = []
        for i in range(round((len(charlist) + 1) / 2), 0, -1): #ties can be max half of len(charlist)
            ties = []
            for tup in top_chars:
                if i == 0:
                    pass
                elif i == tup[1]:
                    ties.append(tup)
            for item in sorted(ties):
                final_sorted.append(item)


        # bool check for real rooms
        for i in range(5):
            if checksum[i] == final_sorted[i][0]:
                is_room = True
            else:
                is_room = False
                break

        # sum all sector IDs and print them to stdout
        if is_room:
            print(room)
            sum_of_sector_IDs = sum_of_sector_IDs + sectorID
    print(sum_of_sector_IDs)



if __name__ == "__main__":
    main()

