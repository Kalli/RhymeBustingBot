import nltk
import re
import os

nltk.data.path.append(os.getcwd()+"/nltk_data")
d = nltk.corpus.cmudict.dict()

def count_syllables(word):
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    if word.lower() in d:
        return max([len([y for y in x if (y[-1].isdigit())]) for x in d[word.lower()]])
    else:
        return sum(word.count(c) for c in vowels)

def real_word(w):
    return re.match(".*\w+.*", w) and w in d and len(d[w]) == 1

def rhyme(word1, word2):
    if word1 in word2 or word2 in word1:
        return 0
    w1 = d[word1][0][::-1]
    w2 = d[word2][0][::-1]
    if w1 == w2: 
        return 0
    else:
        return phoneme_match(w1, w2)

def phoneme_match(w1, w2):
    matching_phonemes = 0
    vowel_match = True
    vowel_found = False
    matching_phonemes = 0
    for i in range(0, min(len(w1), len(w2))):
        if vowel_match:
            if w1[i][-1].isdigit() and w2[i][-1].isdigit() and w1[i][:-1] == w2[i][:-1]:
                matching_phonemes += 1
                vowel_found = True
            elif w1[i] == w2[i]:
                matching_phonemes += 1
            else:
                vowel_match = False
    if vowel_found:
        return matching_phonemes
    else:
        return 0

def find_rhymes(lyrics1, lyrics2):
    m = 0
    hit = (0, 0, 0)
    for index1, line1 in enumerate(lyrics1):
        tokens1 = nltk.word_tokenize(line1)
        if tokens1:
            for index2, line2 in enumerate(lyrics2):
                tokens2 = nltk.word_tokenize(line2)
                if tokens2 and real_word(tokens1[-1]) and real_word(tokens2[-1]):
                    if rhyme(tokens1[-1], tokens2[-1]) > m:
                        m = rhyme(tokens1[-1], tokens2[-1])
                        hit = (m, index1, index2)
    return hit





