# time O(n2k)
# space (nk)

class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        self.max_vac = float('-inf')
        self.memo = defaultdict(lambda: float('-inf'))
        self.cities = len(flights)
        self.final_week = len(days[0])
        
        def backtrack(cur_city, cur_week):
            if cur_week == self.final_week:
                return 0
            if self.memo[(cur_city, cur_week)] != float('-inf'):
                return self.memo[(cur_city, cur_week)]
            cur_vac = 0
            for city in range(self.cities):
                if cur_city == city or flights[cur_city][city]:
                    temp = backtrack(city, cur_week+1)+days[city][cur_week]
                    cur_vac = max(cur_vac, temp)
            self.memo[(cur_city, cur_week)] = cur_vac
            return self.memo[(cur_city, cur_week)]
        return backtrack(0,0)
        