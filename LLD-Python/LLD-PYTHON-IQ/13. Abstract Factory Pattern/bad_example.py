"""Abstract Factory Pattern - Bad Example

This file shows the bad example implementation in the Abstract Factory Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass


# ============= NORTH INDIAN DISHES =============


class PaneerTikka(Food):
    def prepare(self):
        print("Preparing Paneer Tikka (North Indian Starter)")


class ButterChicken(Food):
    def prepare(self):
        print("Preparing Butter Chicken (North Indian Main Course)")


class GulabJamun(Food):
    def prepare(self):
        print("Preparing Gulab Jamun (North Indian Dessert)")


# ============= SOUTH INDIAN DISHES =============


class MeduVada(Food):
    def prepare(self):
        print("Preparing Medu Vada (South Indian Starter)")


class Dosa(Food):
    def prepare(self):
        print("Preparing Dosa (South Indian Main Course)")


class Payasam(Food):
    def prepare(self):
        print("Preparing Payasam (South Indian Dessert)")


# ============= CHINESE DISHES =============


class SpringRolls(Food):
    def prepare(self):
        print("Preparing Spring Rolls (Chinese Starter)")


class FriedRice(Food):
    def prepare(self):
        print("Preparing Fried Rice (Chinese Main Course)")


class FortuneCookie(Food):
    def prepare(self):
        print("Preparing Fortune Cookie (Chinese Dessert)")


class RestaurantService:
    def create_meal(self, cuisine_type: str):
        if cuisine_type == "north_indian":
            starter = PaneerTikka()
            main_course = ButterChicken()
            dessert = GulabJamun()

        elif cuisine_type == "south_indian":
            starter = MeduVada()
            main_course = Dosa()
            dessert = Payasam()

        elif cuisine_type == "chinese":
            starter = SpringRolls()
            main_course = FriedRice()
            dessert = FortuneCookie()

        else:
            print("Cuisine not available!")
            return None

        # Prepare the meal
        starter.prepare()
        main_course.prepare()
        dessert.prepare()


restaurant = RestaurantService()
restaurant.create_meal("north_indian")

# Revision summary:
# - Part of the Abstract Factory Pattern examples.
# - Shows the bad example implementation.
# - Use this file to review the pattern and understand its purpose.
