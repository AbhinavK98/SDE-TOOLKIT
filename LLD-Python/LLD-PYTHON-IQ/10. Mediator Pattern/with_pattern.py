"""Mediator Pattern - With Pattern

This file shows the With Pattern example in the Mediator Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from abc import ABC, abstractmethod
from typing import List


class AirTrafficControl(ABC):
    @abstractmethod
    def register_airplane(self):
        pass

    @abstractmethod
    def send_message(self):
        pass


class ControlTower(AirTrafficControl):
    def __init__(self):
        self.__airplanes: List[Airplane] = []

    def register_airplane(self, new_airplane: "Airplane"):
        self.__airplanes.append(new_airplane)

    def send_message(self, msg: str, sender: "Airplane"):
        for airplane in self.__airplanes:
            if airplane != sender:
                airplane.receive_message(msg, sender)


class Airplane:
    def __init__(self, flight_number: str, tower: "ControlTower"):
        self.__flight_number = flight_number
        self.__tower = tower

        self.__tower.register_airplane(self)

    def send_message(self, msg: str):
        self.__tower.send_message(msg, self)

    def get_flight_number(self) -> str:
        return self.__flight_number

    def receive_message(self, msg: str, who_sent: "Airplane"):
        print(f"{self.__flight_number} got {msg} from {who_sent.get_flight_number()}")


control_tower = ControlTower()
air_india = Airplane("AIR-546", control_tower)
spicejet = Airplane("SPICE-87171", control_tower)
indigo = Airplane("IND-9911", control_tower)

air_india.send_message("I am getting on runway")

express = Airplane("EXP-1122", control_tower)
express.send_message("I am getting on runway")

# Revision summary:
# - Part of the Mediator Pattern examples.
# - Shows the With Pattern example.
# - Use this file to review the pattern and understand its purpose.
