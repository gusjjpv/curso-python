N = int(input())

for _ in range(N):
    A, B = input().split()
    if A[-len(B):] == B:
        print("encaixa")
    else:
        print("nao encaixa")
