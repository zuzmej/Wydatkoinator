# Draw bar graphs. Inherit abstract class Graph

from .chart import Chart


class Stack_chart(Chart):
    def __init__(self, chartview):
        super().__init__(chartview)
        
    def draw_chart(self, expenses: list):
        pass
