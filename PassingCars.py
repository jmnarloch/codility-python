__author__ = 'jakubnarloch'

def solution(A):
    # write your code in Python 2.7
    N = len(A)

    cars = 0
    result = 0
    for ind in range(N):
        if A[ind] == 0:
            cars += 1
        else:
            result += cars

            if result > 1E9:
                return -1

    return result

if __name__ == '__main__':
    A = [0, 1, 0, 1, 1]
    print(solution(A))