"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

"""


from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def hp(self):
        pass

    @abstractmethod
    def name(self):
        pass

class Player(Character):
    def __init__(self, name):
        self.__name = name
        self.__hp = 100
        self.__speed = 1

    def hp(self):
        return self.__hp

    def name(self):
        return self.__name

class StatsReporter:
    def __init__(self, char: Character):
        self.char = char

    def report(self):
        print(f'Name:{self.char.name()}')
        print(f'HP:{self.char.hp()}')
