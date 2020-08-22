
# time: O(N+m)
# space: O(N+M)

from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counts = Counter()
        banned = set(banned)
        start, i = 0, 0
        max_word, max_count = None, 0
        while i < len(paragraph):
            if paragraph[i] in ["!","?","'",";",".", "," , " "]:
                if i!=start:
                    word = paragraph[start:i].lower()
                    if word not in banned:
                        counts[word]+=1
                        if max_word is None:
                            max_count = counts[word]
                            max_word = word
                        elif counts[word]==max_count and word<max_word:
                            max_word = word
                        elif counts[word]>max_count:
                            max_word = word
                            max_count = counts[word]
                            
                start = i+1
            i+=1
        if start!=i:
            word = paragraph[start:i].lower()
            if word not in banned:
                counts[word]+=1
                if max_word is None:
                    max_count = counts[word]
                    max_word = word
                elif counts[word]==max_count and word<max_word:
                    max_word = word
                elif counts[word]>max_count:
                    max_word = word
                    max_count = counts[word]
        return max_word
                

