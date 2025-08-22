BLOCK_SIZE = 5



BLOCKS = {
    "deep_ocean": {
        "id": 0,
        "min_layer": -100,
        "max_layer": -30,
        "color": (0, 0, 150)
    },

    "ocean": {
        "id": 1,
        "min_layer": -30,
        "max_layer": 0,
        "color": (0, 0, 200)
    },

    "sea": {
        "id": 2,
        "min_layer": 0,
        "max_layer": 15,
        "color": (0, 100, 255)
    },

    "sand": {
        "id": 3,
        "min_layer": 15,
        "max_layer": 25,
        "color": (255, 255, 80)
    },

    "grass": {
        "id": 4,
        "min_layer": 25,
        "max_layer": 60,
        "color": (0, 160, 0)
    },

    "stone": {
        "id": 5,
        "min_layer": 60,
        "max_layer": 80,
        "color": (100, 100, 100)
    },

    "snow": {
        "id": 6,
        "min_layer": 80,
        "max_layer": 100,
        "color": (255, 255, 255)
    },
}

BIOMES = {
    # Temp in Celcius Degrees
    "tundra": {
        "min_temp": -100,
        "max_temp": -20,
        "color": (200, 240, 255)
    },

    "forest": {
        "min_temp": -20,
        "max_temp": 35,
        "color": (34, 139, 34)
    },

    "desert": {
        "min_temp": 35,
        "max_temp": 70,
        "color": (210, 180, 140)
    }
}

def pick_block(height_noise: float, temp_noise: float):
    chosen_block = None
    for block_name, block_data in BLOCKS.items():
        if block_data['min_layer'] <= height_noise < block_data['max_layer']:
            chosen_block = block_data
            break

    if not chosen_block:
        return {"color": (0, 0, 0)} # error bro

    if chosen_block["id"] == BLOCKS["grass"]["id"]:
        for biome_name, biome_data in BIOMES.items():
            if biome_data['min_temp'] <= temp_noise <= biome_data['max_temp']:
                block_copy = chosen_block.copy()
                block_copy["color"] = biome_data["color"]
                return block_copy

    return chosen_block

if __name__ == '__main__':
    print(pick_block(1, 1))