import math

def solution(dimensions, your_position, guard_position, distance):
    # dict of distance from your position to your mirrored positions, keys are atan2(y, x)
    radians_of_you = generate_radian_of_you(dimensions, your_position, guard_position, distance)
    # dict of count of guard positions with the same radian, keys are atan2(y, x)
    radians_of_guard = {}

    mirrored_guard_x_positions = get_mirrored_positions(dimensions[0], guard_position[0], your_position[0], distance)
    mirrored_guard_y_positions = get_mirrored_positions(dimensions[1], guard_position[1], your_position[1], distance)
    available_position_count = 0

    for y in mirrored_guard_y_positions:
        for x in mirrored_guard_x_positions:
            current_radian = math.atan2(your_position[1] - y, your_position[0] - x)
            current_distance = hypotenuse(your_position[1] - y, your_position[0] - x)
            # The beam get to your mirrored position before the mirrored guard position
            if current_radian in radians_of_you and radians_of_you[current_radian] < current_distance:
                continue
            # The current direction was counted
            if current_radian in radians_of_guard:
                radians_of_guard[current_radian] += 1
                continue
            if current_distance > distance:
                continue
            radians_of_guard[current_radian] = 1
            available_position_count += 1
    return available_position_count

def generate_radian_of_you(dimensions, your_position, guard_position, distance):
    radians_of_you = {}
    mirrored_your_x_positions = get_mirrored_positions(dimensions[0], your_position[0], your_position[0], distance)
    mirrored_your_y_positions = get_mirrored_positions(dimensions[1], your_position[1], your_position[1], distance)
    for y in mirrored_your_y_positions:
        for x in mirrored_your_x_positions:
            if x == your_position[0] and y == your_position[1]:
                continue
            current_radian = math.atan2(your_position[1] - y, your_position[0] - x)
            current_distance =  hypotenuse(your_position[1] - y, your_position[0] - x)
            if current_radian in radians_of_you and radians_of_you[current_radian] < current_distance:
                continue
            radians_of_you[current_radian] = current_distance
    return radians_of_you

def get_mirrored_positions(dimension, guard_position, your_position, distance):
    available_position = []
    vector_arrays = [[guard_position * -2, guard_position * 2 - dimension * 2],
                    [dimension * 2 - guard_position * 2, guard_position * 2]]
    for vector_array in vector_arrays:
        current_array_key = 0
        current_position = guard_position
        while abs(current_position - your_position) <= distance:
            available_position.append(current_position)
            current_position += vector_array[current_array_key]
            current_array_key = (current_array_key + 1) % 2
    return available_position[1:]

def hypotenuse(leg1, leg2):
    return math.sqrt(leg1**2 + leg2**2)
