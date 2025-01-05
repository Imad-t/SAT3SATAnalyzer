def verify_solution(formula, assignment):
    for clause in formula:
        if not any(assignment.get(abs(lit), False) if lit > 0 else not assignment.get(abs(lit), True) for lit in clause):
            return False
    return True
