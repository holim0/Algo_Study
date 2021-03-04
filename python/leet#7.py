class Solution:
    def reverse(self, x: int) -> int:

        to_String = ""
        isMinus = False

        low = -2**31
        high = 2**31-1

        if x < 0:
            x = -x
            isMinus = True

        to_String = str(x)

        to_String = to_String[::-1]

        if isMinus:
            answer = (-1) * int(to_String)
            if low <= answer <= high:
                return answer

            else:
                return 0

        if low <= int(to_String) <= high:
            return int(to_String)
        else:
            return 0
