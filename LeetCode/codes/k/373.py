# time: O(nm)
# space: O(nm +k)

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        n, m = len(nums1), len(nums2)
        if n==0 or m == 0:
            return []
        pairs = [(nums1[0]+nums2[0],0,0)]
        visited = set()
        output = []
        while pairs and len(output)<k:
            _, i, j  = heapq.heappop(pairs)
            output.append((nums1[i],nums2[j]))
            if i+1<n and (i+1,j) not in visited:
                x = nums1[i+1]+nums2[j]
                heapq.heappush(pairs,(x,i+1,j))
                visited.add((i+1,j))
            if j+1<m and (i,j+1) not in visited:
                x = nums1[i]+nums2[j+1]
                heapq.heappush(pairs,(x,i,j+1))
                visited.add((i,j+1))
        return output
