#!/usr/bin/env python3
#
# day07_a.py
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

import re


def main():
    """the main function"""
    counter = 0

    with open("input.txt") as infile:
        for line in infile.readlines():
            separated_brackets = separate_brackets(line.rstrip())
            if abba_in_string(separated_brackets[0]) \
            and not abba_in_string(separated_brackets[1]):
                counter += 1

    print(counter)


def separate_brackets(s):
    """separates the bracket strings from the no-bracket strings
    takes: string
    returns: list of lists
    """
    separated_list = []
    bracketRegex = re.compile(r"\[\w+\]")
    no_bracket_list = bracketRegex.split(s)
    bracket_list = bracketRegex.findall(s)
    separated_list.extend([no_bracket_list, bracket_list])
    return(separated_list)


def abba_in_string(l):
    """checks for ABBA in strings
    takes: list of strings
    returns: bool
    """
    for element in l:
        # print(element)
        for i in range(len(element)):
            # print(element[i])
            if i == 0:
                continue
            elif i == len(element) - 2:
                continue
            elif i == len(element) - 1:
                continue
            elif element[i] == element[i + 1]\
            and element[i] != element[i - 1]\
            and element[i - 1] == element[i + 2]:
                # print(l)
                return True


if __name__ == "__main__":
    main()

