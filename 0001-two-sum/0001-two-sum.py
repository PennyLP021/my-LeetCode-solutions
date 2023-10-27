class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # index : value
    
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        
    

# better solution using HashMap:
# prevMap = {} # index : value
# for i,n in enumerate(nums):
#   diff = target - n
#   if diff in prevMap:
#       return [prevMap[diff], i]
#   prevMap[i] = n
# return
# hope this works
