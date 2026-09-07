"""Abstract Factory Pattern - Good Example

This file shows the good example implementation in the Abstract Factory Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from abc import ABC, abstractmethod


class Starter(ABC):
    @abstractmethod
    def prepare(self):
        pass


class MainCourse(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Dessert(ABC):
    @abstractmethod
    def prepare(self):
        pass


# ============= NORTH INDIAN DISHES =============


class PaneerTikka(Starter):
    def prepare(self):
        print("Preparing Paneer Tikka (North Indian Starter)")


class ButterChicken(MainCourse):
    def prepare(self):
        print("Preparing Butter Chicken (North Indian Main Course)")


class GulabJamun(Dessert):
    def prepare(self):
        print("Preparing Gulab Jamun (North Indian Dessert)")


# ============= SOUTH INDIAN DISHES =============


class MeduVada(Starter):
    def prepare(self):
        print("Preparing Medu Vada (South Indian Starter)")


class Dosa(MainCourse):
    def prepare(self):
        print("Preparing Dosa (South Indian Main Course)")


class Payasam(Dessert):
    def prepare(self):
        print("Preparing Payasam (South Indian Dessert)")


# ============= CHINESE DISHES =============


class SpringRolls(Starter):
    def prepare(self):
        print("Preparing Spring Rolls (Chinese Starter)")


class FriedRice(MainCourse):
    def prepare(self):
        print("Preparing Fried Rice (Chinese Main Course)")


class FortuneCookie(Dessert):
    def prepare(self):
        print("Preparing Fortune Cookie (Chinese Dessert)")


class CuisineFactory(ABC):
    @abstractmethod
    def create_starter(self) -> Starter:
        pass

    @abstractmethod
    def create_main_course(self) -> MainCourse:
        pass

    @abstractmethod
    def create_dessert(self) -> Dessert:
        pass


class NorthIndianCuisine(CuisineFactory):
    def create_starter(self) -> Starter:
        return PaneerTikka()

    def create_main_course(self) -> MainCourse:
        return ButterChicken()

    def create_dessert(self) -> Dessert:
        return GulabJamun()


class ChineseCuisine(CuisineFactory):
    def create_starter(self) -> Starter:
        return SpringRolls()

    def create_main_course(self) -> MainCourse:
        return FriedRice()

    def create_dessert(self) -> Dessert:
        return FortuneCookie()


class RestaurantService:
    def __init__(self, factory: CuisineFactory):
        self.__factory = factory

    def create_meal(self):
        starter = self.__factory.create_starter()
        main_course = self.__factory.create_main_course()
        dessert = self.__factory.create_dessert()

        starter.prepare()
        main_course.prepare()
        dessert.prepare()

    def change_cuisine(self, new_factory: CuisineFactory):
        self.__factory = new_factory


north_indian_cuisine = NorthIndianCuisine()
restaurant_service = RestaurantService(north_indian_cuisine)
restaurant_service.create_meal()

chinese = ChineseCuisine()
restaurant_service.change_cuisine(chinese)
restaurant_service.create_meal()

# Revision summary:
# - Part of the Abstract Factory Pattern examples.
# - Shows the good example implementation.
# - Use this file to review the pattern and understand its purpose.
