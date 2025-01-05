def verify_solution(formula, assignment):
    return all(
        any(
            (lit > 0) == assignment[abs(lit)]
            for lit in clause
        )
        for clause in formula
    )