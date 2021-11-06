def solution(time, plans):
    time = 3.5
    plans = [["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"]]
    name = ""
    for p in plans:
        cost = 0
        st = p[1]
        en = p[2]
        if st[-2] == 'P':
            st = int(st.split(st[-2])[0])
            st += 12
        else:
            st = int(st.split(st[-2])[0])
        if en[-2] == 'P':
            en = int(en.split(en[-2])[0])
            en += 12
        else:
            en = int(en.split(en[-2])[0])

        if st <= 9.5:
            cost = 8.5
        elif st > 9.5 and st < 18:
            cost = 18-st

        if en > 13 and en <= 18:
            cost += en-13
        elif en > 18:
            cost += 5

        time -= cost
        if time > 0:
            name = p[0]
    return name
