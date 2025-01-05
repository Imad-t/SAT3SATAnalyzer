from sat_solver import solve_sat, solve_3sat
from verifier import verify_solution
from reduction import sat_to_3sat
from utils import generate_random_formula

def main():
    nbr_vars = 10
    nbr_clauses = 10 
    # Example usage
    sat_formula = generate_random_formula(nb_vars=nbr_vars, num_clauses=nbr_clauses)
    print("Generated SAT Formula:", sat_formula)

    # Solve SAT
    sat_result = solve_sat(sat_formula, nb_vars=nbr_vars)
    print("SAT Solution:", sat_result)

    # Convert to 3-SAT
    three_sat_formula,nbr_vars = sat_to_3sat(sat_formula)
    print("Converted 3-SAT Formula:", three_sat_formula)

    # Solve 3-SAT
    three_sat_result = solve_3sat(three_sat_formula, nb_vars=nbr_vars)
    print("3-SAT Solution:", three_sat_result)

    # Verify solutions
    if sat_result:
        print("SAT Solution Verified:", verify_solution(sat_formula, sat_result))
    if three_sat_result:
        print("3-SAT Solution Verified:", verify_solution(three_sat_formula, three_sat_result))

if __name__ == "__main__":
    main()
