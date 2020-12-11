rows = []

f = open("Inputs/Day11.txt", "r")
for x in f:
    rows.append(list(x.rstrip()))
    
print(rows)

def find_next_seat(all_lines, x, delta_x, y, delta_y):
    max_x = len(all_lines[0]) - 1
    max_y = len(all_lines) - 1
    while x <= max_x and y <= max_y:
        x = x + delta_x
        y = y + delta_y
        if (x < 0 or y < 0 or x > max_x or y > max_y):
            return '.'
        if (all_lines[y][x] == '#'):
            return '#'
        if (all_lines[y][x] == 'L'):
            return 'L'
    return '.'

# Count occupied seats in all seats immediately adjacent (front, back, left, right) 
# around the target seat - max value is 8
def count_occupied_los(all_lines, x, y):
    occupied = 0
    
    for delta_y in [-1, 0, 1]:
        for delta_x in [-1, 0, 1]:
            if delta_x == 0 and delta_y == 0:
                continue                
            if find_next_seat(all_lines, x, delta_x, y, delta_y) == '#':
                occupied += 1
    return occupied
       
        
#If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
def occupy_seats_los(all_lines, y):
    occupy_apply = []
    line = all_lines[y]
    for x in range(0, len(line)):        
        if (line[x] == 'L'):
            occupy_count = count_occupied_los(all_lines, x, y)
            if (occupy_count == 0):
                occupy_apply.append(x)
    return occupy_apply
    
#If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
def unoccupy_seats_los(all_lines, y):
    line = all_lines[y]
    unoccupy_apply = []
    for x in range(0, len(line)):        
        if (line[x] == '#'):
            occupy_count = count_occupied_los(all_lines, x, y)
            if (occupy_count >= 5):
                unoccupy_apply.append(x)
    return unoccupy_apply

# Part 2: Find stabilization - look for first seat in every direction, instead of adjacent
moved_rows = rows.copy()
changed = True
while changed:
    prevline = []
    seats_to_occupy = []
    seats_to_clear = []
    for i in range(len(moved_rows)):
        seats_to_occupy.append(occupy_seats_los(moved_rows, i))
        seats_to_clear.append(unoccupy_seats_los(moved_rows, i))
    
    for i in range(len(moved_rows)):
        for occupy_index in seats_to_occupy[i]:
            moved_rows[i][occupy_index] = '#'
        for clear_index in seats_to_clear[i]:
            moved_rows[i][clear_index] = 'L'
        
    all_changes = sum([len(l) for l in seats_to_occupy]) + sum([len(l) for l in seats_to_clear])
    print(str(all_changes) + ' seats changed')
    changed = all_changes > 0
    
print("Part 2 Occupied at stabilization: " + str(sum([l.count('#') for l in moved_rows])))
