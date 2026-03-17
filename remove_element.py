class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        assert 0 <= len(nums)<= 100
        assert 0 <= val <= 100
        count=0
        i=0
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
                count+=1
        return count
        return nums
