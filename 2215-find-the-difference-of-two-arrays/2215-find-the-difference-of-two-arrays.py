class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer0 = []
        answer1 = []
        i = 0
        j = 0
        for i in range(len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in answer0:
                answer0.append(nums1[i])
            i += 1
        for j in range(len(nums2)):
            if nums2[j] not in nums1 and nums2[j] not in answer1:
                answer1.append(nums2[j])
        
        answer = [answer0, answer1]
        return answer
                