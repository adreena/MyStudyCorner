# time O(N)
# space: O(N)

def removeComments(self, source: List[str]) -> List[str]:
    # // 1 line
    # /* */
    in_block = False
    output = []
    for line in source:
        if not in_block:
            temp_line = []
        i = 0
        while i < len(line):
            ignore = False
            if line[i:i+2] == '/*' and not in_block:
                in_block = True
                i+=1
            elif line[i:i+2] == '*/' and in_block:
                in_block = False
                i+=1
            elif not in_block and line[i:i+2]=='//':
                break
            elif not in_block:
                temp_line.append(line[i])
            i+=1

        if temp_line and not in_block:
            output.append("".join(temp_line))
        # print(line, temp_line, output)
        # print('----')
    return output
