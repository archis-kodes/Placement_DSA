class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        array = [0] * (len(s)+1)
        for start, end, direction in shifts:
            if direction == 0:
                array[start] += -1
                array[end+1] += 1
            else:
                array[start] += 1
                array[end+1] += -1

        array.pop()

        cumSum = 0
        for i in range(len(array)):
            cumSum += array[i]
            array[i] = chr((ord(s[i]) - ord('a') + cumSum)%26 +ord('a'))
        return "".join(array)