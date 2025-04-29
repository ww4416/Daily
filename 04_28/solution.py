"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""


class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = 0
        numslen = len(nums)
        while index1 < numslen:
            index2 = len(nums)-1
            while index2 > 0: 
                if nums[index1] + nums[index2] == target:
                    return [index1, index2]
                index2 = index2 - 1
            index1 = index1 + 1


nums = [2,7,11,15]
res = Solution.twoSum(nums, 9)
print(res)