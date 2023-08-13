# Abstract class to draw graphs

from abc import ABC, abstractmethod


class Chart(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def draw_chart(self, expenses: list):
        pass
