class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        1 <= len(s) <= 2 * 10**5
        l=list(s)
        new=[]
        
        print(l)
        for x in l:
            if x.isalnum():
                lc=x.lower()
                new.append(lc)
        print(new)
        lenn=len(new)
        print(lenn)
        for i in range(lenn//2):
            if new[i]!=new[lenn-1-i]:
                return False
        return True  
