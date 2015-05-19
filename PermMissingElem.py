__author__ = 'jakubnarloch'

def solution(A):
    # write your code in Python 2.7
    sum = 0
    N = len(A)
    for val in A:
        sum += val

    expected = (N + 1) * (N + 2) // 2;

    return expected - sum

if __name__ == '__main__':
    A = [2, 3, 1, 5]
    print(solution(A))
