import functools 

f = open("Inputs/Day16_Tickets.txt", "r")
ticketvals = []
for x in f:
    vals = x.rstrip().split(',')
    ticketvals.append([int(v) for v in vals])


f = open("Inputs/Day16_rules.txt", "r")
fields = []
for x in f:
    rule_data = x.rstrip().split(':')
    rule = { 'field': rule_data[0] }
    
    ranges = rule_data[1].split(' or ')
    rule['ranges'] = []
    for r in ranges:
        numbers = r.split('-')
        rule_range = int(numbers[0]), int(numbers[1])
        rule['ranges'].append(rule_range)
    fields.append(rule)

f = open("Inputs/Day16_My_ticket.txt", "r")
my_ticket = []
for x in f:
    my_ticket = [int(v) for v in x.split(',')]

def valid_number(num, ranges):
    for (min_val, max_val) in ranges:
        if min_val <= num and num <= max_val:
            return True
    return False

valid_tickets = []
for ticket in ticketvals:
    valid_ticket = True
    for value in ticket:
        valid_value = False
        for field in fields:
            if valid_number(value, field['ranges']):
                valid_value = True
                break
        if not valid_value:
            valid_ticket = False
            break
    if (valid_ticket):
        valid_tickets.append(ticket)

for field in fields:
    field['possible_index'] = list(range(len(fields)))
    field['index'] = -1

for ticket in valid_tickets:
    for i in range(len(ticket)):
        value = ticket[i]
        for field in fields:
            if not valid_number(value, field['ranges']):
                if i in field['possible_index']:
                    field['possible_index'].remove(i) 

fields_sorted = sorted(fields, key=lambda x: len(x['possible_index']))
for f in fields_sorted:
    candidates = [x for x in f['possible_index'] if x not in [f['index'] for f in fields]]
    f['index'] = candidates[0]

dep_vals = []

for f in fields:
    if f['field'].startswith('departure'):
        dep_vals.append(my_ticket[f['index']])

print(functools.reduce(lambda a, b: a * b, dep_vals))
