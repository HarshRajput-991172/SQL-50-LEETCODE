class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        n = len(nums)
        nums.sort()
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements for i

            j, k = i + 1, n - 1
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                if total_sum < 0:
                    j += 1
                elif total_sum > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # Skip duplicates for j and k
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans