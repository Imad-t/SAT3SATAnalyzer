def sat_to_3sat(formula):
    new_formula = []
    for clause in formula:
        if len(clause) == 3:
            new_formula.append(clause)
        elif len(clause) < 3:
            while len(clause) < 3:
                clause.append(0)  # Use a dummy variable
            new_formula.append(clause)
        else:
            while len(clause) > 3:
                new_clause = clause[:2] + [len(new_formula) + 1]
                new_formula.append(new_clause)
                clause = [len(new_formula)] + clause[2:]
            new_formula.append(clause)
    return new_formula
