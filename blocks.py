BLOCK_SIZE = 5

BLOCKS = {
    "water": {
        "min_layer": -0.1,
        "max_layer": 15,
        "color": (0, 0, 200)
    },

    "sand": {
        "min_layer": 15,
        "max_layer": 25,
        "color": (255, 255, 80)
    },

    "grass": {
        "min_layer": 25,
        "max_layer": 60,
        "color": (0, 160, 0)
    },

    "stone": {
        "min_layer": 60,
        "max_layer": 80,
        "color": (100, 100, 100)
    },
    
    "snow": {
        "min_layer": 80,
        "max_layer": 100,
        "color": (255, 255, 255)
    },
}

BIOMES = {
    "grassland": {
        "temp": 0.1
    }
}

def pick_block(noise: float):
    for block_name, data in BLOCKS.items():
        if data["min_layer"] <= noise < data["max_layer"]:
            return data
    return None

if __name__ == '__main__':
    print(pick_block(1))