from dictionary import Dictionary


class SourceFile:

    def __init__(self, fullpath):
        self.fullpath = fullpath
        self.wordcount = 0
        self.profanityscore = 0
        self.profanewordcount = [0, 0, 0, 0, 0]
        self.profanewords = []
        self.profanelines = []

    def favoriteprofaneword(self):
        from collections import Counter
        words = Counter(self.profanewords)
        favoriteword = words.most_common(1)
        if len(favoriteword) > 0:
            return [elem[0] for elem in favoriteword][0]
        else:
            return None

    def parse(self):
        dictionary = Dictionary()
        # Split file into tokens
        with open(self.fullpath) as file:
            for linenum, line in enumerate(file):
                for word, score in dictionary.wordlist.items():
                    matches = dictionary.regexlist[word].findall(line)
                    if matches:
                        for match in matches:
                            self.wordcount += 1
                            self.profanewordcount[int(score)] += 1
                            self.profanityscore += int(score)
                            self.profanelines.append(linenum)
                            self.profanewords.append(word)