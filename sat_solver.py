def solve_sat(formula):
    def is_satisfiable(formula, assignment={}):
        # Check if the formula is satisfied
        if all(any((lit > 0 and assignment.get(abs(lit), False)) or (lit < 0 and not assignment.get(abs(lit), False)) for lit in clause) for clause in formula):
            return assignment

        # Check if the formula is unsatisfiable
        if any(all((lit > 0 and assignment.get(abs(lit), False) is False) or (lit < 0 and assignment.get(abs(lit), False) is True) for lit in clause) for clause in formula):
            return None

        # Find the first unassigned variable
        unassigned = next((abs(lit) for clause in formula for lit in clause if abs(lit) not in assignment), None)
        if unassigned is None:
            return None

        # Try assigning True and False to the unassigned variable
        for value in [True, False]:
            assignment[unassigned] = value
            result = is_satisfiable(formula, assignment)
            if result:
                return result
            del assignment[unassigned]

        return None

    return is_satisfiable(formula)


def solve_3sat(formula):
    return solve_sat(formula)  # Reuse the SAT solver
