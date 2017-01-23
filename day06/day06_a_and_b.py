#!/usr/bin/env python3
#
# day06_a_and_b.py
# 
# copyright 2017 noticemesen.py
# 
# gitlab: gitlab.com/noticemesenpy
# github: github.com/noticemesenpy
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

from collections import Counter

def main():
    """the main function"""
    columns = make_columns()
    print(decode_message(columns))


def make_columns():
    """splits lines of text into columns"""
    l_0 = []
    l_1 = []
    l_2 = []
    l_3 = []
    l_4 = []
    l_5 = []
    l_6 = []
    l_7 = []

    with open("input.txt") as infile:
        for line in infile.readlines():
            l_0.append(line[0])
            l_1.append(line[1])
            l_2.append(line[2])
            l_3.append(line[3])
            l_4.append(line[4])
            l_5.append(line[5])
            l_6.append(line[6])
            l_7.append(line[7])

    big_list = [l_0, l_1, l_2, l_3, l_4, l_5, l_6, l_7]
    return big_list


def decode_message(l):
    """finds most common element in 5 lists and appends them to new list"""
    result = []
    # print(l)

    for l in l:
        count = Counter(l)
        result.append(count.most_common()[-1][0]) # change -1 to 0 to solve day06_a

    return "".join(result)


if __name__ == "__main__":
    main()

