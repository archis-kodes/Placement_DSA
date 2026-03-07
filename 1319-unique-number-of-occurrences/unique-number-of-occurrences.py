class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mp = dict()
        for i in arr:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i] += 1
        c = set()
        for element, count in mp.items():
            if count in c:
                return False
            else:
                c.add(count)
        return True
