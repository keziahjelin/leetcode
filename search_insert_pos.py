class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        assert 1 <= len(nums) <= 10**4 
#nums contains distinct values sorted in ascending order.
        assert -10**4 <= target <= 10**4
        nums.sort()
        length=len(nums)
        for i in range(length):
            if target<=nums[i]:
                print(i)
                return i 
        return length   
