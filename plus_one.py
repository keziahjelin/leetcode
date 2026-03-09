class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        assert 1 <= len(digits) <= 100
        ad=""
        for i in digits:
            ad=ad+str(i)
        #print(ad)
        adnew=str(int(ad)+1)
        #print(adnew)
        ls=[int(i)for i in adnew]
        return ls
        #ls = []
        #for i in adnew:
        #num = int(i)
        #ls.append(num)    
sol=Solution()       