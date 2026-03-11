class Solution(object):
    def bitwiseComplement(self, n):
        m=n
        if m==0:
            return 1
        mask =0
        while (m!=0):
            mask = (mask << 1) | 1
            m = m >> 1
        return ~(n) & mask
        