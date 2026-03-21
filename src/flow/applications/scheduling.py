from src.flow.core.network import FlowNetwork
from src.flow.core.edmonds_karp import edmonds_karp

def solve_scheduling(project_demands, engineer_capacities, assignments):
    """
    project_demands: {'ProjectA': 20, 'ProjectB': 10}
    engineer_capacities: {'Alice': 15, 'Bob': 20}
    assignments: List of (Project, Engineer, MaxHoursPerProject)
    """
    fn = FlowNetwork()
    source = 'START'
    sink = 'END'
    
    # 1. Source to Projects (Demand)
    for project, demand in project_demands.items():
        fn.add_edge(source, project, demand)
        
    # 2. Projects to Engineers (Matching constraints)
    for proj, eng, limit in assignments:
        fn.add_edge(proj, eng, limit)
        
    # 3. Engineers to Sink (Total Capacity)
    for eng, cap in engineer_capacities.items():
        fn.add_edge(eng, sink, cap)
        
    max_hours, flow_dict = edmonds_karp(fn, source, sink)
    
    # Extract specific schedule
    schedule = []
    for proj, eng, limit in assignments:
        hours = flow_dict.get((proj, eng), 0)
        if hours > 0:
            schedule.append(f"{eng} works {hours}h on {proj}")
            
    return max_hours, schedule