class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        hashmap = {}
        for i in range(0,n):
            remaining = target - nums[i]
            if remaining in hashmap:
                return(hashmap[remaining],i)
            else:
                hashmap[nums[i]] = i
