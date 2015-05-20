__author__ = 'jakubnarloch'

def solution(S):
    # write your code in Python 2.7
    N = len(S)
    if N == 0:
        return 1

    stack = [None] * N
    size = 0

    parentheses = {'(': ')', '{': '}', '[': ']'}

    for ch in S:
        if ch in parentheses:
            stack[size] = ch
            size += 1
        else:
            if size == 0 or parentheses[stack[size - 1]] != ch:
                return 0
            size -= 1

    return 1 if size == 0 else 0

if __name__ == '__main__':
    print(solution('{[()()]}'))




