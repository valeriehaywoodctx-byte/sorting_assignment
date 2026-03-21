from src.flow.applications.matching import max_bipartite_matching

def test_hiring():
    applicants = ['Alice', 'Bob', 'Charlie', 'David']
    jobs = ['Dev', 'Design', 'QA', 'Manager']
    
    qualifications = [
        ('Alice', 'Dev'), ('Alice', 'Design'),
        ('Bob', 'Dev'),
        ('Charlie', 'Dev'), ('Charlie', 'QA'),
        ('David', 'QA'), ('David', 'Manager')
    ]
    
    count, pairs = max_bipartite_matching(applicants, jobs, qualifications)
    
    print(f"Total Positions Filled: {count}")
    for p, j in pairs:
        print(f"  Assignment: {p} -> {j}")

if __name__ == "__main__":
    test_hiring()