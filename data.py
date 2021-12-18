from typing import List


class Map:
    def __init__(self, heights, entities):
        self.heights: List[List[int]] = heights
        self.entities: List = entities
        self.size_x: int = len(heights)
        self.size_y: int = len(heights[0])

    def getHeights(self) -> str:
        return ' '.join('0' for _ in range(self.size_x * self.size_y))

    def getWaterDepths(self) -> str:
        return ' '.join('0' for _ in range(self.size_x * self.size_y))

    def getWaterOutflows(self) -> str:
        return ' '.join('0:0:0:0' for _ in range(self.size_x * self.size_y))

    def getMoistureLevels(self) -> str:
        return ' '.join('0' for _ in range(self.size_x * self.size_y))

