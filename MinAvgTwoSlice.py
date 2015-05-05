__author__ = 'jakubnarloch'

def solution(A):
    # write your code in Python 2.7
    N = len(A)

    index = 0
    max = (A[0] + A[1]) / 2.0
    for ind in range(N - 1):
        avg2 = (A[ind] + A[ind + 1]) / 2.0

        if avg2 < max:
            max = avg2
            index = ind

        if ind <= N - 3:
            avg3 = (A[ind] + A[ind + 1] + A[ind + 2]) / 3.0

            if avg3 < max:
                max = avg3
                index = ind

    return index

if __name__ == '__main__':
    A = [4, 2, 2, 5, 1, 5, 8]
    print(solution(A))
