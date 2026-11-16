
import nltk

words = ["The", "dog", "runs", "fast"]

# Initial tagging
tagged_words = [
    ("The", "NN"),
    ("dog", "NN"),
    ("runs", "NN"),
    ("fast", "NN")
]

# Transformation rule
for i, (word, tag) in enumerate(tagged_words):
    if word.lower() == "the":
        tagged_words[i] = (word, "DT")
    elif word.endswith("s"):
        tagged_words[i] = (word, "VBZ")
    elif word.lower() == "fast":
        tagged_words[i] = (word, "RB")

print("Transformation-Based Tagging:")

for word, tag in tagged_words:
    print(word, ":", tag)
