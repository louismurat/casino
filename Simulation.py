from collections import Counter
import numpy as np
from matplotlib import pyplot as plt
import random


thousandsthrows = [random.randint(1, 6)+random.randint(1, 6) for _ in range(1000)]

labels, values = zip(*sorted(Counter(thousandsthrows).items()))
indexes = np.arange(len(labels))
width = 1
plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.show()

millions_throws = [random.randint(1, 6)+random.randint(1, 6) for _ in range(1000000)]
print(Counter(millions_throws))

list_resultat = sorted(Counter(millions_throws).items())
print(list_resultat)
list_nombre = []
for i, j in list_resultat:
    list_nombre.append(int(j))


list_retour = np.array([30, 15, 10, 7.5, 6, 4, 6, 7.5, 10, 15, 30])
print(list_nombre)
print(list_nombre*list_retour)
print(sum(list_nombre*list_retour))