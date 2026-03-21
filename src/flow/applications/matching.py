from src.flow.core.network import FlowNetwork
from src.flow.core.edmonds_karp import edmonds_karp

def max_bipartite_matching(applicants, jobs, qualifications):
    """
    Solves the matching problem by reducing it to Max-Flow.
    qualifications: list of tuples (applicant, job)
    """
    fn = FlowNetwork()
    source = 'source'
    sink = 'sink'

    # 1. Connect source to all applicants
    for person in applicants:
        fn.add_edge(source, person, 1)

    # 2. Connect all jobs to sink
    for job in jobs:
        fn.add_edge(job, sink, 1)

    # 3. Connect applicants to qualified jobs
    for person, job in qualifications:
        fn.add_edge(person, job, 1)

    # 4. Run Max Flow
    max_matches, flow_dict = edmonds_karp(fn, source, sink)
    
    # Extract the matching pairs
    matches = []
    for person, job in qualifications:
        if flow_dict.get((person, job), 0) == 1:
            matches.append((person, job))
            
    return max_matches, matches