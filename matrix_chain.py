import sys


def MatrixChainOrder(p, n):
    m = [[0 for x in range(n)] for x in range(n)]
    for i in range(1, n):
        m[i][i] = 0

    for curr in range(2, n):
        for i in range(1, n - curr + 1):
            j = i + curr - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q

    return m[1][n - 1]


if __name__ == '__main__':
    num_of_matrices = int(input("Enter Number of matrices: "))
    idx = 0
    arr = []
    current_matrix = None
    while idx <= num_of_matrices:
        if idx < num_of_matrices:
            current_matrix = int(input("enter n of NxM matrix: "))
        elif idx == num_of_matrices:
            current_matrix = int(input("enter m of last Matrix: "))
        arr.insert(idx, current_matrix)
        idx += 1
    size = len(arr)
    min_num = MatrixChainOrder(arr, size)
    print("Minimum Number of multiplications are:", min_num)
