__author__ = 'jakubnarloch'

def solution(S, P, Q):
    # write your code in Python 2.7
    N = len(S)
    M = min(len(P), len(Q))
    occurrences = [[-1 for j in range(4)] for i in range(N + 1)]

    genoms = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

    for ind in range(1, N + 1):
        for j in range(4):
            occurrences[ind][j] = occurrences[ind - 1][j]

        occurrences[ind][genoms[S[ind - 1]]] = ind - 1

    result = [0] * M
    for ind in range(M):
        for j in range(4):
            if occurrences[Q[ind] + 1][j] >= P[ind]:
                result[ind] = j + 1
                break

    return result

if __name__ == '__main__':
    S = 'CAGCCTA'
    P = [2, 5, 0]
    Q = [4, 5, 6]
    print(solution(S, P, Q))
