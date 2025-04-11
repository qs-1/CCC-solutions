import sys
input = sys.stdin.readline
n = int(input())
scores = [int(input()) for _ in range(n)]
bronze = sorted(set(scores))[-3]
print(bronze, scores.count(bronze))