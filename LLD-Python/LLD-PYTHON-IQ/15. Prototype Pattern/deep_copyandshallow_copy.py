"""Prototype Pattern - Deep Copyandshallow Copy

This file shows the Deep Copyandshallow Copy example in the Prototype Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

import copy

list1 = [1, 4, 5, 2, [65, 43, 21, 54], 99, 76, 54]

list2 = copy.deepcopy(list1)

list2[4][1] = 1000

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(id(list1[4]))
print(id(list2[4]))

# Revision summary:
# - Part of the Prototype Pattern examples.
# - Shows the Deep Copyandshallow Copy example.
# - Use this file to review the pattern and understand its purpose.
