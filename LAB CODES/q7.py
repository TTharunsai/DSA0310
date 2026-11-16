
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

text = "The boy is playing cricket"

words = nltk.word_tokenize(text)

result = nltk.pos_tag(words)

print("POS Tagging:")
for word, tag in result:
    print(word, ":", tag)
