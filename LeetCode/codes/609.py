# time O(N)
# space O(N)
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = defaultdict(lambda:[])
        for path in paths:
            info = path.split(' ')
            d = info[0]
            files = info[1:]
            
            for file in files:
                content = ""
                name=''
                i = 0
                while i <len(file) and file[i]!='(':
                    name+=file[i]
                    i+=1
                content = file[i+1:-1]
                contents[content].append(f"{d}/{name}")
        # print(contents)
        output = [val for key, val in contents.items() if len(val)>1]
        return output