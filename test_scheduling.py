from src.flow.applications.scheduling import solve_scheduling

def test_office_hours():
    demands = {'Alpha': 20, 'Beta': 15}
    caps = {'Alice': 18, 'Bob': 20}
    
    # (Project, Engineer, Max allowed on this specific project)
    assignments = [
        ('Alpha', 'Alice', 10),
        ('Alpha', 'Bob', 15),
        ('Beta', 'Alice', 10),
        ('Beta', 'Bob', 10)
    ]
    
    total_hours, work_plan = solve_scheduling(demands, caps, assignments)
    
    print("--- Part 2: Scheduling Application ---")
    print(f"Total Billable Hours Managed: {total_hours}")
    for plan in work_plan:
        print(f"  {plan}")

if __name__ == "__main__":
    test_office_hours()