def make_binary(binary_list,n):
    if n==0:
        return binary_list
    binary_list.append(n%2)
    make_binary(binary_list,n//2)
#bin(n)

n = int(input())
for _ in range(n):
    num = int(input())
    binary_list = []
    make_binary(binary_list,num)
    for idx,n in enumerate(binary_list):
        if n==1:
            print(idx,end=" ")
