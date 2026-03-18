import numpy as np
from scipy.optimize import linprog

def set_cover_lp_rounding(universe, subsets, costs):
    """
    Solves Set Cover via LP Relaxation and Deterministic Rounding.
    Complexity: Polynomial
    """
    n_subsets = len(subsets)
    n_elements = len(universe)
    universe_list = list(universe)
    
    # Objective: Minimize sum of (costs[i] * x[i])
    c = np.array(costs)
    
    # Constraints: For each element, sum(x_i for sets containing element) >= 1
    A_ub = []
    for element in universe_list:
        row = [1 if element in subsets[i] else 0 for i in range(n_subsets)]
        A_ub.append(row)
    
    # linprog uses A_ub * x <= b_ub, so we multiply by -1 for >= 1
    A_ub = -np.array(A_ub)
    b_ub = -np.ones(n_elements)
    
    # Bounds: 0 <= x_i <= 1
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=(0, 1), method='highs')
    
    if res.success:
        # Deterministic Rounding: If the LP says pick 0.5 or more, we take the set
        selected = [i for i, val in enumerate(res.x) if val >= 0.5]
        return selected, res.fun
    return None, None

if __name__ == "__main__":
    U = {1, 2, 3, 4}
    S = [{1, 2}, {2, 3}, {3, 4}, {1, 4}]
    Costs = [10, 10, 10, 10]
    
    indices, lp_val = set_cover_lp_rounding(U, S, Costs)
    print(f"LP Selected Subset Indices: {indices}")
    print(f"LP Relaxation Lower Bound: {lp_val:.2f}")