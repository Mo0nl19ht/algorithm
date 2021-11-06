def solution(rows, columns):
    ans = [[0 for i in range(columns)] for k in range(rows)]
    chk = [[0 for i in range(columns)] for k in range(rows)]
    num = 1
    r = 0
    c = 0
    chk_zero = 0
    all = rows*columns
    while chk_zero < all:
        ans[r][c] = num
        if chk[r][c] == 0:
            chk_zero += 1
            chk[r][c] = 1
        if num % 2 == 0:
            r += 1
            if r == rows:
                r = 0
        else:
            c += 1
            if c == columns:
                c = 0
        num += 1
        if r == 0 and c == 0 and num % 2 != 0:
            break
    return ans
