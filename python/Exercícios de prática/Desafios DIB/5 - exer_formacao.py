T = int(input())

def garrafas(N, K):
  
  trocas = N // K
  sobra = N % K
  num_garrafas = trocas + sobra
    
  return num_garrafas
  
    
for i in range(T):
    
  N, K = map(int, input().split())
  
  print(garrafas(N, K))