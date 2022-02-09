"""Word Finder: finds random words from a dictionary."""

from random import choice


class WordFinder:
    def __init__(self, path):
        file = open(path)
        self.words = self.parse(file)
        print(f"There are {len(self.words)} Words in the file")


    def parse(self, file):
        return [w.strip() for w in file]

    def random(self):
        return choice(self.words)

words = WordFinder('words.txt')
print(words.random())

