import math

rows = []

f = open("Inputs/Day12.txt", "r")
for x in f:
    rows.append([x.rstrip()[0], int(x.rstrip()[1:])])

position = {'x': 0, 'y':0}
waypoint_pos = {'x': 10, 'y': 1}

direction = {    
    0: {'x_d': 1, 'y_d' : 0}, 
    1: {'x_d': 0, 'y_d' : -1},
    2: {'x_d': -1, 'y_d' : 0},
    3: {'x_d': 0, 'y_d' : 1}}
current_direction = 0

direction_map = {
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3
}

#Action N means to move the waypoint north by the given value.
#Action S means to move the waypoint south by the given value.
#Action E means to move the waypoint east by the given value.
#Action W means to move the waypoint west by the given value.
def move_waypoint_in_direction(arg1, arg2):
    m_direction = direction[direction_map[arg1]]
    waypoint_pos['x'] += arg2 * m_direction['x_d']
    waypoint_pos['y'] += arg2 * m_direction['y_d']

rotation_direction = {    
    0: {'x_d': 0, 'y_d' : 0}, 
    1: {'x_d': 1, 'y_d' : 1},
    2: {'x_d': 0, 'y_d' : 2},
    3: {'x_d': -1, 'y_d' : -1}}


def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.
    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


#Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
#Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
def rotate_waypoint(arg1, arg2):    
    radian_rotate = math.radians(arg2) 
    if arg1 == 'R':
        radian_rotate = radian_rotate * -1
    abs_waypoint_pos = (position['x'] + waypoint_pos['x'], position['y'] + waypoint_pos['y'])
    new_abs_waypoint_pos = rotate((position['x'], position['y']), abs_waypoint_pos, radian_rotate)
    newx, newy = new_abs_waypoint_pos
    waypoint_pos['y'] = newy - position['y']
    waypoint_pos['x'] = newx - position['x']

#Action F means to move forward to the waypoint a number of times equal to the given value.
def move_forward(arg1, arg2):
    position['x'] += arg2 * waypoint_pos['x']
    position['y'] += arg2 * waypoint_pos['y']

move_functions = { 'N': move_waypoint_in_direction, 'E': move_waypoint_in_direction,
    'W': move_waypoint_in_direction, 'S': move_waypoint_in_direction,
    'L': rotate_waypoint, 'R': rotate_waypoint, 'F': move_forward }

for instruction in rows:
    move_functions[instruction[0]](instruction[0], instruction[1])

print (abs(position['x']) + abs(position['y']))