import re


class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        if len(s) == 0:
            return 0

        lower_bound = (-1) * 2**31
        upper_bound = 2**31 - 1

        s = re.match("[+-]?\d+", s)

        if s:
            answer = int(s.group())

        else:
            return 0

        if answer < lower_bound:
            answer = lower_bound

        if answer > upper_bound:
            answer = upper_bound

        return answer
