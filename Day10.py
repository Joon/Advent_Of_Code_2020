adaptor_jolts = []

f = open("Inputs/Day10.txt", "r")

for x in f:
    adaptor_jolts.append(int(x))
    
print(adaptor_jolts)

jolt_target = max(adaptor_jolts)
combos = []
start = 0
current_len = 2

add_number = 0
for x in adaptor_jolts:
    if x <= 3:
        combo = {}
        combo['combos'] = [0, x]
        combo['max'] = x
        combo['last_round'] = 0
        combos.append(combo)
        
def fork_combo(combos, start_combo, start_combos, add_index, add_number, process_round):
    if (add_index == 1):
        start_combo['max'] = add_number
        start_combo['combos'].append(add_number)
        start_combo['last_round'] = process_round
    else:
        combo = {}
        combo['combos'] = start_combos.copy()
        combo['combos'].append(add_number)
        combo['max'] = add_number
        combo['last_round'] = process_round
        combos.append(combo)
        
smallest_combo_end = 1
process = True
process_round = 0
while process:
    process_round += 1
    # Process all combos that exist at this stage
    for x in range(len(combos)):
        start_combo = combos[x]
        orig_max = start_combo['max']
        start_combos = start_combo['combos'].copy()
        add_index = 0
        for add_number in adaptor_jolts:
            if add_number > orig_max and add_number <= (orig_max + 3):
                add_index += 1
                fork_combo(combos, start_combo, start_combos, add_index, add_number, process_round)
    
    for y in range(len(combos) - 1, -1, -1):
        combo = combos[y]
        # Is this a stale branch, i.e. won't match anythign else?
        if combo['max'] < jolt_target and combo['last_round'] < process_round:
            print('deleting')
            del combos[y]
    
    smallest_combo_end = min(x['max'] for x in combos)
    # Continue until all the combos are at the max
    process = smallest_combo_end < jolt_target

print(len(combos))