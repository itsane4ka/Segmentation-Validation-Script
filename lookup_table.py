import numpy as np


COLOR_TABLE_DICT = {
        "Hidden":                [0, 255, 255],      # 00 Hidden
        "TopOfRail":             [255, 255, 0],      # 01 TopOfRail
        "WebOfRail":             [100, 60, 60],      # 02 WebOfRail
        "RailFoot":              [100, 200, 100],    # 03 RailFoot
        "Mounting":              [0, 0, 255],        # 04 Mounting
        "SwitchBladeTip":        [115, 115, 0],      # 05 SwitchBladeTip
        "WheelGuide":            [123, 14, 214],     # 06 WheelGuide
        "WeldingSpot":           [187, 187, 0],      # 07 WeldingSpot
        "Clip":                  [255, 192, 130],    # 08 Clip
        "Screw":                 [50, 90, 80],       # 09 Screw
        "ButtStrap":             [0, 255, 190],      # 10 ButtStrap
        "IsolatingStrap":        [128, 128, 0],      # 11 IsolatingStrap
        "Ballast":               [127, 127, 127],    # 12 Ballast
        "TieConcrete":           [180, 0, 180],      # 13 TieConcrete
        "TieSteel":              [255, 0, 255],      # 14 TieSteel
        "TieWood":               [100, 0, 100],      # 15 TieWood
        "Cable":                 [125, 100, 35],     # 16 Cable
        "CableLookAlikes":       [125, 125, 100],    # 17 CableLookAlikes
        "Obstacle":              [240, 230, 140],    # 18 Obstacle
        "Other":                 [0, 0, 0]           # 19 Other
}

LABEL_RGB_PALETTE = np.array([COLOR_TABLE_DICT[k] for k in COLOR_TABLE_DICT.keys()]).astype(np.uint8)
