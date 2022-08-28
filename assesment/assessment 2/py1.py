def maxArea(a, Len):
    area = 0
    for i in range(Len):
        for j in range(i + 1, Len):
            area = max(area, min(a[j], a[i]) * (j - i))
    return area


arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
length = len(arr)
print(maxArea(arr, length))
