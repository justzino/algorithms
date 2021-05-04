# 2차원 리스트 90도 회전하기
def rotate_a_matrix_by_90_degree(matrix):
    n = len(matrix)      # 행 길이 계산
    m = len(matrix[0])   # 열 길이 계산
    result = [[0] * n for _ in range(m)]    # 결과 리스트

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = matrix[i][j]

    return result
