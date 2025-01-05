from typing import List, Dict, Union

def solve_sat(clauses: List[List[int]], nb_vars: int) -> Union[Dict[int, bool], None]:
    """
    Try to find an assignment satisfying all clauses.
    :param clauses: list of clauses, each clause is a list of "literals"
    :param nb_vars: number of variables (n)
    :return: a dictionary {var_index -> bool} representing the assignment,
             or None if unsatisfiable.
    """
    assignment = {}  # var_index -> bool, e.g., {1: True, 2: False, ...}

    def backtrack(var_index: int) -> bool:
        # If all variables are assigned, check if the assignment satisfies all clauses
        if var_index > nb_vars:
            return check_all_clauses(assignment, clauses)

        # Try assigning True or False to the current variable
        for val in [True, False]:
            assignment[var_index] = val
            if backtrack(var_index + 1):
                return True
            # Backtrack if no solution found
            del assignment[var_index]
        return False

    def check_all_clauses(assign: Dict[int, bool], cls: List[List[int]]) -> bool:
        # Check that all clauses are satisfied by the current assignment
        for clause in cls:
            satisfied = False
            for literal in clause:
                if literal > 0 and assign[abs(literal)] is True:
                    satisfied = True
                    break
                if literal < 0 and assign[abs(literal)] is False:
                    satisfied = True
                    break
            if not satisfied:
                return False
        return True

    if backtrack(1):  # Start with variable 1
        return assignment
    else:
        return None

def solve_3sat(clauses: List[List[int]], nb_vars: int) -> Union[Dict[int, bool], None]:
    """
    Try to find an assignment satisfying all clauses, where each clause contains exactly 3 literals.
    """
    assignment = {}

    def backtrack(var_index: int) -> bool:
        # If all variables are assigned, check if the assignment satisfies all clauses
        if var_index > nb_vars:
            return check_all_clauses(assignment, clauses)

        # Try assigning True or False to the current variable
        for val in [True, False]:
            assignment[var_index] = val
            if backtrack(var_index + 1):
                return True
            # Backtrack if no solution found
            del assignment[var_index]
        return False

    def check_all_clauses(assign: Dict[int, bool], cls: List[List[int]]) -> bool:
        # Check that all clauses are satisfied by the current assignment
        for clause in cls:
            satisfied = False
            for literal in clause:
                if literal > 0 and assign[abs(literal)] is True:
                    satisfied = True
                    break
                if literal < 0 and assign[abs(literal)] is False:
                    satisfied = True
                    break
            if not satisfied:
                return False
        return True

    if backtrack(1):  # Start with variable 1
        return assignment
    else:
        return None
