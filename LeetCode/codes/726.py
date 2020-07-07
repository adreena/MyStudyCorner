# Time: O(N2) worst case parenthesis might take every chars pop out
# Space: O(N)

from collections import Counter
def countOfAtoms(self, formula: str) -> str:
    stack = []
    i=0
    while i < len(formula):
        if i > 0 and formula[i].isdigit():
            
            # collect all digits
            val = int(formula[i])
            i+=1
            while i < len(formula) and formula[i].isdigit():
                val = val*10 + int(formula[i])
                i+=1
                
            # check for closing parenthesis and the prev value before parenthesis
            if prev==')':
                d = Counter({})
                while len(stack)>0 and stack[-1]!='(':
                    temp = stack.pop()
                    if isinstance(temp, Counter):
                        d += temp
                stack.pop() #pop '('
                for k, v in d.items():
                    d[k]*=val
                stack.append(d)
            else:
                if stack[-1][prev] == 1:
                    stack[-1][prev]=val
                else:
                    stack[-1][prev]*=val

        else:
            if formula[i] == '(' or formula[i]==')':
                prev = formula[i]
                stack.append(formula[i])
                i+=1
            else:
                temp = formula[i]
                i+=1
                
                # collect all lower continuing chars 
                while i < len(formula):
                    if formula[i].isalpha() and formula[i].islower():
                        temp+=formula[i]
                        i+=1
                    else:
                        break
                prev = temp
                stack.append(Counter({temp:1}))

    all_counts = Counter({})
    for c in stack:
        all_counts+=c

    keys = sorted(all_counts.keys())
    output = ''
    for k in keys:
        val = all_counts[k]
        if val > 1:
            output+=k + str(val)
        else:
            output+=k
    return output