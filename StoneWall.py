__author__ = 'jakubnarloch'

def solution(H):
    # write your code in Python 2.7
    N = len(H)

    stack = [None] * N
    size = 0

    blocks = 0
    for ind in range(N):

        while size > 0 and H[ind] < stack[size - 1]:
            size -= 1

        if size == 0 or H[ind] != stack[size - 1]:
            blocks += 1
            stack[size] = H[ind]
            size += 1

    return blocks

if __name__ == '__main__':
    H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
    print(solution(H))