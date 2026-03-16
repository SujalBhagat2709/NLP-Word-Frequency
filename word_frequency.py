from collections import Counter

text = "nlp is fun and nlp is powerful"

tokens = text.split()

freq = Counter(tokens)

print(freq)