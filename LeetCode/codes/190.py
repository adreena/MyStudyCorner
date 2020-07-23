# time: O(1)
# space: O(1)

def reverseBits(self, n: int) -> int:
    result = 0 
    mask = 1
    for i in range(32):
        result<<=1
        result|=n &mask
        n>>=1
    return result