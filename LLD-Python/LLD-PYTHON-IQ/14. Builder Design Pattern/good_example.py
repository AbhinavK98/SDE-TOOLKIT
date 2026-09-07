"""Builder Design Pattern - Good Example

This file shows the good example implementation in the Builder Design Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

class Laptop:
    processor = None
    ram = None
    graphic_card = None
    color = None
    screen_size = None

    def display_specs(self):
        if self.processor:
            print(f"processor = {self.processor}")
        if self.ram:
            print(f"Ram = {self.ram}")
        if self.graphic_card:
            print(f"Graphic Card = {self.graphic_card}")
        if self.color:
            print(f"Color = {self.color}")
        if self.screen_size:
            print(f"Screen Size = {self.screen_size}")


class LaptopBuilder:
    def __init__(self):
        self.__laptop = Laptop()

    def set_processor(self, processor: str):
        self.__laptop.processor = processor
        return self

    def set_ram(self, ram: str):
        self.__laptop.ram = ram
        return self

    def set_graphic_card(self, graphic_card: str):
        self.__laptop.graphic_card = graphic_card
        return self

    def set_color(self, color: str):
        self.__laptop.color = color
        return self

    def set_screen_size(self, screen_size: str):
        self.__laptop.screen_size = screen_size
        return self

    def build(self):
        return self.__laptop


l = LaptopBuilder().set_processor("i5-43423").set_ram("5").set_color("black").build()
l.display_specs()

# Revision summary:
# - Part of the Builder Design Pattern examples.
# - Shows the good example implementation.
# - Use this file to review the pattern and understand its purpose.
