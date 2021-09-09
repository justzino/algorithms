def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    lps = [0] * M

    # Preprocess the pattern
    computeLPS(pat, lps)

    i = 0  # index for txt[]
    j = 0  # index for pat[]
    while i < N:
        # 문자열이 같은 경우 양쪽 인덱스를 모두 증가시킴
        if pat[j] == txt[i]:
            i += 1
            j += 1

        # Pattern 을 찾은 경우
        if j == M:
            print("Found pattern at index " + str(i - j))
            j = lps[j - 1]

        # Pattern 을 찾지 못한 경우
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            # j!=0인 경우는 짧은 lps 에 대해 재검사
            if j != 0:
                j = lps[j - 1]
            # j==0이면 일치하는 부분이 없으므로 인덱스 증가
            else:
                i += 1


def computeLPS(pat, lps):
    length = 0  # length of the previous longest prefix suffix

    # 항상 lps[0]==0이므로 while 문은 i==1부터 시작한다.
    i = 1
    while i < len(pat):
        # 이전 인덱스에서 같았다면 다음 인덱스만 비교하면 된다.
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # 일치하지 않는 경우
            if length != 0:
                # 이전 인덱스에서는 같았으므로 length 을 줄여서 다시 검사
                length = lps[length-1]
                # 다시 검사해야 하므로 i는 증가하지 않음
            else:
                # 이전 인덱스에서도 같지 않았다면 lps[i]는 0 이고 i는 1 증가
                lps[i] = 0
                i += 1


# 예시
# txt = "ABABDABACDABABCABAB"
# pat = "ABABCABAB"
# 다른 예시
txt = 'ABXABABXAB'
pat = 'ABXAB'
KMPSearch(pat, txt)
