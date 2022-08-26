import numpy as np


COLOR_TABLE_DICT = {
    "Background":               [255, 255, 255],    # 00 Background
    "Ballast":                  [127, 127, 127],    # 01 Ballast
    "TieWood":                  [100, 0, 100],      # 02 TieWood
    "TieConcrete":              [180, 0, 180],      # 03 TieConcrete
    "TieSteel":                 [255, 0, 255],      # 04 TieSteel
    "Rail":                     [255, 255, 0],      # 05 Rail
    "Vegetation":               [0, 255, 0],        # 06 Vegetation
    "Mounting":                 [0, 0, 255],        # 07 Mounting
    "Hidden":                   [0, 255, 255],      # 08 Hidden
    "Other":                    [0, 0, 0],          # 09 Other
    "SwitchBlade":              [191, 191, 0],      # 10 SwitchBlade
    "SwitchBladeTip":           [115, 115, 0],      # 11 SwitchBladeTip
    "SwitchRod":                [255, 0, 0],        # 12 SwitchRod
    "FrogFrame":                [255, 127, 0],      # 13 FrogFrame
    "Barrier":                  [240, 230, 140],    # 14 Barrier
    "Sensor":                   [0, 127, 127],      # 15 Sensor
    "Cable":                    [125, 100, 35],     # 16 Cable
    "WingRail":                 [253, 250, 255],    # 17 WingRail
    "WheelGuide":               [123, 14, 214],     # 18 WheelGuide
    "SwitchBladeSpacer":        [0, 112, 0],        # 19 SwitchBladeSpacer
    "ButtStrap":                [0, 255, 190],      # 20 ButtStrap
    "CableDuct":                [125, 100, 75],     # 21 CableDuct
    "SlidingPlate":             [0, 110, 255],      # 22 SlidingPlate
    "Screw":                    [50, 90, 80],       # 23 Screw
    "SwitchBladeBearing":       [102, 77, 179],     # 24 SwitchBladeBearing
    "SwitchEngine":             [102, 0, 0],        # 25 SwitchEngine
    "Frog":                     [171, 73, 0],       # 26 Frog
    "LeadWire":                 [125, 100, 0],      # 27 LeadWire
    "DoubleSlipeSwitch":        [200, 200, 200],    # 28 DoubleSlipeSwitch
    "SwitchEngineMount":        [180, 0, 0],        # 29 SwitchEngineMount
    "CableLookalikes":          [125, 100, 100],    # 30 CableLookalikes
    "SleeperAnchor":            [60, 190, 200],     # 31 SleeperAnchor
    "RailFootObject":           [255, 50, 0],       # 32 RailFootObject
    "ExpansionJointStabilizer": [200, 60, 60],      # 33 ExpansionJointStabilizer
    "UnknownObject":            [255, 100, 0],      # 34 UnknownObject
}

LABEL_RGB_PALETTE = np.array([COLOR_TABLE_DICT[k] for k in COLOR_TABLE_DICT.keys()]).astype(np.uint8)
