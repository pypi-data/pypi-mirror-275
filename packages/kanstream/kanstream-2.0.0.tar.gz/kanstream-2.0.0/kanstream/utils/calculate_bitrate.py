from functools import lru_cache

import numpy as np


@lru_cache(maxsize=128)
def calculate_bitrate(width: int, height: int, fps: int):
    dictionary = {
        (160, 120): {15: 130},
        (120, 120): {15: 100},
        (320, 180): {15: 280},
        (180, 180): {15: 200},
        (240, 180): {15: 240},
        (320, 240): {15: 400},
        (240, 240): {15: 280},
        (424, 240): {15: 440},
        (640, 360): {15: 800, 30: 1200},
        (360, 360): {15: 520, 30: 800},
        (480, 360): {15: 640, 30: 980},
        (640, 480): {10: 800, 15: 1000, 30: 1500},
        (480, 480): {15: 800, 30: 1200},
        (848, 480): {15: 1220, 30: 1860},
        (960, 720): {15: 1820, 30: 2760},
        (1280, 720): {15: 2260, 30: 3420},
        (1920, 1080): {15: 4160, 30: 6300}
    }

    size = width, height

    if dictionary.get(size) and fps in dictionary[size]:
        return dictionary[size][fps]

    sizes = np.asarray(list(dictionary.keys()))
    distances = np.linalg.norm(sizes - size, axis=1)
    nearest_size = sizes[np.argmin(distances)]

    fps_dict = dictionary[tuple(nearest_size)]
    if fps in fps_dict:
        return fps_dict[fps]

    func = lambda x: -0.00066667 * x ** 2 + 0.06333333 * x + 0.2
    bit_rate = round(func(fps) * fps_dict[15])

    return bit_rate
