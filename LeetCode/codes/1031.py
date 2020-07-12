# time O(N)
# Space: O(1)

def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
    for i in range(1, len(A)):
        A[i]+=A[i-1]

    l_max = A[L-1]
    m_max = A[M-1]
    total = A[L+M-1]
    # L -- M
    for i in range(L+M, len(A)):
        l_max = max(l_max, A[i-M]-A[i-M-L])
        total = max(total, l_max + A[i]-A[i-M])
    for i in range(L+M, len(A)):
        m_max = max(m_max, A[i-L]-A[i-M-L])
        total = max(total, m_max+A[i]-A[i-L])

    return total