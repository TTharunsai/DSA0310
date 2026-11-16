
from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "played", "plays", "running", "happiness"]

for word in words:
    print(word, ":", ps.stem(word))
