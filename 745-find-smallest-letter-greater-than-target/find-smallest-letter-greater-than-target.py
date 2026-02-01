class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        diff = 26
        for letter in letters:
            n = ord(letter) - ord(target)
            if n > 0:
                diff = min(diff, n)
        if diff == 26:
            return letters[0]
        return chr(ord(target)+diff)