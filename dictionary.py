import re


class Dictionary:

    def __init__(self):
        self.wordlist = {}
        self.regexlist = {}
        with open('dictionary.csv') as dictfile:
            for line in dictfile:
                (key, value) = line.split(",")
                self.wordlist[key] = value
                # Generate Regex lookup table
                self.regexlist[key] = re.compile(str.format(r"\b{}\b", re.escape(key)))
