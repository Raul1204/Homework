import certifi
import ssl
from urllib.request import urlopen

url = ()
url1 = "https://www.gutenberg.org/files/84/84-0.txt"
url2 = "https://www.gutenberg.org/files/67632/67632-0.txt"
local_name = "frankenstein.txt"
ul = input("which do you want to read first url1 or url2?:")
if ul == "url1":
    url = url1
elif ul == "url2":
    url = url2






def save_locally():
    """
    Save the book locally, so we can use it faster and no need to load every time
    :return: None
    """
    with open(local_name, "w") as local_fp:
        with urlopen(url, context=ssl.create_default_context(cafile=certifi.where())) as fp:
            for line in fp:
                line = line.decode('utf-8-sig').replace("\n", "")
                local_fp.write(line)


punctuation = ",;!.?-()"
def get_unique_words():
    """
    Get the dictionary of unique words and their frequency
    :return: dict
    """
    unique_words = {}
    with open(local_name) as fp:
        for line in fp:
            # remove punctuation
            for p in punctuation:
                line = line.replace(p, " ")
            line = line.lower()
            # get the words:
            for word in line.split():
                unique_words[word] = unique_words.get(word, 0) + 1

    return unique_words


save_locally()
unique_words = get_unique_words()
most_frequent = list(unique_words.values())
most_frequent.sort(reverse=True)
# print(most_frequent)
for word_frequency in most_frequent[0:]:
    for unique_word, value in unique_words.items():
        if word_frequency == value:
            print(f"common word '{unique_word}' appears {value} times")
            # change the value so we don't get it again if there are multiple words with the same frequency
            unique_words[unique_word] = -1
            break

#Question 1
print(len(unique_words))

#Question 2
seven_words = []

for word in url:
    if len(word) >=7:
        seven_words.append(word)
print(seven_words)

#Question 3
file = open("frankenstein.txt", "r")
data = file.read()
count_words = data.split()

print("Total number of words", len(count_words))
