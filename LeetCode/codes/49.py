# time : O(Nlogs)
# space: O(N)


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(lambda:list())
        for str in strs:
            key = ''.join(sorted(list(str)))
            groups[key].append(str)
        return groups.values()