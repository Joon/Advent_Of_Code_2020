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

def valid_number(num, ranges):
    for (min_val, max_val) in ranges:
        if min_val <= num and num <= max_val:
            return True
    return False


invalid_values = []
for ticket in ticketvals:
    for value in ticket:
        valid_value = False
        for field in fields:
            if valid_number(value, field['ranges']):
                valid_value = True
                break
        if not valid_value:
            invalid_values.append(value)


print(sum(invalid_values))