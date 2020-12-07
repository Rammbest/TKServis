import sys
a = sys.argv.copy()
a.pop(0)
print(*a)