from collections import Counter

text = "nlp nlp ai machine learning ai ai"

tokens = text.split()

freq = Counter(tokens)

print(freq.most_common(3))