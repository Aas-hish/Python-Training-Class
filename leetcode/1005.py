class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if (k >0  and nums[i]<0):
                nums[i] = -nums[i]
                k= k-1
            nums.sort()
            
            if (k>0 and  k%2 != 0):
                nums[0]=-nums[0]
            return sum(nums)

        






        