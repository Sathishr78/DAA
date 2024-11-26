# Write a program that finds the closest pair of points
import math
points = [(1, 2), (4, 5), (7, 8), (3, 1)]
min_distance = float('inf')
closest_pair = None
n = len(points)
for i in range(n):
    for j in range(i + 1, n):
        dist = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
        if dist < min_distance:
            min_distance = dist
            closest_pair = (points[i], points[j])
print(f"Closest pair: {closest_pair[0]} - {closest_pair[1]}")
print(f"Minimum distance: {min_distance}")
#3.program for to find the shortest path pair of points in the given set using brute force approch
import math

def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def closest_pair(points):
    """Find the closest pair of points using the brute force method."""
    min_distance = float('inf')
    closest_points = (None, None)
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_points = (points[i], points[j])

    return closest_points, min_distance
points = [(10, 0), (11, 5), (5, 3), (9, 3.5), (15, 3), (12.5, 7), (6, 6.5), (7.5, 4.5)]
closest_points, distance = closest_pair(points)
print(f"The closest pair of points is: {closest_points} with a distance of {distance:.2f}")
#2.Convex Hull Problem (Brute Force)
import math
def calculate_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
def find_closest_pair(points):
    """Find the closest pair of points using brute force."""
    min_distance = float('inf')
    closest_pair = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            dist = calculate_distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (points[i], points[j])
    return closest_pair, min_distance
points = [(1, 2), (4, 5), (7, 8), (3, 1)]
closest_pair, min_distance = find_closest_pair(points)
print(f"Closest pair: {closest_pair[0]} - {closest_pair[1]}")
print(f"Minimum distance: {min_distance}")
#4.to slove travelling sales man person by the exhaustive search
import itertools
import math

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def tsp(cities):
    start_city = cities[0]
    shortest_distance = float('inf')
    shortest_path = []

    for perm in itertools.permutations(cities[1:]):
        current_path = [start_city] + list(perm) + [start_city]
        current_distance = sum(distance(current_path[i], current_path[i + 1]) for i in range(len(current_path) - 1))

        if current_distance < shortest_distance:
            shortest_distance = current_distance
            shortest_path = current_path

    return shortest_distance, shortest_path
cities_case1 = [(1, 2), (4, 5), (7, 1), (3, 6)]
cities_case2 = [(2, 4), (8, 1), (1, 7), (6, 3), (5, 9)]
result1 = tsp(cities_case1)
result2 = tsp(cities_case2)
print("Test Case 1:")
print("Shortest Distance:", result1[0])
print("Shortest Path:", result1[1])
print("\nTest Case 2:")
print("Shortest Distance:", result2[0])
print("Shortest Path:", result2[1])
#5. Exhaustive Search with Permutations
import itertools
def total_cost(assignment, cost_matrix):
    total = 0
    for worker, task in enumerate(assignment):
        total += cost_matrix[worker][task]
    return total
def assignment_problem(cost_matrix):
    num_workers = len(cost_matrix)
    workers = list(range(num_workers))
    optimal_assignment = None
    min_cost = float('inf')
    for perm in itertools.permutations(workers):
        current_cost = total_cost(perm, cost_matrix)
        if current_cost < min_cost:
            min_cost = current_cost
            optimal_assignment = perm
    return optimal_assignment, min_cost
cost_matrix_1 = [[3, 10, 7],
                  [8, 5, 12],
                  [4, 6, 9]]
optimal_assignment_1, min_cost_1 = assignment_problem(cost_matrix_1)
print(f"Optimal Assignment: {optimal_assignment_1}, Minimum Cost: {min_cost_1}")
cost_matrix_2 = [[15, 9, 4],
                  [8, 7, 18],
                  [6, 12, 11]]
optimal_assignment_2, min_cost_2 = assignment_problem(cost_matrix_2)
print(f"Optimal Assignment: {optimal_assignment_2}, Minimum Cost: {min_cost_2}")
# 6.0-1 Knapsack Problem Solutions
def total_value(items, values):
    return sum(values[i] for i in items)

def is_feasible(items, weights, capacity):
    total_weight = sum(weights[i] for i in items)
    return total_weight <= capacity

def knapsack(weights, values, capacity):
    n = len(weights)
    best_value = 0
    best_combination = []

    for i in range(1 << n):  # Iterate through all possible combinations
        selected_items = [j for j in range(n) if (i & (1 << j)) > 0]
        if is_feasible(selected_items, weights, capacity):
            current_value = total_value(selected_items, values)
            if current_value > best_value:
                best_value = current_value
                best_combination = selected_items

    return best_combination, best_value
weights1 = [2, 3, 1]
values1 = [4, 5, 3]
capacity1 = 4
result1 = knapsack(weights1, values1, capacity1)
print(f"Optimal Selection: {result1[0]}, Total Value: {result1[1]}")
weights2 = [1, 2, 3, 4]
values2 = [2, 4, 6, 3]
capacity2 = 6
result2 = knapsack(weights2, values2, capacity2)
print(f"Optimal Selection: {result2[0]}, Total Value: {result2[1]}")




