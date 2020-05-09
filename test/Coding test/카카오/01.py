def trans(n):
    if n == 0:
        return [3,1]
    i = (n-1)//3
    j = n - 1 - 3*i
    return [i,j]

def solution(numbers, hand):
    answer = ''
    left = [3, 0]
    right = [3, 2]
    left_side = [1,4,7]
    right_side = [3,6,9]
    for num in numbers:
        if num in left_side:
            answer += 'L'
            left = trans(num)
        elif num in right_side:
            answer += 'R'
            right = trans(num)
        else:
            pos = trans(num)
            l_d = abs(pos[0] - left[0]) + abs(pos[1] - left[1])
            r_d = abs(pos[0] - right[0]) + abs(pos[1] - right[1])
            if l_d == r_d:
                if hand == 'left':
                    answer += 'L'
                    left = pos
                else:
                    answer += 'R'
                    right = pos
            elif l_d < r_d:
                answer += 'L'
                left = pos
            else:
                answer += 'R'
                right = pos
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))