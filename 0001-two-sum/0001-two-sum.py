class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums[i+1:]:
                j = nums.index(diff, i+1)
                break
            else:
                i += 1
        return [i,j]