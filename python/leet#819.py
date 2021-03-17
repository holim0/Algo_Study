class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()

        real = ""

        for i in range(len(paragraph)):
            if paragraph[i].isalpha():
                real += paragraph[i]
            else:
                real += " "

        dict = {}

        para_list = real.split()

        for para in para_list:
            if para not in dict:
                dict[para] = 1

            else:
                dict[para] += 1

        dict = sorted(dict.items(), key=lambda dict: dict[1], reverse=True)

        for key, val in dict:
            if key not in banned:
                return key
