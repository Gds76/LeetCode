class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        lst1 = []
        lst2 = []
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                lst1.append(nums1[i])
                lst1 = list(set(lst1))
        answer.append(lst1)
        for j in range(len(nums2)):
            if nums2[j] not in nums1:
                lst2.append(nums2[j])
                lst2 = list(set(lst2))
        answer.append(lst2)
        return answer        

        