# SwearScan

Do you ever get so angry while programming that you leave streams of profanity in your source code? Are you a [C++ programmer](https://www.wired.com/2011/02/cussing-in-commits-which-programming-language-inspires-the-most-swearing/) or an [aspiring Linux kernel maintainer](https://www.vidarholen.net/contents/wordcount/)? Every wonder how many of your fellow developers are just as much of a potty mouth as you?

SwearScan is a tool that scans code (and other text-based file) directories for profanity, then scores you based on volume and vulgarity. It's a fun little tool for checking the conversational cleanliness of your source code.

DISCLAIMER: This project may contain words or references that some individuals might find offensive. These words do not reflect my own personal beliefs and are included solely for demonstrative purposes. 

```bash
...
Scanning /home/user/my-repo/my-file.h
Line 3:	    ****
Line 6:	    ****
Line 20:    ****
Found 3 words for a score of 9
...

Total files scanned: 53
Words found: 10 Mild, 16 Medium, 20 Strong, 11 Very Strong
Most profane file: /home/swearscan/my-repo/my-file.cpp with 45 words for a score of 121
Most common word: ****
Total score: 146
```

## How to use it

Call the script with the directory you want to scan:

```$ python swearscan.py ~/my-project```

## How it works

The profanity dictionary is sourced from [Ofcom](http://www.digitalspy.com/tv/news/a809925/ofcom-swear-words-ranking-in-order-of-offensiveness/) with minor modifications.

Each word has an assigned rating based on its vulgarity:

- Mild: 1
- Medium: 2
- Strong: 3
- Strongest: 4

The ratings are summed for each file, then for the entire directory. Each file is scanned line-by-line using Regular Expressions, and any matches are listed underneath the file name with the line number that they appear on. SwearScan also shows the total number of profane words, the most commonly used word, and the most vulgar file.

### Adding and Removing Words

Words and their ratings are stored as comma-separated values in the [dictionary.csv](dictionary.csv) file.