# def sat_to_3sat(formula):
#     new_formula = []
#     for clause in formula:
#         if len(clause) == 3:
#             new_formula.append(clause)
#         elif len(clause) < 3:
#             while len(clause) < 3:
#                 clause.append(0)  # Use a dummy variable
#             new_formula.append(clause)
#         else:
#             while len(clause) > 3:
#                 new_clause = clause[:2] + [len(new_formula) + 1]
#                 new_formula.append(new_clause)
#                 clause = [len(new_formula)] + clause[2:]
#             new_formula.append(clause)
#     return new_formula
def sat_to_3sat(formula):
    new_formula = []
    max_var = 0  # Track the highest variable used

    # Find the maximum variable in the formula
    for clause in formula:
        for literal in clause:
            max_var = max(max_var, abs(literal))

    max_var += 1  # Start new variables from max_var + 1

    for clause in formula:
        if len(clause) == 1:
            # Case 1: Clause with one literal, introduce two new variables z1, z2
            z1 = max_var
            z2 = max_var + 1
            max_var += 2  # Increment variable counter
            new_formula.extend([
                [clause[0], z1, z2],
                [clause[0], -z1, z2],
                [clause[0], z1, -z2],
                [clause[0], -z1, -z2]
            ])

        elif len(clause) == 2:
            # Case 2: Clause with two literals, introduce one new variable z1
            z1 = max_var
            max_var += 1  # Increment variable counter
            new_formula.extend([
                [clause[0], clause[1], z1],
                [clause[0], clause[1], -z1]
            ])

        elif len(clause) == 3:
            # Case 3: Clause already has 3 literals, no change
            new_formula.append(clause)

        else:
            # Case 4: Clause with more than 3 literals
            # Break down the clause by introducing new variables (z1, z2, ..., zk-3)
            new_vars = []
            for i in range(len(clause) - 3):
                z = max_var
                max_var += 1
                new_vars.append(z)

            # First clause: (l1 ∨ l2 ∨ z1)
            new_formula.append([clause[0], clause[1], new_vars[0]])

            # For the remaining literals, generate clauses: (l3 ∨ -z1 ∨ z2), (l4 ∨ -z2 ∨ z3), ...
            for i in range(1, len(clause) - 3):
                new_formula.append([clause[i + 1], -new_vars[i - 1], new_vars[i]])

            # The last clause: (lk-1 ∨ lk ∨ -zk-3)
            new_formula.append([clause[-2], clause[-1], -new_vars[-1]])

    max_var -= 1
    return new_formula, max_var
