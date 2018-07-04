no_of_words = int(input())
from collections import Counter,OrderedDict
count_words = Counter()
ordered_word = OrderedDict()
for i in range(no_of_words):
    inp = [input()]
    count_words.update(inp)
    ordered_word[inp[0]]=count_words[inp[0]]
    
print(len(ordered_word))
print(*[v for k,v in ordered_word.items()])
