# time: O(NM) M replacements, N characters
# space: O(N)

def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
    S = list(S)
    for idx, src, trg in sorted(zip(indexes, sources, targets), reverse=True):
        if S[idx:idx+len(src)] == list(src):
            S[idx:idx+len(src)] = list(trg)
    return ''.join(S)
