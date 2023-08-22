"""
Consider a variation of the Monty Hall problem with four doors, two of which hide a goat and two of which hide a car.
In this variation, Monty doesn't know where the cars are, so he chooses one of the three remaining doors at random once 
you make your choice. He then offers you the choice of switching to one of the unopened doors, or staying with your door.

(a) Assuming you stay, what is the probability that you get a car given Monty revealed a goat?
    
(b) Assuming you switch, what is the probability that you get a car given Monty revealed a goat?
    
(c) Based on your answers, should you switch or stay if Monty reveals a goat? What about if he reveals a car?

(d) Assuming you switch, what is the probability that Monty revealed a goat given you got a car?
"""

import random
from typing import Callable

NUM_TRIALS = 100000


def choose_random_door(doors: list[str]) -> str:
    choice = random.choice(doors)
    doors.remove(choice)
    return choice


def simulate_game(strategy: str) -> (str, str):
    doors = ["goat", "goat", "car", "car"]

    your_choice = choose_random_door(doors)
    montys_choice = choose_random_door(doors)
    if strategy == "switch":
        your_choice = choose_random_door(doors)

    return your_choice, montys_choice


def estimate_event_probability(strategy: str, event: Callable) -> float:
    successes = 0
    for _ in range(NUM_TRIALS):
        your_choice, montys_choice = simulate_game(strategy)
        if event(your_choice, montys_choice):
            successes += 1

    return successes / NUM_TRIALS


# Events

def monty_reveals_goat(your_choice: str, montys_choice: str) -> bool:
    return montys_choice == "goat"


def you_win_car_and_monty_reveals_goat(your_choice: str, montys_choice: str) -> bool:
    return your_choice == "car" and montys_choice == "goat"


def you_win_car(your_choice: str, montys_choice: str) -> bool:
    return your_choice == "car"


def main():
    # Assuming you stay, probability that you get a car given Monty reveals a goat
    part_a_answer = (estimate_event_probability(strategy="stay", event=you_win_car_and_monty_reveals_goat) 
                     / estimate_event_probability(strategy="stay", event=monty_reveals_goat))
    
    # Assuming you switch, probability that you get a car given Monty reveals a goat
    part_b_answer = (estimate_event_probability(strategy="switch", event=you_win_car_and_monty_reveals_goat)
                     / estimate_event_probability(strategy="switch", event=monty_reveals_goat))
    
    # Assuming you switch, probability that Monty reveals a goat given you get a car
    part_d_answer = (estimate_event_probability(strategy="switch", event=you_win_car_and_monty_reveals_goat)
                     / estimate_event_probability(strategy="switch", event=you_win_car))
    
    print("Part (a):", part_a_answer)
    print("Part (b):", part_b_answer)
    print("Part (d):", part_d_answer)


main()


"""
The answers to part (a), (b), and (d) are all 2/3.

For part (c), your choice does not matter.
If Monty reveals a goat, your win probability is 2/3 regardless of if you switch or stay.
If he reveals a car, your win probability is 1/3 either way.
"""
