class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        type_dict = {}

        max_value = len(candyType)//2

        for t in candyType:
            if t not in type_dict:
                type_dict[t] = 0

        type_size = len(type_dict)

        if max_value >= type_size:
            return type_size

        else:
            return max_value
