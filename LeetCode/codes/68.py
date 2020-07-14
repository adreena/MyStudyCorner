# time: O(n2)
# space O(n)

def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

    groups = [[]]
    cur_len = 0
    for w in words:
        if cur_len+len(w)>maxWidth:
            groups.append([])
            cur_len = 0
        groups[-1].append(w)
        cur_len += len(w) + 1

    output = []
    for g_idx, g in enumerate(groups):
        if len(g) == 1 or g_idx == len(groups)-1:
            temp = " ".join(g)
            for s in range(maxWidth - len(temp)):
                temp+= " "
            output.append(temp)
        else:
            num_spaces = [0 for i in range(len(g)-1)]
            total_len = 0
            for w in g:
                total_len+=len(w)

            rem = maxWidth-total_len
            space_idx =0
            while rem:
                num_spaces[space_idx]+=1
                space_idx = (space_idx+1)%len(num_spaces)
                rem-=1

            temp = g[0]
            for w, sp in zip(g[1:], num_spaces):
                temp+= ' '*sp + w
            output.append(temp)
    return output
