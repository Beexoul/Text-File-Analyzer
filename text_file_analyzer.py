import string
filename = input("Enter the name of the text file: ")
with open(filename, 'r') as file:
    text = file.read()

words = text.split()
num_words = len(words)

sentences = text.split(".")
num_sentences = len(sentences)

paragraphs = text.split("\n\n")
num_paragraphs = len(paragraphs)

word_freq = {}
for word in words:
    word = word.translate(str.maketrans('', '', string.punctuation))
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

most_freq_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]

print("Number of words:", num_words)
print("Number of sentences:", num_sentences)
print("Number of paragraphs:", num_paragraphs)
print("Most frequent words:")
for word, freq in most_freq_words:
    print(word, "-", freq)
