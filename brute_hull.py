'''
Nilan Lovelace (@njl8879)
Computational Geometry, Fall 2024
Convex Hull: Brute Force Algorithm

Find the convex hull of a set of points using a brute force algorithm, O(n^3)
'''
import math
import time

def pa(p1, p2):
    '''
    Finds the polar angle between points
    :param p1: list[int]: Starting point (x, y)
    :param p2: list[int]: point being measured (x, y)
    :return: polar angle between the plane p1 lies on and the angle of the line between p1 and p2
    '''
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]

    if y1 == y2:
        return -math.pi
    dy = y1 - y2
    dx = x1 - x2

    return math.atan2(dy, dx)
def dist(p1, p2):
    '''
    Finds Euclidean distance between two points
    :param p1: list[int] First Point
    :param p2: list[int] Second point
    :return: Euclidean distance
    '''
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]

    return math.sqrt((y2-y1)**2 + (x2 - x1)**2)
def _det(p, q, r):
    '''
    Finds determinant of set of points to determine where r sits in relation to p and q
    :param p:
    :param q:
    :param r:
    :return:
    '''
    det = (p[0] * q[1] + q[0] * r[1] + r[0] * p[1]) - (p[1] * q[0] + q[1] * r[0] + r[1] * p[0])

    if det < 0:
        return -1
    if det == 0:
        return 0
    else:
        return 1
def brute(points):
    '''
        Performs the Brute Force Algorithm on the set of points
        :param points: list[(x,y)] Set of points
        :return: list[(x,y)] Points making up the Convex Hull
        '''
    #stores points in hull
    hull = []

    points = sorted(points)
    n = len(points)

    for i in range(n-1):
        for j in range(i+1, n):
            p = points[i]
            q = points[j]
            #does point r sit left to points p and q?
            left = False
            #does point r sit right to points p and q
            right = False
            #include points p and q into hull?
            include = True
            for k in range(n): #check where all points sit in relation to points p and q
                if k not in {i, j}:
                    r = points[k]
                    #finds if point r sits left or right of p and q
                    det_r = _det(p, q, r)

                    if det_r == 1:
                        left = True
                    elif det_r == -1:
                        right = True
                    elif r < p or r > q:
                        include = False
                        break
                if left and right:
                    #if points are on the left and right of p and q
                    #don't include point in hull
                    include = False
                    break
            if include:
                hull.append(tuple(p))
                hull.append(tuple(q))
    # return completed hull
    return (hull)
def main():
    # read n and points from file
    points = []

    inputFile = input("Type filename: ")
    inputFile = open(inputFile, "r+")
    lines = inputFile.readlines()
    inputFile.close()

    for line in lines:
        line.strip("\n")

    n = int(lines[0])

    for num in range(1, n + 1):
        point = lines[num]
        pair = point.split(" ")
        point_pair = [eval(x) for x in pair]
        points.append(point_pair)

    start = time.time()
    #find convex hull
    hull = set(brute(points))
    end = time.time()

    #sort convex hull points counterclockwise
    lowest = min(hull, key=lambda x: (x[1], x[0]))
    hull = sorted(hull, key=lambda p: (pa(lowest, p), dist(lowest, p)))

    # write results to output file and print
    hullSize = len(hull)
    outputFile = open("bruteOutput.txt", "w")

    print(hullSize)
    toWrite = [f"{hullSize}\n"]

    for point in hull:
        points = f"{point[0]} {point[1]}"
        print(points)
        toWrite.append(points + "\n")
    outputFile.writelines(toWrite)
    outputFile.close()

    print("The time of execution of above program is :",
          (end - start) * 10 ** 3, "ms")

if __name__ == '__main__':
    main()

