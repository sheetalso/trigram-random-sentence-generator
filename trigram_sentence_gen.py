from text_cleaning import cleanse_dict
import random
from nltk import word_tokenize, trigrams
from collections import defaultdict


def cleanse(words):
    """converts contractions to real words"""
    result = []
    for word in words:
        if word not in cleanse_dict.keys():
            result.append(word)
        else:
            result.append(cleanse_dict[word])
    return result


def get_trigrams(path):
    """converts text input into trigrams"""
    with open(path, 'r') as f:
        raw_text = f.read()

    text = " ".join(cleanse(raw_text.split()))
    words = word_tokenize(text)
    return [gram for gram in trigrams(words)]


def generate_using_trigrams(starts, trigram_transitions):
    """generates a random sentence"""
    current = random.choice(starts)   # choose a random starting word
    prev = "."   # and precede it with punctuation
    result = [current]
    while True:
        next_word_candidates = trigram_transitions[(prev, current)]
        next = random.choice(next_word_candidates)

        prev, current = current, next
        result.append(current)

        if current == ".":
            return " ".join(result)


def make_paragraph(gen_fn, grams):
    """uses text generation function to assemble a paragraph"""
    trigram_transitions = defaultdict(list)
    starts = []

    for prev, current, next in grams:
        if prev == ".":              # if previous word was a period
            starts.append(current)   # then this was a start word

        trigram_transitions[(prev, current)].append(next)

    text = ""
    for i in xrange(random.randrange(3, 12)):    # produces variable length sentences
        text += generate_using_trigrams(starts, trigram_transitions)

    return text.replace(" .", ". ") \
               .replace(" ,", ",") \
               .replace(" ?", "?") \
               .replace(" n't", "n't") \
               .replace(" 's", "'s") \
               .replace(" 'd", "'d") \
               .replace(" ''", "") \
               .replace(" ..", "...")   # the replacements are ugly and could obviously be done better, but handles some edge cases

if __name__ == "__main__":
    path = "<path to your text file>"
    grams = get_trigrams(path)
    gen_fn = generate_using_trigrams
    print make_paragraph(gen_fn, grams)
