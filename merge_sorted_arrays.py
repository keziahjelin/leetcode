class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        assert len(nums1) == m + n
        assert len(nums2) == n
        assert 0 <= m, n <= 200
        assert 1 <= m + n <= 200
        
        for i in range(n):
            nums1.pop(-1)
            print(nums1)
        nums1.extend(nums2)
        nums1.sort()
