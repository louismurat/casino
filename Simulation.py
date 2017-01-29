from collections import Counter
import numpy as np
from matplotlib import pyplot as plt
import random

random.seed(3456)


# creation of the simulation of the thousand throws
thousandsthrows = [random.randint(1, 6)+random.randint(1, 6) for _ in range(1000)]

labels, values = zip(*sorted(Counter(thousandsthrows).items()))
indexes = np.arange(len(labels))
width = 1
plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.show()

# we create a millions of throws
millions_throws = [random.randint(1, 6)+random.randint(1, 6) for _ in range(1000000)]
print(Counter(millions_throws))
# we sort them
list_resultat = sorted(Counter(millions_throws).items())
print(list_resultat)
# we obtain the number of result of throws of dices
list_nombre = []
for i, j in list_resultat:
    list_nombre.append(int(j))

# we multiply by a possible list of return amount
list_retour = np.array([30, 15, 10, 7.5, 6, 4, 6, 7.5, 10, 15, 30])
print(list_nombre)
print(list_nombre*list_retour)
print(sum(list_nombre*list_retour))