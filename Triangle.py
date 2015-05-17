__author__ = 'jakubnarloch'


def solution(A):
    # write your code in Python 2.7
    N = len(A)

    A.sort()

    for ind in range(2, N):
        if (A[ind - 2] + A[ind - 1] > A[ind]
            and A[ind - 2] + A[ind] > A[ind - 1]
            and A[ind - 1] + A[ind] > A[ind - 2]):
            return 1

    return 0


if __name__ == '__main__':
    A = [10, 2, 5, 1, 8, 20]
    print(solution(A))