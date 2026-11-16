
import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'boy' | 'apple'
V -> 'eats'
""")

parser = nltk.ChartParser(grammar)

sentence = "the boy eats the apple".split()

print("Parsing Result:")

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
