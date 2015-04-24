__author__ = 'jakubnarloch'

from math import ceil

def solution(X, Y, D):
    return int(ceil(float(Y - X) / D))

if __name__ == '__main__':
    X = 10
    Y = 85
    D = 30
    print(solution(X, Y, D))
