__author__ = 'jakubnarloch'

def solution(X, A):
    # write your code in Python 2.7
    N = len(A)
    count = [-1] * (X + 1)

    pos = 1
    min_time = -1
    for ind in range(N):
        if A[ind] <= X and count[A[ind]] == -1:
            count[A[ind]] = ind

            if A[ind] == pos:
                while pos <= X and count[pos] != -1:
                    min_time = max(min_time, count[pos])
                    pos += 1

    while pos <= X and count[pos] != -1:
        min_time = max(min_time, count[pos])
        pos += 1

    return min_time if pos > X else -1


if __name__ == '__main__':
    # X = 5
    # A = [1, 3, 1, 4, 2, 3, 5, 4]
    X = 1
    A = [2]
    print(solution(X, A))
