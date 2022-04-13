def solution(participant, completion):
    a = 1
    participant.sort()
    completion.sort()
    for idx, peo in enumerate(participant):
        if peo != completion[idx]:
            return peo
