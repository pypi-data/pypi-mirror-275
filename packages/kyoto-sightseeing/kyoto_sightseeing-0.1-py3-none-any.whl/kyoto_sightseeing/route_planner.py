import itertools
import math
from kyoto_sightseeing.coordinates import get_coordinates

def calculate_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    R = 6371  # 地球の半径（km）
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def plan_route(start, end, waypoints, num_days, accommodations):
    routes = []
    
    start_coords = get_coordinates(start)
    end_coords = get_coordinates(end)
    waypoints_coords = [get_coordinates(place) for place in waypoints]
    accommodations_coords = [get_coordinates(place) for place in accommodations]
    
    def split_list(lst, n):
        k, m = divmod(len(lst), n)
        return [lst[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)]

    permuted_points = list(itertools.permutations(waypoints_coords))
    min_distance = float('inf')
    best_route = None
    
    for perm in permuted_points:
        full_route = [start_coords] + list(perm)
        segments = split_list(full_route, num_days)
        
        total_distance = 0
        for segment in segments:
            for i in range(len(segment) - 1):
                total_distance += calculate_distance(segment[i], segment[i + 1])
        
        if total_distance < min_distance:
            min_distance = total_distance
            best_route = segments

    for i, segment in enumerate(best_route):
        if i < len(accommodations_coords):
            segment.append(accommodations_coords[i])
        if i < num_days - 1:
            next_start = accommodations_coords[i]
            best_route[i + 1].insert(0, next_start)
        routes.append(segment)

    # Ensure the end point is added only to the last day
    if len(routes) == num_days:
        routes[-1].append(end_coords)

    return routes
