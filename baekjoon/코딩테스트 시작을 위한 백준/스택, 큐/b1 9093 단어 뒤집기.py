import dis
def make_reverse(sentence):
    ans = []
    arr = sentence.split(" ")
    for s in arr:
        ans.append("".join((reversed(s))))
    return ans

# 400ms정도 걸린다
def why_400():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input())
    for sentence in arr:
        print(*make_reverse(sentence))


# 신기하다 한번 포문 돌리고 그 안에서 해결하는게 더 빠를거라 생각했는데
# 이게 2배정도 느리다
# 800ms가 걸리는데 왜일까?
def why_800():
    n = int(input())
    arr = []
    for _ in range(n):
        print(*make_reverse(input()))

print("400")
bytecode = dis.Bytecode(why_400)
for instr in bytecode:
    print(instr.opname)

print("800짜리")

bytecode = dis.Bytecode(why_800)
for instr in bytecode:
    print(instr.opname)