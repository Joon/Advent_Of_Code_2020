def calc_sum(pieces):
    running_tot = 0
    current_op = None
    for p in pieces:
        if p == '+' or p == '*':
            current_op = p
        else:
            if type(p) is list:
                current_val = calc_sum(p)
            else:
                current_val = int(''.join(filter(str.isdigit, p)))
            if (current_op == None):
                running_tot = current_val
            else:
                if current_op == '+':
                    running_tot = running_tot + current_val
                else:
                    running_tot = running_tot * current_val
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
    

sums = [l for l in open("Inputs/Day18.txt", "r")]
total = 0
for sum in sums:
    total = total + parse_sum(sum)
print(total)