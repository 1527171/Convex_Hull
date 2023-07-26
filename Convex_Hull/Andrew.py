def cross(p: list[int], q: list[int], r: list[int]) -> int:
    '''
    向量 ->a=q-p;向量 ->b=r-p
    如果满足->a * ->b > 0,则属于目前凸包的一个点
    否则需要反复对比之前已找到的点，不断移除，直到符合->a * ->b > 0
    '''
    return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])


def getConvexHull(points: list[list[int]]) -> list[list[int]]:
    points.sort()
    hull = []
    n = len(points)
    if n < 4:
        return points
    # 下半
    for i, p in enumerate(points):
        print(hull)
        while len(hull) > 1 and cross(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    # 上半
    m = len(hull)
    for i in range(n - 2, -1, -1):
        print(hull)
        while len(hull) > m and cross(hull[-2], hull[-1], points[i]) <= 0:
            hull.pop()
        hull.append(points[i])
    return hull


def triangle_area(x1, y1, x2, y2, x3, y3):
    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return area


def largestTriangleArea(points: list[list[int]]) -> float:
    Hull = getConvexHull(points)
    ans, n = 0, len(Hull)
    for i, p in enumerate(Hull):
        k = i + 2
        for j in range(i + 1, n - 1):
            q = Hull[j]
            while k + 1 < n:
                curArea = triangle_area(p[0], p[1], q[0], q[1], Hull[k][0], Hull[k][1])
                nextArea = triangle_area(p[0], p[1], q[0], q[1], Hull[k + 1][0], Hull[k + 1][1])
                if curArea >= nextArea:
                    break
            ans = max(ans,triangle_area(p[0], p[1], q[0], q[1], Hull[k][0], Hull[k][1]))
    return ans


if __name__ == "__main__":
    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    print(largestTriangleArea(points))
