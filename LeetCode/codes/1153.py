# time: O(1)
# space: O(1)

from collections import defaultdict
def canConvert(self, str1: str, str2: str) -> bool:
    if str1 == str2 :
        return True
    mapping = defaultdict(lambda:None)
    for c1, c2 in zip(str1, str2):
        if c1 not in mapping:
            mapping[c1] = c2
        else:
            if mapping[c1] != c2:
                return False
    return len(set(str2))< 26
