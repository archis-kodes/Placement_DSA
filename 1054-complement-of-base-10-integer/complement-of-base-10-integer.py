class Solution(object):
    def bitwiseComplement(self, n):
        n = bin(n)[2:]
        m = ""
        for i in n:
            if i=='0':
                m = m+'1'
            else:
                m = m+'0'
        return int(m,2)