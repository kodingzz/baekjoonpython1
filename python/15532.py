'''
import sys
t=int(sys.stdin.readline())
for i in range(t):
    a,b=sys.stdin.readline().split()
    print(int(a)+int(b))
'''
import sys

io = sys.stdin.read().split('\n')
n = int(io[0])
del io[0]

for i in range(n):
  a, b = io[i].split()
  io[i] = (f"{int(a) + int(b)}\n")

sys.stdout.write(''.join(io))