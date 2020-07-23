# time: O(logn)
#space: O(1)

def trailingZeroes(self, n: int) -> int:
    zero_count = 0
    temp = n
    while n >0:
        n//=5
        zero_count+=n
    return zero_count