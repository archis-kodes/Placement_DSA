class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp = dict()
        s = s.split()

        if len(s) !=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in mp:
                if s[i] not in mp.values():
                    mp[pattern[i]] = s[i]
                else:
                    return False
            else:
                if mp[pattern[i]] != s[i]:
                    return False

        
        return True