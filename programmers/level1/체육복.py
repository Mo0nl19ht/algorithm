# set.discard(target) 사용하면 해당 값 없어도 오류 안난다
def solution(n, lost, reserve):
    answer = 0
    n_lost = (set(lost)-set(reserve))
    n_reserve = (set(reserve)-set(lost))
    for l in n_lost:
        try:
            n_reserve.remove(l-1)
            answer += 1
        except:
            try:
                n_reserve.remove(l+1)
                answer += 1
            except:
                continue
    return n-len(n_lost)+answer
