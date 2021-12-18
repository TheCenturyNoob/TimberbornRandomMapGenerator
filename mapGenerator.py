from data import Map


def generateMap(x: int, y: int):
    heights = generateHeights(x, y)
    entities = generateEntities(heights)
    return Map(heights, entities)


def generateHeights(x: int, y: int):
    return [[0 for yi in range(y)] for xi in range(x)]


def generateEntities(heights):
    return []
