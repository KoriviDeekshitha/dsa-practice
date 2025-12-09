class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = { }
        for i, num in enumerate(nums):
            remain = target - num
            if remain in seen:
                return [seen[remain], i]
            seen[num] = i
