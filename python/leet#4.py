class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merge = nums1 + nums2

        merge.sort()

        answer = 0

        if len(merge) % 2 == 0:

            idx = len(merge)//2

            answer = (merge[idx-1]+merge[idx])/2

        else:
            idx = len(merge)//2
            answer = merge[idx]
        return answer
