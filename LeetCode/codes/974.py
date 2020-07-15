# time O(N)
# space O(N)
# if there are 2 sums % k equal to M , subtract of them % k ==0
# need to sum combination of prefix_sums 

from collections import Counter
def subarraysDivByK(self, A: List[int], K: int) -> int:
    prefix_sum = [0]
    for a in A:
        prefix_sum.append((prefix_sum[-1]+a) %K)
    counter = Counter(prefix_sum)
    return sum(v*(v-1)//2 for v in counter.values())
