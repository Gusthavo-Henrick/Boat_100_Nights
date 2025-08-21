import time

def get_seed():
    seed = (123 * time.time() * 123) * 2 ** 5
    return seed

seed = get_seed()

def get_random_num(range_num: int, is_int: bool = True):
    random_num = (seed % range_num) + 1
    if is_int:
        random_num = int(random_num)
    return random_num

def shuffle_list(lst: list):
    for i in range(len(lst) - 1, 0, -1):
        j = get_random_num(i)
        lst[i], lst[j] = lst[j], lst[i]

    return lst

permutation: list[int] = [i for i in range(256)]
permutation = shuffle_list(permutation)
permutation *= 2

def floor(num: float):
    num_int = int(num)
    if num >= 0 or num_int == num:
        return num_int
    else:
        return num_int - 1

def get_gradient(hash_value, offset_x, offset_y):
    vectors = [
        (1, 1), (1, 0), (1, -1),
        (0, 1), (0, -1),
        (-1, 1), (-1, 0), (-1, -1)
    ]

    gradient = vectors[hash_value & 7]
    return gradient[0] * offset_x + gradient[1] * offset_y

def get_fade_curve(t):
    # 6t^5 - 15t^4 + 10t^3 (This is the equation, put it in geogebra)
    fade = t ** 3 * (t * (t * 6 - 15) + 10)
    return fade

def linear_interpolation(dot_left, dot_right, fade_weight):
    return dot_left + fade_weight * (dot_right - dot_left)

def get_perlin_noise(x, y, ampliation: float):
    x *= ampliation
    y *= ampliation

    floor_x = int(floor(x))
    floor_y = int(floor(y))

    cell_x = floor_x & 255
    cell_y = floor_y & 255

    local_x = x - floor_x
    local_y = y - floor_y

    fade_x = get_fade_curve(local_x)
    fade_y = get_fade_curve(local_y)

    corner_top_left = permutation[permutation[cell_x] + cell_y]
    corner_top_right = permutation[permutation[cell_x + 1] + cell_y]
    corner_bottom_left = permutation[permutation[cell_x] + cell_y + 1]
    corner_bottom_right = permutation[permutation[cell_x + 1] + cell_y + 1]

    dot_top_left = get_gradient(corner_top_left, local_x, local_y)
    dot_top_right = get_gradient(corner_top_right, local_x - 1, local_y)
    top_interpolation = linear_interpolation(dot_top_left, dot_top_right, fade_x)

    dot_bottom_left = get_gradient(corner_bottom_left, local_x, local_y - 1)
    dot_bottom_right = get_gradient(corner_bottom_right, local_x - 1, local_y - 1)
    bottom_interpolation = linear_interpolation(dot_bottom_left, dot_bottom_right, fade_x)

    final_interpolation = linear_interpolation(top_interpolation, bottom_interpolation, fade_y)
    return final_interpolation

def expand_noise(noise, expand_to: float | int, round_to: int = 2):
    if noise <= 0:
        return 0
    noise *= expand_to
    if round_to == 0:
        return int(noise)
    noise = round(noise, round_to)
    return noise

def get_color_noise(perlin_noise, type: str = 'rgb', is_num: bool = True):
    if not is_num:
        match type.lower():
            case 'hex':
                color = int(perlin_noise * 255)
                return f'#{color:02x}x{color:02x}{color:02x}'
            case 'rgb':
                color = int(perlin_noise * 255)
                return f'({color}, {color}, {color})'
            case _:
                color = int(perlin_noise * 255)
                return f'({color}, {color}, {color})'
    else:
        color = int(perlin_noise * 255)
        return (color, color, color)
    
if __name__ == '__main__':
    print(f'{seed = }')