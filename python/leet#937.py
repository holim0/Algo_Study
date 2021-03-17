class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        digi = []
        letter = []
        for s in logs:
            tmp = s.split(" ")

            if tmp[1].isdigit():
                digi.append(s)
            else:
                letter.append(s)

        new_arr = []
        for l in letter:
            tmp = l.split(" ")

            identifier = tmp[0]

            rest = " ".join(tmp[1:])

            new_arr.append((identifier, rest))

        new_arr = sorted(new_arr, key=lambda x: (x[1], x[0]))

        letter = []

        for val in new_arr:
            tmp = " ".join(val)
            letter.append(tmp)

        return letter+digi
