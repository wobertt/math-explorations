import random as r


class Literal:
    def __init__(self, index: int, value: bool):
        self.index = index
        self.value = value

    
    def to_string(self):
        return f"{self.index} {self.value}"


class Formula:
    def __init__(self, N: int):
        self.N = N
        self.true_assignments = list(range(1 << N))


    def is_satisfiable(self):
        return bool(self.true_assignments)
    

    def add_clause(self, clause: list[Literal]):
        self.true_assignments = [
            assignment for assignment in self.true_assignments
            if any(((assignment >> literal.index) & 1) == literal.value for literal in clause)
        ]


class CNFSimulator:
    def __init__(self, N: int):
        self.N = N

    def get_random_literal(self):
        return Literal(r.randint(0, self.N-1), r.choice([False, True]))
    

    def get_random_clause(self):
        return [self.get_random_literal() for _ in range(3)]
    

    def simulate_trial(self):
        formula = Formula(self.N)
        k = 0
        while formula.is_satisfiable():
            k += 1
            formula.add_clause(self.get_random_clause())
        return k
    
    
    def simulate_trials(self, t):
        return [self.simulate_trial() for _ in range(t)]


def get_probabilities(results: list[int]):
    p_greater_than = []
    for i in range(1, max(results)):
        p_greater_than.append(len([x for x in results if x > i]) / len(results))
    return p_greater_than


def main():
    simulator = CNFSimulator(20)
    num_trials = 1000
    results = simulator.simulate_trials(num_trials)
    # print(results)
    print(get_probabilities(results))


main()
