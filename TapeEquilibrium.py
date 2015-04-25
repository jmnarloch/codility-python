__author__ = 'jakubnarloch'

def solution(A):
    # write your code in Python 2.7
    N = len(A)

    sum = 0
    for val in A:
        sum += val

    left = sum - A[N - 1]
    right = A[N - 1]
    diff = abs(right - left)
    for ind in range(N - 2, 0, -1):
        left -= A[ind]
        right += A[ind]

        diff = min(diff, abs(right - left))

    return diff

if __name__ == '__main__':
    A = [3, 1, 2, 4, 3]
    print(solution(A))

