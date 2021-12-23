from collections import namedtuple

StepInfo = namedtuple("StepInfo", ['x','y','v_x', 'v_y'])


def run():
    target_range = get_input("day17/input.txt")
    return calc(target_range)


def get_input(file):
    
    with open(file, encoding="utf8") as f:
        line = f.readline()
    _, coords = line.split(': x=')
    x_range, y_range = coords.split(', y=')
    x_min, x_max = x_range.split('..')
    y_min, y_max = y_range.split('..')

    return (
        (int(x_min), int(x_max)),
        (int(y_min), int(y_max)) )
    

def calc(target_range):
    x_range, y_range = target_range
    x_min, x_max = x_range
    y_min, y_max = y_range
    count = 0
    v_y = y_min-2
    for v_x in range(x_max+1):
        for v_y in range(y_min-1, max(abs(y_min), abs(y_max))): 
            height = test_velosity(target_range, v_x, v_y)
            if height != None:
                count += 1
    return count


def test_velosity(target_range, v_x, v_y):
    max_y = 0
    step_info = StepInfo(0, 0, v_x, v_y)
    while moving_toward_target(target_range, step_info):
        if step_info.y > max_y:
            max_y = step_info.y
        if point_in_target_area(target_range,(step_info.x, step_info.y)):
            return max_y
        step_info = next_step(step_info)
    return None


def next_step(step_info):
    x = step_info.x + step_info.v_x
    y = step_info.y + step_info.v_y
    v_y = step_info.v_y - 1
    v_x = step_info.v_x
    if v_x > 0:
        v_x -= 1
    elif v_x < 0:
        v_x += 1

    return StepInfo(x,y, v_x, v_y)


def point_in_target_area(target_range, point):
    x_range, y_range = target_range
    x_min, x_max = x_range
    y_min, y_max = y_range
    x,y = point
    #print(f"{x_min} <= {x} <= {x_max} and {y_min} <= {y} <= {y_max}")
    return x_min <= x <= x_max and y_min <= y <= y_max


def moving_toward_target(target_range, step_info):
    x_range, y_range = target_range
    y_min, y_max = y_range
    #print(f"    {step_info.v_y} >= 0 or {step_info.y} > {y_min}")
    return step_info.v_y >= 0 or step_info.y >= y_min
