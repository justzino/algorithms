n = int(input())

n_500, m_500 = divmod(n, 500)
n_100m, m_100 = divmod(m_500, 100)
n_50, m_50 = divmod(m_100, 50)
n_10, m_10 = divmod(m_50, 10)

print(n_500 + n_100m + n_50 + n_10)
