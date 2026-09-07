"""Template Pattern - Pattern

This file shows the Pattern example in the Template Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from abc import ABC, abstractmethod


class DataParser(ABC):
    def parse(self):
        self._open()
        self._dataParser()
        self._close()

    def _open(self):
        print("Opening the file")

    def _close(self):
        print("Closing the file")

    @abstractmethod
    def _dataParser(self):
        pass


class CSVParser(DataParser):
    def _dataParser(self):
        print("Parsing CSV File")


csv_parser = CSVParser()
csv_parser.parse()

# Revision summary:
# - Part of the Template Pattern examples.
# - Shows the Pattern example.
# - Use this file to review the pattern and understand its purpose.
