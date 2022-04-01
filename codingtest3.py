def solution(clothes):
    answer = 1
    dic = {}
    for clothe, clothe_type in clothes:
        if clothe_type in dic:
            dic[clothe_type].append(clothe)
        else:
            dic[clothe_type] = [clothe]

    for key in dic.keys():
        answer *= len(dic[key]) + 1

    return answer - 1