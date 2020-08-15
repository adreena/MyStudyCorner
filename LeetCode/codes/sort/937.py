# time: O(nlogn)
# space: O(1)

class Solution:  
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def my_sort(log):
            id, rest = log.split(' ',1)
            if rest[0].isalpha():
                return (-1, rest, id)
            return (1,)
        
        logs.sort(key=lambda x: my_sort(x))
        return logs