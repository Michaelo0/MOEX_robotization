from collections import Counter

print(*Counter(input().split(',')).most_common()[0][0])