
import random

text = "I love python programming. I love machine learning."

words = text.lower().replace(".", "").split()

bigrams = {}

for i in range(len(words) - 1):
    first = words[i]
    second = words[i + 1]

    if first not in bigrams:
        bigrams[first] = []

    bigrams[first].append(second)

word = "i"
result = [word]

for i in range(10):
    if word in bigrams:
        word = random.choice(bigrams[word])
        result.append(word)
    else:
        break

print("Generated Text:")
print(" ".join(result))
