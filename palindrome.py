class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        assert -2**31 <= x <= 2**31 - 1
        element=list(str(x))
        n=len(element)
        for i in range(n//2):
            if element[i]!=element[n-1-i]:
                return False
        return True            
                #print(j)           
sol=Solution()
