import sys
n = int(sys.stdin.readline())
conf = []
for i in range(n):
    conf.append(list(map(int, sys.stdin.readline().split())))
conf = sorted(conf, key=lambda x: x[0])
conf = sorted(conf, key=lambda x: x[1])

count = 0
before = 0
for s, e in conf:
    if s >= before:
        count+=1
        before = e

print(count, end="")

