import itertools

f = open("Inputs/Day17.txt", "r")
cubes = []

for j, x in enumerate(f):
    cubes.extend([{'x': int(i), 'y': int(j), 'z': 0, 'val': v} for i, v in enumerate(list(x.rstrip()))])

def calc_neighbours(cube):
    coords = []
    xs = [cube['x'] - 1, cube['x'], cube['x'] + 1]
    ys = [cube['y'] - 1, cube['y'], cube['y'] + 1]
    zs = [cube['z'] - 1, cube['z'], cube['z'] + 1]
    return [x for x in itertools.product(xs, ys, zs) if x != (cube['x'], cube['y'], cube['z'])]

def cube_by_position(x, y, z):
    for c in cubes:
        if c['x'] == x and c['y'] == y and c['z'] == z:
            return c
    return None

# each cycle, expand the list so that all neighbours are available to 
# operate on
def init_neighbours(cube):
    current_active = active_range(cubes)
    for x, y, z in calc_neighbours(cube):
        if cube_by_position(x, y, z) == None:
            if (x <= current_active['maxx'] + 1 and x >= current_active['minx'] - 1) and (y <= current_active['maxy'] + 1 and y >= current_active['miny'] - 1) and (z <= current_active['maxz'] + 1 and z >= current_active['minz'] - 1):
                cube = {'x': x, 'y': y, 'z': z, 'val': '.'}
                cubes.append(cube)

def switch_nodes(cubes, cube):
    enabled_count = 0
    disabled_count = 0
    for x, y, z in calc_neighbours(cube):
        v = cube_by_position(x, y, z)
        if (v != None):
            c = v['val']        
            if (c == '#'):
                enabled_count += 1
            else:
                disabled_count += 1
    #If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
    if cube['val'] == '#' and enabled_count != 2 and enabled_count != 3:
        return 'off'
     # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
    if cube['val'] == '.' and enabled_count == 3:
        return 'on'

def active_range(cubes):
    x_range = set([x['x'] for x in cubes if x['val'] == '#'])
    y_range = set([x['y'] for x in cubes if x['val'] == '#'])
    z_range = set([x['z'] for x in cubes if x['val'] == '#'])
    return {'minx': min(x_range), 'maxx': max(x_range), 'miny': min(y_range), 'maxy': max(y_range), 'minz': min(z_range), 'maxz': max(z_range)}

def print_layers(cubes):
    x_range = set([x['x'] for x in cubes])
    y_range = set([x['y'] for x in cubes])
    z_range = set([x['z'] for x in cubes])
    z = min(z_range)
    while z <= max(z_range):
        print('Z layer {}'.format(z))
        y = min(y_range)
        while y <= max(y_range):
            x = min(x_range)
            line = ''
            while x <= max(x_range):
                cube = cube_by_position(x, y, z)
                if cube == None:
                    line += '.'
                else:
                    line += cube['val']
                x += 1
            print(line)
            y += 1
        z += 1

print(len(cubes))
turn = 0
while turn < 6:
    print('working on turn: ' + str(turn))
    #print_layers(cubes)
    turn += 1
    switch_on = []
    switch_off = []
    for i in range(len(cubes)):
        init_neighbours(cubes[i])
    for c in cubes:
        action = switch_nodes(cubes, c)
        if (action == 'on'):
            switch_on.append(c)
        if (action == 'off'):
            switch_off.append(c)
    for c in switch_on:
        c['val'] = '#'
    for c in switch_off:
        c['val'] = '.'
    print(len([c for c in cubes if c['val'] == '#']))
