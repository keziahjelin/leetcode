class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        assert 1 <= n <= 45
        count=0
        a,b=1,2
        for i in range(n-1):
            a,b=b,a+b
            print("a= ", a, "b= ", b)
        return a
