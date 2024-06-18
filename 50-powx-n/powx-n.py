class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        _pow = 1

        if n == 0:
            return 1
        
        if n < 0:
            return pow(1/x, -n)
        
        if n%2 == 0:
            return pow(x*x, n//2)
        
        else:
            return x * pow(x*x, (n-1)//2)