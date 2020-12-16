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

def apply_mask(number, mask):
    bit_string = '{0:b}'.format(number)
    result_bitstr = ''
    for i in range(len(mask)):
        index = (len(bit_string) - i) - 1
        mask_index = (len(mask) - i) - 1
        # We've run out of bits, just apply const mask values now
        if (index < 0):
            if mask[mask_index] == '1':
                result_bitstr = '1' + result_bitstr
            else:
                result_bitstr = '0' + result_bitstr
        else:
            if mask[mask_index] == '1':
                result_bitstr = '1' + result_bitstr
            elif mask[mask_index] == '0':
                result_bitstr = '0' + result_bitstr
            else:
                result_bitstr = bit_string[index] + result_bitstr
    return (bit_string, result_bitstr, int(result_bitstr, 2))

registers = {}

for r in rows:
    startv, valm, vali = apply_mask(r['init_value'], r['mask'])
    r['value'] = vali
    r['init_bits'] = startv
    r['result_bits'] = valm
    registers[r['mem_addr']] = r['value']

print(sum(registers.values()))
