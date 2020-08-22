# time : O(1)
# space: O(N)

import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.data_idx = defaultdict(lambda:-1)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.data_idx:
            self.data_idx[val] = len(self.data)
            self.data.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data:
            to_remove_id = self.data_idx[val]
            last_id = self.data_idx[self.data[-1]]
            self.data[to_remove_id] = self.data[last_id]
            self.data_idx[self.data[-1]] = to_remove_id
            del self.data_idx[val]
            self.data.pop()
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()