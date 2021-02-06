def solution(numbers, hand):
    answer = ''

    keyPad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]

    leftHand = {'x': 3, 'y': 0}
    rightHand = {'x': 3, 'y': 2}

    for n in numbers:
        if n == 2 or n == 5 or n == 8 or n == 0:
            x = 0
            y = 1
            if n == 2:
                x = 0
                y = 1
            if n == 5:
                x = 1
                y = 1
            if n == 8:
                x = 2
                y = 1
            if n == 0:
                x = 3
                y = 1
            leftDist = abs(x-leftHand['x'])+abs(y-leftHand['y'])
            rightDist = abs(x-rightHand['x'])+abs(y-rightHand['y'])
            if leftDist == rightDist:
                if hand == "right":
                    answer += "R"
                    rightHand['x'] = x
                    rightHand['y'] = y

                else:
                    answer += "L"
                    leftHand['x'] = x
                    leftHand['y'] = y

            else:
                if leftDist < rightDist:
                    answer += "L"
                    leftHand['x'] = x
                    leftHand['y'] = y

                elif leftDist > rightDist:
                    answer += "R"
                    rightHand['x'] = x
                    rightHand['y'] = y

        elif n == 1 or n == 4 or n == 7:
            answer += "L"
            if n == 1:
                leftHand['x'] = 0
                leftHand['y'] = 0
            if n == 4:
                leftHand['x'] = 1
                leftHand['y'] = 0
            if n == 7:
                leftHand['x'] = 2
                leftHand['y'] = 0
        else:
            if n == 3:
                rightHand['x'] = 0
                rightHand['y'] = 2

            if n == 6:
                rightHand['x'] = 1
                rightHand['y'] = 2
            if n == 9:
                rightHand['x'] = 2
                rightHand['y'] = 2
            answer += "R"

    return answer
