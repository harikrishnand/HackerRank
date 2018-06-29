inp = input()
import itertools

print(*[(len(list(ls)),int(k)) for k,ls in itertools.groupby(inp, key = lambda x: x)], sep = ' ')
