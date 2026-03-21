from src.flow.core.network import FlowNetwork
from src.flow.core.edmonds_karp import edmonds_karp
from src.flow.core.push_relabel import push_relabel
from src.flow.core.min_cost_flow import min_cost_max_flow

def test_all():
    fn = FlowNetwork()
    # Simple setup: s -> A -> t
    fn.add_edge('s', 'A', 10, 2) # Cap 10, Cost 2
    fn.add_edge('s', 'B', 10, 5) # Cap 10, Cost 5
    fn.add_edge('A', 't', 5, 1)  # Cap 5, Cost 1
    fn.add_edge('B', 't', 10, 1) # Cap 10, Cost 1

    print("--- Part 1: Core Solver Verification ---")
    
    # Test Max Flow
    val_ek, _ = edmonds_karp(fn, 's', 't')
    val_pr, _ = push_relabel(fn, 's', 't')
    print(f"Max Flow (EK): {val_ek}")
    print(f"Max Flow (PR): {val_pr}")

    # Test Min-Cost
    flow_val, cost_val, _ = min_cost_max_flow(fn, 's', 't')
    print(f"Min-Cost Max-Flow: Flow={flow_val}, Cost={cost_val}")

if __name__ == "__main__":
    test_all()