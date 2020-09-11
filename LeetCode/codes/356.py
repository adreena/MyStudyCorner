# time O(NlogM)
# space O(NM)
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        X = defaultdict(lambda:[])
        for x, y in points:
            X[y].append(x)

        for key, val in X.items():
            val.sort()

        Y= None
        for items in X.values():
            for i in range(len(items) //2 + 1):
                a = items[i]
                b = items[len(items)-i-1]
                cur = float(a+b)/2
                if not Y:
                    Y = cur
                elif Y!=cur:
                    return False
        return True
