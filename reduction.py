
def sat_to_3sat(formula):
    new_formula = []
    max_var = 0  #  highest variable index value used

    # Find max variable
    for clause in formula:
        for literal in clause:
            max_var = max(max_var, abs(literal))

    max_var += 1 

    for clause in formula:
        if len(clause) == 1:
            # Case 1: clause with one literal, introduce two new variables z1, z2
            #(l ∨ z1 ∨ z2),(l ∨ -z1 ∨ z2),(l ∨ z1 ∨ -z2),(l ∨ -z1 ∨ -z2).

            z1 = max_var
            z2 = max_var + 1
            max_var += 2  # increment variable counter
            new_formula.extend([
                [clause[0], z1, z2],
                [clause[0], -z1, z2],
                [clause[0], z1, -z2],
                [clause[0], -z1, -z2]
            ])

        elif len(clause) == 2:
            # Case 2: clause with two literals, introduce one new variable z1
            #: (l1 ∨ l2 ∨ z1),(l1 ∨ l2 ∨ -z1).
            z1 = max_var
            max_var += 1  # incremnt variable counter
            new_formula.extend([
                [clause[0], clause[1], z1],
                [clause[0], clause[1], -z1]
            ])

        elif len(clause) == 3:
            # Case 3: clause already has 3 literals
            new_formula.append(clause)

        else:
            # Case 4: clause > 3 literals
            # introducing new variables (z1, z2, ..., zk-3) so that:
            #(l1 ∨ l2 ∨ z1),(l3 ∨ -z1 ∨ z2),(l4 ∨ -z2 ∨ z3), . . . ,(lk−2 ∨ -zk−4 ∨ zk−3),(lk−1 ∨ lk ∨ -zk−3)
            new_vars = []
            for i in range(len(clause) - 3):
                z = max_var
                max_var += 1
                new_vars.append(z)

            # 1st clause(l1 ∨ l2 ∨ z1)
            new_formula.append([clause[0], clause[1], new_vars[0]])

            # For remaining literals, generate clauses: (l3 ∨ -z1 ∨ z2), (l4 ∨ -z2 ∨ z3), ...
            for i in range(1, len(clause) - 3):
                new_formula.append([clause[i + 1], -new_vars[i - 1], new_vars[i]])

            #last clause: (lk-1 ∨ lk ∨ -zk-3)
            new_formula.append([clause[-2], clause[-1], -new_vars[-1]])

    max_var -= 1
    return new_formula, max_var
