__author__ = 'jakubnarloch'

def solution(N, A):
    # write your code in Python 2.7

    M = len(A)
    counters = [0] * N

    max_result = max_counter = 0
    for ind in range(M):
        if A[ind] == N + 1:
            max_result = max(max_result, max_counter)
        else:
            if counters[A[ind] - 1] < max_result:
                counters[A[ind] - 1] = max_result

            counters[A[ind] - 1] += 1
            max_counter = max(max_counter, counters[A[ind] - 1])

    for ind in range(N):
        counters[ind] = max(max_result, counters[ind])

    return counters

if __name__ == '__main__':
    N = 5
    A = [3, 4, 4, 6, 1, 4, 4]
    print(solution(N, A))