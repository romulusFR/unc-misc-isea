"""Est-ce que Ronaldo a de la chance de marquer un but dans chaque minute de match

Exemple pris par SB le 6/5/22

"""

# %%

from collections import Counter
import numpy as np
import seaborn as sns

# %%

NB_SIM = 1000


def run(nb_buts, nb_sim=NB_SIM):
    """Simulation pour un nb de buts"""
    nb_ok = 0
    for _ in range(nb_sim):
        buts = np.random.randint(90, size=nb_buts)
        counts = np.bincount(buts)
        # counts = Counter(buts)
        # sns.histplot(b, bins=90)
        # print(i, nb_minutes)
        # if len(counts.keys()) == 90:
        #    nb_ok += 1
        if counts.shape == (90,) and np.sum(counts == 0) == 0:
            nb_ok += 1
    return nb_ok


nb = run(385)

print(f"Ronaldo had {100*nb/NB_SIM}% chance to score on each minute.")

# %%

d = {}
for nb in range(0, 1001):
    n = run(nb, 1000)
    d[nb] = n
# %%

sns.scatterplot(x=d.keys(), y=d.values())
