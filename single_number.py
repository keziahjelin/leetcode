class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        1 <= len(nums) <= 3 * 10**4
        count=0
        numss={}
        res=0
        for k in nums:
            res ^=k
        return res
