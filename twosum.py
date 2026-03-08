class Solution(object):
    def twoSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result=[]
        assert 2 <= len(nums) <= 10**4, "List length must be between 2 and 10,000"
        assert -10**9 <= target <= 10**9
        for i in range(len(nums)):
            for j in range(len(nums)-1):
        #print("all : ",i,nums[i],j+1,nums[j+1])
                if j+1>i:
                    if (nums[i]+nums[j+1]==target):
                        #print("matched : ",i,nums[i],j+1,nums[j+1])
                        result.extend([i,j+1])

        return result
sol=Solution()
nums=[2,7,11,15]
target=9
print(sol.twoSum(nums,target))      