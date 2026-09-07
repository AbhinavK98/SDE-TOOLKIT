"""Composite Pattern - Bad Example

This file shows the bad example implementation in the Composite Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from typing import List


class File:
    def __init__(self, name: str):
        self.__name = name

    def show_details(self):
        return f"File : {self.__name}"


class Folder:
    def __init__(self, name: str):
        self.__name = name
        self.__files: List[File] = []

    def add_file(self, file: File):
        self.__files.append(file)

    def show_details(self):
        print(f"Folder name: {self.__name}")
        for file in self.__files:
            print(file.show_details())


file1 = File("image.png")
file2 = File("ppt")
file3 = File("word.exe")

folder = Folder("my_drive")

folder.add_file(file1)
folder.add_file(file2)
folder.add_file(file3)

folder.show_details()

# Revision summary:
# - Part of the Composite Pattern examples.
# - Shows the bad example implementation.
# - Use this file to review the pattern and understand its purpose.
