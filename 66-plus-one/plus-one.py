class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]==9 and len(digits)==1:
            return [1, 0]
        elif digits[-1]==9:
            p = self.plusOne(digits[:-1])
            p.append(0)
            return p
        else:
            digits[-1]+=1
            return digits