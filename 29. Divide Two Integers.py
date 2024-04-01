import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor==-1 and dividend==-2147483648:
            return 2147483647
        if dividend<0 and divisor<0:
            res=dividend/divisor
            return int(res)
        else:
            res=dividend/divisor
            return int(res)