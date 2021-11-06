def solution(log):
    h = 0
    m = 0
    for i in range(0, len(log), 2):
        st = log[i].split(":")
        en = log[i+1].split(":")
        st_h, st_m = int(st[0]), int(st[1])
        en_h, en_m = int(en[0]), int(en[1])

        if en_h > st_h and en_m < st_m:
            en_h -= 1
            en_m += 60

        if en_h-st_h <= 0 and en_m-st_m < 5:
            continue
        elif en_h-st_h >= 2 or (en_h-st_h >= 1 and en_m-st_m >= 45):
            h += 1
            m += 45
        else:
            h += en_h-st_h
            m += en_m-st_m
    m_h = m//60
    m_m = m-m//60*60
    h += m_h
    ans = []
    if (h < 10):
        ans.append(f"0{h}")
    else:
        ans.append(f"{h}")
    if (m_m < 10):
        ans.append(f"0{m_m}")
    else:
        ans.append(f"{m_m}")
    return ":".join(ans)
