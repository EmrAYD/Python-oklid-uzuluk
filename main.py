# 1. Adım: Noktaların tanımlanması
points = [(1, 2), (4, 6), (7, 8), (2, 1)]

# 2. Adım: Öklid mesafesi için bir fonksiyon yazma
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# 3. Adım: Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# 4. Adım: Minimum mesafenin bulunması
min_distance = min(distances)
print(f'Minimum mesafe: {min_distance}')
