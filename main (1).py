import math

def euclideanDistance(point1,point2):
    return math.sqrt((point1[0]-point2[0])**2+(point1[0]-point2[1])**2)

points = [(1,2),(2,3),(4,5),(9,8),(5,2)]
distances = []

for i in range(len(points)):
    for j in range(i+1,len(points)):
        distance = euclideanDistance(points[i],points[j])
        distances.append(distance)
print(distances)

minDistance = min(distances)
print("minimum distance ",minDistance)
