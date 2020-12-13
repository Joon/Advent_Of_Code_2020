rows = []

f = open("Inputs/Day12.txt", "r")
for x in f:
    rows.append([x.rstrip()[0], int(x.rstrip()[1:])])

position = {'x': 0, 'y':0}
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

#Action N means to move north by the given value.
#Action S means to move south by the given value.
#Action E means to move east by the given value.
#Action W means to move west by the given value.
def move_in_direction(arg1, arg2):
    m_direction = direction[direction_map[arg1]]
    position['x'] += arg2 * m_direction['x_d']
    position['y'] += arg2 * m_direction['y_d']

#Action L means to turn left the given number of degrees.
#Action R means to turn right the given number of degrees.
def turn(arg1, arg2):
    if arg1 == 'R':
        action = 1
    if arg1 == 'L':
        action = -1
    increment = action * (arg2 / 90)
    global current_direction
    current_direction = (current_direction + increment) % 4

#Action F means to move forward by the given value in the direction the ship is currently facing.
def move_forward(arg1, arg2):
    m_direction = direction[current_direction]
    position['x'] += arg2 * m_direction['x_d']
    position['y'] += arg2 * m_direction['y_d']

move_functions = { 'N': move_in_direction, 'E': move_in_direction,
    'W': move_in_direction, 'S': move_in_direction,
    'L': turn, 'R': turn, 'F': move_forward }

for instruction in rows:
    move_functions[instruction[0]](instruction[0], instruction[1])

print (abs(position['x']) + abs(position['y']))