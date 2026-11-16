
import nltk
from nltk.probability import ConditionalFreqDist

sentences = [
    [("I", "PRP"), ("love", "VB"), ("Python", "NN")],
    [("He", "PRP"), ("likes", "VB"), ("cricket", "NN")],
    [("She", "PRP"), ("plays", "VB"), ("football", "NN")]
]

cfd = ConditionalFreqDist()

for sentence in sentences:
    for word, tag in sentence:
        cfd[word.lower()][tag] += 1

words = ["I", "love", "Python"]

print("Stochastic POS Tagging:")

for word in words:
    tags = cfd[word.lower()]
    if tags:
        tag = tags.max()
        print(word, ":", tag)
    else:
        print(word, ": Unknown")
