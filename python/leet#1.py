class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        size = len(nums)
        answer = []
        for i in range(size):
            for j in range(i+1, size):
                if nums[i] + nums[j] == target:
                    answer.append(i)
                    answer.append(j)
                    return answer
