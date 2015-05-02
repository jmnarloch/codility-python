__author__ = 'jakubnarloch'

def solution(A, B, K):
    # write your code in Python 2.7
    result = B // K - A // K
    if A % K == 0:
        result += 1

    return result

if __name__ == '__main__':
    A = 6
    B = 11
    K = 2
    print(solution(A, B, K))
    print(solution(11, 345, 17))
