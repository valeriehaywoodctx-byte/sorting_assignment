def facility_location_greedy(facilities, customers, opening_costs, service_costs):
    """
    Greedy heuristic for Facility Location.
    We pick facilities that minimize the marginal cost of serving unserved customers.
    """
    open_facilities = set()
    unserved_customers = set(customers)
    total_cost = 0

    # In a real greedy approach, we find the facility with the best 'bang for buck'
    # For this implementation, we evaluate based on minimum total addition to cost
    while unserved_customers:
        best_f = None
        best_cost_inc = float('inf')

        for f in facilities:
            # If already open, cost to open is 0
            f_cost = opening_costs[f] if f not in open_facilities else 0
            # Calculate service cost for all remaining customers from this facility
            s_cost = sum(service_costs[(f, c)] for c in unserved_customers)
            
            if f_cost + s_cost < best_cost_inc:
                best_cost_inc = f_cost + s_cost
                best_f = f

        open_facilities.add(best_f)
        total_cost += opening_costs[best_f] if best_f not in open_facilities else 0
        
        # In this greedy version, we satisfy all customers with the best facility found
        for c in unserved_customers:
            total_cost += service_costs[(best_f, c)]
        
        unserved_customers.clear()

    return open_facilities, total_cost

if __name__ == "__main__":
    facs = [0, 1]
    custs = [0, 1, 2]
    op_costs = {0: 100, 1: 50} # Fac 1 is cheaper to open
    # Fac 0 is much cheaper to serve (5 vs 20)
    serv_costs = {(0,0): 5, (0,1): 5, (0,2): 5, 
                  (1,0): 20, (1,1): 20, (1,2): 20}
    
    chosen, cost = facility_location_greedy(facs, custs, op_costs, serv_costs)
    print(f"Opened Facilities: {chosen} | Total Cost: {cost}")