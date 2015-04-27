__author__ = 'jakubnarloch'

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    count = [0] * (N)
    for val in A:
        if val < 1 or val > N:
            return 0

        count[val - 1] += 1

    for ind in range(N):
        if count[ind] != 1:
            return 0

    return 1

if __name__ == '__main__':
    A = [4, 1, 3, 2]
    print(solution(A))

