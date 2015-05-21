__author__ = 'jakubnarloch'

def solution(S):
    # write your code in Python 2.7
    N = len(S)
    if N == 0:
        return 1

    nest = 0
    for ch in S:
        if ch == '(':
            nest += 1
        else:
            nest -= 1

        if nest < 0:
            return 0

    return 1 if nest == 0 else 0

if __name__ == '__main__':
    solution('')