class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        answer = ""

        strs = sorted(strs, key=len)

        arr = list(strs[0])

        for i in range(len(arr)):
            flag = False
            tmp = answer+arr[i]
            for j in range(1, len(strs)):
                cur = strs[j]
                if tmp not in cur[:i+1]:
                    flag = True
                    break

            if flag:
                break

            else:
                answer = tmp

        return answer
