class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        array = [0]*(len(s))
        shift = sum(shifts)
        for i in range(len(s)):
            array[i] = chr((ord(s[i]) - ord('a') +shift)%26 + ord('a'))
            shift = shift - shifts[i]
        return "".join(array)