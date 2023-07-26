def triangle_area(x1, y1, x2, y2, x3, y3):
    area = 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
    return area


def largestTriangleArea(points:list[list[int]]) -> float:
    res = 0
    for i in range(0, len(points)-2):
        for j in range(i+1, len(points)-1):
            for k in range(j+1, len(points)):
                res = max(res, triangle_area(points[i][0],points[i][1],points[j][0],points[j][1],points[k][0],points[k][1]))
    return res

if __name__=="__main__":
    points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    print(largestTriangleArea(points))