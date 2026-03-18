def is_satisfied(clause, assignment):
    """ Checks if a single clause is True under current assignment. """
    for literal in clause:
        var = abs(literal)
        val = assignment.get(var)
        if val is not None:
            # If literal is positive and var is True, OR literal is negative and var is False
            if (literal > 0 and val) or (literal < 0 and not val):
                return True
    return False

def solve_sat(variables, clauses, assignment={}):
    """ Simple backtracking SAT solver. """
    if not variables:
        return assignment if all(is_satisfied(c, assignment) for c in clauses) else None

    var = variables[0]
    remaining = variables[1:]

    # Try setting variable to True
    assignment[var] = True
    result = solve_sat(remaining, clauses, assignment)
    if result: return result

    # Try setting variable to False
    assignment[var] = False
    result = solve_sat(remaining, clauses, assignment)
    if result: return result

    # Backtrack
    del assignment[var]
    return None

if __name__ == "__main__":
    # Formula: (x1) AND (NOT x1 OR x2)
    vars_list = [1, 2]
    formula = [[1], [-1, 2]]
    print(f"SAT Solution: {solve_sat(vars_list, formula)}")