class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        size = len(nums)

        dict = {}

        for i in range(size+1):
            if i not in dict:
                dict[i] = False

        for n in nums:
            dict[n] = True

        for k, v in dict.items():

            if v == False:
                return k
