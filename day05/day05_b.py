#!/usr/bin/env python3
#
# filename.py
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


import hashlib


def main():
    """the main function"""
    puzzle_input = "cxdnnyjw"
    password = [None] * 8
    index = 0

    while None in password:
        md5_hash = hashlib.md5((puzzle_input + str(index)).encode("utf")).hexdigest()
        if str(md5_hash[0:5]) == "00000":
            sixth = md5_hash[5]
            if sixth.isdigit() and \
               int(sixth) >= 0 and int(sixth) <= 7 and \
               password[int(sixth)] == None:
                password[int(sixth)] = md5_hash[6]
        index += 1

    print("".join(password))


if __name__ == "__main__":
    main()
