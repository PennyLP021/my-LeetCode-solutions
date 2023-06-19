class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer0, answer1 = [], []
        i = 0
        j = 0
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                answer0.append(nums1[i])
            i += 1
        for j in range(len(nums2)):
            if nums2[j] not in nums1:
                answer1.append(nums2[j])
        
        answer = [set(answer0), set(answer1)]
        return answer
                