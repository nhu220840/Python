# Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
# frequently and their corresponding appearance. You could ignore all
# function characters such as comma, dot, semicolon, ...
# Sample output:
# house: 453
# dog: 440
# people: 312
# ...

from collections import Counter
from re import split


def main():
    counter = Counter()
    with open("data_science/Ex2/story.txt", "r") as f:
        for line in f:
            line = line.strip().lower()
            if not line:
                continue
            counter.update(x for x in split("[^a-z]+", line) if x)
    freqSorted = sorted(counter, key=counter.get, reverse=True)
    longestWord = max(counter, key=len)
    wordLength = len(longestWord)

    count = 0
    print("Word".rjust(16), "|", "Count".ljust(16))
    print("=" * 35)
    for word in freqSorted:
        print(word.title().rjust(16), "|", str(counter[word]).ljust(16))
        count += 1
        if count >= 100:
            break


if __name__ == '__main__':
    main()