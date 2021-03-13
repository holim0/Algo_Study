import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        if "." in p or "*" in p:

            answer = re.match(p, s)

            if answer:
                if answer.group() == s:
                    return True

                else:
                    return False

            else:
                return False

        else:
            if s == p:
                return True

            else:
                return False
