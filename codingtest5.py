def solution(numbers):
    if any(numbers)==False:
        return '0'
    b=list(map(str,numbers))
    b.sort(key=lambda x: x*3 , reverse=True)
    return ''.join(b)
