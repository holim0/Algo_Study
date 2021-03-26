class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [nums[0]]
        rev = [nums[-1]]

        for i in range(1, len(nums)):
            pre.append(pre[-1] * nums[i])

        reversed_nums = nums[::-1]

        for i in range(1, len(reversed_nums)):
            rev.append(rev[-1] * reversed_nums[i])

        answer = []
        rev = rev[::-1]
        for i in range(len(nums)):
            if i == 0:
                value = rev[i+1]
                answer.append(value)
            elif i == len(nums)-1:
                answer.append(pre[i-1])
            else:
                value = rev[i+1] * pre[i-1]
                answer.append(value)

        return answer
