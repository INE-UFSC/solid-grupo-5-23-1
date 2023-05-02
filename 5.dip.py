"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

"""
from abc import ABC, abstractmethod


class IStatsReporter(ABC):

    def __init__(self, char: Player):
        self.__char = char

    @abstractmethod
    def report(self):
        pass

class Player:
    def __init__(self, name, stats: IStatsReporter):
        self.__stats = stats
        self.__name = name
        self.__hp = 100
        self.__speed = 1

    def hp(self):
        return self.__hp

    def name(self):
        return self.__name
    
    def speed(self):
        return self.__speed
    
    def report(self):
        return self.__stats.report()

class StatsReporter(IStatsReporter):
    def __init__(self, char: Player):
        super().__init__(char)

    def report(self):
        print(f'Name:{super().char.name()}')
        print(f'HP:{super().char.hp()}')
        print(f'Speed:{super().char.speed()}')
