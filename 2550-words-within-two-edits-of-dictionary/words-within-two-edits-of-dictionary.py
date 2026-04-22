class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        for query in queries:
            for word in dictionary:
                changePermit = 2
                for i in range(len(word)):
                    if word[i] != query[i]:
                        changePermit -=1
                        if changePermit < 0:
                            break
                if changePermit >= 0:
                    result.append(query)
                    break
        return result