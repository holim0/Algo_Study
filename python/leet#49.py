class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict = {}

        answer = []
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in dict:
                dict[sorted_s] = [s, ]

            else:
                dict[sorted_s].append(s)

        for value in dict.values():
            answer.append(value)

        return answer
