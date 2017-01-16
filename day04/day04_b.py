#!/usr/bin/env python3
#
# day04_b.py
# 
# copyright 2017 noticemesen.py
# 
# github: github.com/noticemesenpy
# gitlab: gitlab.com/noticemesenpy
# 
# ********************************************************************************
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# ********************************************************************************


import re


def main():
    """the main function"""
    # example room -- mybbycsfo-mkxni-yzobkdsyxc-614[ybckm]
    alphaBet = [
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
            ]
    deciphered_rooms = []

    with open("real_rooms.txt", "r") as infile:
        for line in infile.readlines():
            deciphered_char = []
            for char in line:
                if char.isalpha():
                    char = alphaBet[(alphaBet.index(char) + int(line[-11:-8])) % 26]
                    deciphered_char.append(char)
                else:
                    deciphered_char.append(char)
            deciphered_rooms.append("".join(deciphered_char))

    for room in deciphered_rooms:
        print(room)



if __name__ == "__main__":
    main()

