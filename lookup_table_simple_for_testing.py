import numpy as np


COLOR_TABLE_DICT = {
    "Background":               [255, 255, 255],    # 00 Back
    "Ballast":                  [0, 0, 0],          # 01 Front
}

LABEL_RGB_PALETTE = np.array([COLOR_TABLE_DICT[k] for k in COLOR_TABLE_DICT.keys()]).astype(np.uint8)
