def calc_sum(pieces):
    running_tot = 0
    current_op = None
    # first pass - resolve brackets
    resolve_pieces = []
    for p in pieces:
        if type(p) is list:
            resolve_pieces.append(calc_sum(p))
        else:
            if p == '+' or p == '*':
                resolve_pieces.append(p)
            else:
                resolve_pieces.append(int(''.join(filter(str.isdigit, p))))
    
    last_val = None
    op = None
    while '+' in resolve_pieces:
        process_pieces = []
        first_plus = resolve_pieces.index('+')
        for i in range(first_plus - 1):
            process_pieces.append(resolve_pieces[i])
        process_pieces.append(resolve_pieces[first_plus - 1] + resolve_pieces[first_plus + 1])
        for i in range(first_plus + 2, len(resolve_pieces)):
            process_pieces.append(resolve_pieces[i])
        resolve_pieces = process_pieces

    # Final step: resolve multiplication
    running_tot = None
    for p in resolve_pieces:
        if p == '*':
            op = p
        else:
            val = p
            if running_tot == None:
                running_tot = val
            else:
                running_tot = running_tot * val
    return running_tot



def parse_sum(str):    
    pieces = list(parse_parens(str.split(' ')))
    return calc_sum(pieces)
    
        
def parse_parens(str_pieces):
    result = []
    if (str_pieces == None):
        return []
    i = 0
    while i < len(str_pieces):
        if '(' in str_pieces[i]:
            # find closing paren
            # Special case: two opening parens in one string
            paren_count = str_pieces[i].count('(') 
            end_index = -1
            for j in range(i + 1, len(str_pieces)):
                if '(' in str_pieces[j]:
                    # Special case: two opening parens in one string
                    paren_count += str_pieces[j].count('(')                    
                if ')' in str_pieces[j]:
                    # Special case: two closing parens in one string
                    paren_count -= str_pieces[j].count(')')
                if (paren_count <= 0):
                    end_index = j
                    break
            if (end_index == -1):
                raise Exception("Unterminated parenthesis")
            # Chop off one opening paren
            recurse_to = [str_pieces[i][1:]]
            recurse_to.extend(str_pieces[i + 1:end_index])
            # chop off one closing paren
            recurse_to.append(str_pieces[end_index][:-1])
            result.append(parse_parens(recurse_to))
            i = j
        else:
            result.append(str_pieces[i])
        i += 1
    return result


sums = [l.strip() for l in open("Inputs/Day18.txt", "r")]
total = 0
for sum in sums:
    total = total + parse_sum(sum)
print(total)