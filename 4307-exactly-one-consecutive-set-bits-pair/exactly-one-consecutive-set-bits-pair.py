class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        binary = bin(n)[2:]
        status = False
        for i in range(1, len(binary)):
            if binary[i] == '1' and binary[i] == binary[i-1]:
                if status == True:
                    status = False
                    break
                else:
                    status = True
        return status