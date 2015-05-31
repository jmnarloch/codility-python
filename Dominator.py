__author__ = 'jakubnarloch'

def solution(A):
    # write your code in Python 2.7

    N = len(A)

    if N == 0:
        return -1
    elif N == 1:
        return 0

    candidate = A[0]
    occur = 1
    for ind in range(1, N):
        if A[ind] == candidate:
            occur += 1
        else:
            occur -= 1

        if occur == 0:
            candidate = A[ind]
            occur = 1

    leader = candidate
    count = 0
    index = -1
    for ind in range(N):
        if leader == A[ind]:
            if index == -1:
                index = ind
            count += 1

    if count < (N // 2) + 1:
        return -1

    return index

if __name__ == '__main__':
    A = [3, 4, 3, 2, 3, -1, 3, 3]
    print(solution(A))
