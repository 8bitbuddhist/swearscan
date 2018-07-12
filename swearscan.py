import os
from sourcefile import SourceFile
import argparse


def main(url):
    files = []
    for root, directories, filenames in os.walk(url):
        for filename in filenames:
            file = SourceFile(os.path.join(root, filename))
            files.append(file)
            try:
                print("Parsing " + file.fullpath)
                file.parse()
                if len(file.profanewords) > 0:
                    for index, word in enumerate(file.profanewords):
                        print("Line " + str(file.profanelines[index] + 1) + ": " + word)
                    print("Found " + str(len(file.profanewords)) + " words for a score of " + str(file.profanityscore))
                    print()
            except Exception as ex:
                print("Failed to parse file: ", ex)

    # Calculate and display statistics
    mostprofanefile = max(files, key=lambda curfile: len(curfile.profanewords))

    from collections import Counter
    mostprofanewords = []
    for file in files:
        word = file.favoriteprofaneword()
        if word is not None:
            mostprofanewords.append(word)

    if len(mostprofanewords) > 0:
        profanewords = Counter(mostprofanewords)
        mostcommonprofaneword = [elem[0] for elem in profanewords.most_common(1)][0]
    else:
        mostcommonprofaneword = "N/A"

    print()
    print("Total files scanned: " + str(len(files)))
    print("Words found: "
          + str(sum(file.profanewordcount[1] for file in files)) + " Mild, "
          + str(sum(file.profanewordcount[2] for file in files)) + " Medium, "
          + str(sum(file.profanewordcount[3] for file in files)) + " Strong, "
          + str(sum(file.profanewordcount[4] for file in files)) + " Very Strong")
    totalprofanityscore = sum(file.profanityscore for file in files)
    if totalprofanityscore > 0 :
        print("Most profane file: " + str(mostprofanefile.fullpath) + " with " + str(len(mostprofanefile.profanewords))
              + " words for a score of " + str(mostprofanefile.profanityscore))
        print("Most common word: " + mostcommonprofaneword)
        print("Total score: " + str(totalprofanityscore))


parser = argparse.ArgumentParser(description='Scan a directory for profanity.')
parser.add_argument('dir', type=str, nargs=1, help='directory to scan')
args = parser.parse_args()
main(args.dir[0])
