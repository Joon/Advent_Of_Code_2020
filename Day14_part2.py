rows = []

f = open("Inputs/Day14.txt", "r")
mask = ''
for x in f:
    parts = x.rstrip().split(' = ')
    
    if (parts[0] == 'mask'):
        mask = parts[1]
    else:
        new_row = {'mask': mask, 'mem_addr': int(''.join(filter(str.isdigit, parts[0]))), 'init_value': int(parts[1])}
        rows.append(new_row)

#def apply_mask(number, mask):
#    bit_string = '{0:b}'.format(number)
#    result_bitstr = ''
#    for i in range(len(bit_string)):
#        index = (len(bit_string) - i) - 1
#        mask_index = (len(mask) - i) - 1
#        # We've run out of bits, just apply const mask values now
#        if mask[mask_index] == 'X':
#            result_bitstr = 'X' + result_bitstr
#        elif(mask[mask_index] == '1'):
#            result_bitstr = '1' + result_bitstr
#        else:
#            result_bitstr = bit_string[index] + result_bitstr
#    return result_bitstr

def apply_mask(number, mask):
    bit_string = '{0:b}'.format(number)
    result_bitstr = ''
    for i in range(len(mask)):
        index = (len(bit_string) - i) - 1
        mask_index = (len(mask) - i) - 1
        # We've run out of bits, just apply mask values now
        if (index < 0):
            if mask[mask_index] == 'X':
                result_bitstr = 'X' + result_bitstr
            elif(mask[mask_index] == '1'):
                result_bitstr = '1' + result_bitstr
            else:
                result_bitstr = '0' + result_bitstr
        else:
            if mask[mask_index] == 'X':
                result_bitstr = 'X' + result_bitstr
            elif(mask[mask_index] == '1'):
                result_bitstr = '1' + result_bitstr
            else:
                result_bitstr = bit_string[index] + result_bitstr
    return result_bitstr



def calc_mask_float(mask):
    resulting_numbers = []
    stack = []
    stack.append(mask)
    while len(stack) > 0:
        proto = stack.pop()
        if 'X' in proto:
            # Floating bits remain - calc the first one found
            i = proto.index('X')
            stack.append(proto[:i] + '1' + proto[i+1:])
            stack.append(proto[:i] + '0' + proto[i+1:])
        else:
            resulting_numbers.append(int(proto, 2))
    return resulting_numbers

registers = {}

for r in rows:    
    r['address_mask'] = apply_mask(r['mem_addr'], r['mask'])
    overwrite_addresses = calc_mask_float(r['address_mask'])
    for add in overwrite_addresses:
        registers[add] = r['init_value']
    
print(sum(registers.values()))
