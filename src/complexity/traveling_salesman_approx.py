import math

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def tsp_nearest_neighbor(cities):
    """
    Greedy heuristic for TSP. Always visit the closest unvisited city.
    Complexity: O(n^2)
    """
    unvisited = list(cities.keys())
    current_city = unvisited.pop(0)
    path = [current_city]
    total_dist = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(cities[current_city], cities[city]))
        total_dist += distance(cities[current_city], cities[next_city])
        current_city = next_city
        unvisited.remove(current_city)
        path.append(current_city)
    
    # Return to start
    total_dist += distance(cities[path[-1]], cities[path[0]])
    path.append(path[0])
    return path, total_dist

if __name__ == "__main__":
    # City Name: (x, y) coordinates
    my_cities = {"A": (0,0), "B": (1,5), "C": (4,1), "D": (3,3)}
    route, dist = tsp_nearest_neighbor(my_cities)
    print(f"Route: {' -> '.join(route)} | Total Distance: {dist:.2f}")