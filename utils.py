import random

def generate_random_formula(nb_vars, num_clauses):
    formula = []
    for _ in range(num_clauses):
        clause = []
        for _ in range(random.randint(1, 3)):  # Randomize clause size (1 to 3 literals)
            var = random.randint(1, nb_vars)
            clause.append(var if random.random() > 0.5 else -var)
        formula.append(clause)
    return formula
