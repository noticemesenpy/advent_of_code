#!/usr/bin/env python3
"""
make_my__days.py

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
    with open("make_my_days.sh", "w") as bcomm:
        bcomm.write("#!/bin/bash\n\n")
        bcomm.write("mkdir day{01..24}\n\n")
        bcomm.write("vim -o ")
        for i in range(24):
            bcomm.write("day" + str(i + 1).zfill(2) + "/day" + str(i + 1).zfill(2) + ".py ")


if __name__ == "__main__":
    main()
