# time O(log(m+n))
# space: O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m>n:
            nums1, nums2 = nums2, nums1
            n, m = m, n
        left = 0
        right = m
        while left<=right:
            mid1 = (left+right+1) //2
            mid2 = (m+n+1)//2 - mid1
            
            leftMax1, leftMax2 = float('-inf'), float('-inf')
            rightMin1, rightMin2 = float('inf'), float('inf')
            if mid1>0:
                leftMax1 = nums1[mid1-1]
            if mid2>0:
                leftMax2 = nums2[mid2-1]
            if mid1<m:
                rightMin1 = nums1[mid1]
            if mid2<n:
                rightMin2 = nums2[mid2]
            
            if leftMax1<=rightMin2 and leftMax2<=rightMin1:
                if (n+m) % 2 == 0:
                    return (max(leftMax1, leftMax2)  + min(rightMin1, rightMin2)) /2
                return max(leftMax1, leftMax2)
            if leftMax1>rightMin2:
                right = mid1-1
            else:
                left = mid1+1
                
        