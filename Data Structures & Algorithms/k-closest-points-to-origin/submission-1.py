import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        shortest_distance = float('inf')
        for point in points:
            x = point[0]
            y = point[1]
            distance = math.sqrt((x ** 2)+(y ** 2))
            result.append((distance, point))
        
        result.sort(key=lambda x: x[0])
        result = [p for _, p in result[:k]]
        return result