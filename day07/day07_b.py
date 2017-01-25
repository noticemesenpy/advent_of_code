#!/usr/bin/env python3
#
# day07_b.py
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
            if aba_in_super_with_bab_in_hyper(separated_brackets):
                counter += 1
            # print("new line\n")

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


def aba_in_super_with_bab_in_hyper(l):
    """checks for ABBA in strings
    takes: list of strings
    returns: bool
    """
    for super_seq in l[0]:
        for i in range(len(super_seq)):
            if i == len(super_seq) - 2 \
            or i == len(super_seq) - 1:
                continue
            elif super_seq[i] == super_seq[i + 2] \
            and super_seq[i] != super_seq[i + 1]:
                a = super_seq[i]
                b = super_seq[i + 1]
                for hyper_seq in l[1]:
                    if b + a + b in hyper_seq:
                        # print(a + b + a)
                        return True


if __name__ == "__main__":
    main()

