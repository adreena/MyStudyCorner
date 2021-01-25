# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def get_candidate(words):
            reps = [defaultdict(lambda:0)]*6
            for word in words:
                for i in range(len(word)):
                    reps[i][word[i]]+=1
            max_score = 0
            max_candidate = ''
            for word in words:
                s = 0
                for i in range(len(word)):
                    s+=reps[i][word[i]]
                if s>max_score:
                    max_score = s
                    max_candidate=word
            return max_candidate

        words = wordlist
        while words:
            best = get_candidate(words)
            score = master.guess(best)
            if score == 6:
                return best
            new_words = []
            for word in words:
                s = 0
                for c1, c2 in zip(word, best):
                    if c1 == c2:
                        s+=1
                if s == score:
                    new_words.append(word)
            words = new_words
            # print(words)
        
