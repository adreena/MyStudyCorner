class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.current = list(nums)
        self.seed = 0

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.current = self.original[:]
        return self.current

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        temp = list(self.current)
        i = 0
        while temp:
            j = random.randrange(len(temp))
            self.current[i] = temp.pop(j)
            i+=1
        return self.current


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()