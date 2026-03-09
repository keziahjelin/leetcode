class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        assert 1 <= len(s) <= 10**4 
        count=0
        words=s.split()
        if s.isalpha==False or s.isspace==False:
            print("Invalid")
        for word in words[-1]:
            for letter in word[-1]:
                count+=1
                print("count : ", count, "letter : ", letter, "word : ", word)
        return count
sol=Solution()            
