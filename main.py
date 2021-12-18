from mapGenerator import generateMap
from saveIO import saveMap

if __name__ == '__main__':
    randomMap = generateMap(x=12, y=12)
    saveMap(randomMap=randomMap, filename='test')
