class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for index, num in enumerate(nums):
            for index2, num2 in enumerate(nums):
                if index2 <= index:
                    continue
                else:
                    if num + num2 == target:
                        return [index, index2]




nums = [2,7,11,15]
res = Solution.twoSum(nums, 9)
print(res)