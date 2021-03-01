class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        dict = {}

        for i in list(s):
            if i not in dict:
                dict[i] = False

        s = list(s)

        start, end = 0, 0

        answer = 0
        cnt = 0
        while True:

            endVal = s[end]
            if not dict[endVal]:

                answer = max(answer, end-start+1)
                dict[endVal] = True
                end += 1

            else:
                dict[s[start]] = False
                start += 1

            if end >= len(s):
                break

        return answer
