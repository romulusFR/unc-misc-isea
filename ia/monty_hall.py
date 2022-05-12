"""Main module
PML : 2.3.2 Example: The Monty Hall problem
"""

# %%
import numpy as np

TRIALS = 10
DOORS_NB = 3
DOORS = set(range(DOORS_NB))
np.random.seed(None)


def gen_games(nb=TRIALS):
    """Generate n choices of doors [0, .., DOORS_NB-1]"""
    return np.random.randint(DOORS_NB, size=nb)


def play(winning_door):
    """A run :
    1. the player pick a door
    2. the host shows another loossing door
    3. the player stays or switches his pick
    """
    players_choice = np.random.randint(DOORS_NB)
    free_doors = DOORS - {winning_door, players_choice}
    showed_door = np.random.choice(list(free_doors))
    return winning_door, players_choice, showed_door


def winning(triple):
    """Compute winnings"""
    winning_door, players_choice, showed_door = triple
    win_when_stays = winning_door == players_choice

    pickable = DOORS - {showed_door, players_choice}
    picked_door = np.random.choice(list(pickable))
    win_when_switches = winning_door == picked_door

    return win_when_stays, win_when_switches


def run(nb=TRIALS):
    """Run many games and compute odds"""
    games = gen_games(nb)
    nb_wins_staying = 0
    nb_wins_switching = 0
    for door in games:
        stay, switch = winning(play(door))
        nb_wins_staying += stay
        nb_wins_switching += switch
    return nb_wins_staying, nb_wins_switching


if __name__ == "__main__":
    n = 10000
    w_stays, w_switches = run(n)
    print(f"{100*w_stays/n:.2f}% winning staying")
    print(f"{100*w_switches/n:.2f}% winning switching")
    print(f"{w_switches/w_stays:.2f}x staying/switching odds")
