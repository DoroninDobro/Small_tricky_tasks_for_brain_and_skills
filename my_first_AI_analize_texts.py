# Task for Yandex-specialisations about ML, Scipy, distance vector

import re
import numpy as np
import scipy.spatial.distance

sentences = []
with open("sentences.txt", "r") as i_file:
    for line in i_file:
        sentences.append(line.lower())
with open("sentences.txt", "r") as i_file:
    text = i_file.read().lower()
a = re.split('[^a-z]', text)
i = 0
while i < len(a):
    if len(a[i]) == 0:
        del(a[i])
    else:
        i += 1
words = set(a)
i = 0
dict_word = {}
for word in words:
    dict_word[i] = word
    i += 1
matrix = np.eye(22,254)
for sentence in range(len(sentences)):
    for index in range(len(dict_word)):
        matrix[sentence, index] = len(re.findall(rf"\b{dict_word[index]}\W", sentences[sentence]))
# print(matrix)
# print(sentences[0], sentences[1],sentences[2])
# print(dict_word[0], dict_word[1], dict_word[2])
dists = []
for row in matrix:
    dists.append(scipy.spatial.distance.cosine(matrix[0,:], row))
print(dists)
print(len(dists))







