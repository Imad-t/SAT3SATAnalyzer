from typing import List, Dict, Union

def solve_sat(clauses: List[List[int]], nb_vars: int) -> Union[Dict[int, bool], None]:
    assignment = {}  # var_index -> bool

    def backtrack(var_index: int) -> bool:
        # if all variables are assigned, check if the assignment satisfies all clauses
        if var_index > nb_vars:
            return check_all_clauses(assignment, clauses)

        # try assigning True or False to the current variable
        for val in [True, False]:
            assignment[var_index] = val
            if backtrack(var_index + 1):
                return True
            # backtrack if no solution 
            del assignment[var_index]
        return False

    def check_all_clauses(assign: Dict[int, bool], cls: List[List[int]]) -> bool:
        # check if all clauses are satisfied by current assignment
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

    if backtrack(1):  #strat with variable 1
        return assignment
    else:
        return None

def solve_3sat(clauses: List[List[int]], nb_vars: int) -> Union[Dict[int, bool], None]:
    """
    Try to find an assignment satisfying all clauses, where each clause contains exactly 3 literals.
    """
    assignment = {}

    def backtrack(var_index: int) -> bool:
        # if all variables are assigned, check if the assignment satisfies all clauses
        if var_index > nb_vars:
            return check_all_clauses(assignment, clauses)

        # try assigning True or False to the current variable
        for val in [True, False]:
            assignment[var_index] = val
            if backtrack(var_index + 1):
                return True
            # backtrack if no solution 
            del assignment[var_index]
        return False

    def check_all_clauses(assign: Dict[int, bool], cls: List[List[int]]) -> bool:
        # check that all clauses are satisfied by current assignment
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

    if backtrack(1):  # start with variable 1
        return assignment
    else:
        return None
