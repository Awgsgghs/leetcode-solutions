class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for bit in range(32):
            if n&1<<bit:
                if bit==0:
                    res-=1<<32
                else:
                    res|=1<<(31-bit)
        return res
