
# time: O(1)
# space: O(1)

def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        total = (D-B)*(C-A) + (H-F)*(G-E)
        if E>=C or A>=G or F>=D or B>=H:
            return total
        overlap_w = min(C-A, C-E, G-E, G-A)
        overlap_h = min(D-F, D-B, H-B, H-F)
        return total - overlap_w*overlap_h