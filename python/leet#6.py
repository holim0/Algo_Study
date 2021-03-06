class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        zig = [[] for _ in range(numRows)]

        answer = ""

        interval = numRows-2

        gap = interval + numRows

        for i in range(0, len(s), gap):
            for j in range(i, i+numRows):

                if j < len(s):
                    idx = j % gap
                    zig[idx].append(s[j])

            start = i+numRows

            idx = numRows-2
            for j in range(start, i+gap):
                if j < len(s):
                    zig[idx].append(s[j])
                    idx -= 1

        for i in range(numRows):
            for j in zig[i]:
                answer += j

        return answer
