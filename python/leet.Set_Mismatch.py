class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        size = len(nums)

        answer = []

        cnt = {}

        for n in nums:

            if n not in cnt:
                cnt[n] = 1
            else:
                cnt[n] += 1

        for k, v in cnt.items():
            if v > 1:
                answer.append(k)
                break

        for i in range(1, size+1):

            if i not in nums:
                answer.append(i)
                break

        return answer
