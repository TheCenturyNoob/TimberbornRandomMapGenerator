import os
import zipfile
from datetime import datetime
from typing import Dict

from data import Map

jsonBase: dict = {
    'GameVersion': None,
    'Timestamp': None,
    'Singletons': {
        'MapSize': {
            'Size': {
                'X': None,
                'Y': None
            }
        },
        'TerrainMap': {
            'Heights': {
                'Array': None
            }
        },
        'CameraStateRestorer': {
            'SavedCameraState': {
                'Target': {
                    'X': 0.0,
                    'Y': 0.0,
                    'Z': 0.0
                },
                'ZoomLevel': 0.0,
                'HorizontalAngle': 30.0,
                'VerticalAngle': 70.0
            }
        },
        'WaterMap': {
            'WaterDepths': {
                'Array': None
            },
            'Outflows': {
                'Array': None
            }
        },
        'SoilMoistureSimulator': {
            'MoistureLevels': {
                'Array': None
            }
        }
    },
    'Entities': []
}


def mapToJson(randomMap: Map) -> Dict:
    newMap = jsonBase.copy()

    newMap['GameVersion'] = '0.1.1.0-b735201-sw'
    newMap['Timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    newMap['Singletons']['MapSize']['Size']['X'] = randomMap.size_x
    newMap['Singletons']['MapSize']['Size']['Y'] = randomMap.size_y
    newMap['Singletons']['TerrainMap']['Heights']['Array'] = randomMap.getHeights()
    newMap['Singletons']['WaterMap']['WaterDepths']['Array'] = randomMap.getWaterDepths()
    newMap['Singletons']['WaterMap']['Outflows']['Array'] = randomMap.getWaterOutflows()
    newMap['Singletons']['SoilMoistureSimulator']['MoistureLevels']['Array'] = randomMap.getMoistureLevels()

    return newMap


def saveMap(randomMap: Map, filename: str, targetDirectory: str = '.') -> None:
    mapJson: Dict = mapToJson(randomMap)
    with open('world.json', 'w') as f:
        f.write(str(mapJson).replace('\'', '"'))
    with zipfile.ZipFile(f'{os.path.join(targetDirectory, filename)}.timber', 'w') as f:
        f.write('world.json')
    # os.remove('world.json')
