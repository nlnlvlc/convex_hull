'''
Nilan Lovelace (@njl8879)
Computational Geometry, Fall 2024
Convex Hull: Graham's Scan Algorithm

Find the convex hull of a set of points using a Graham's Scan algorithm, O(nlogn)
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
    #seperate points into respective x, y values
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
def orientation(p, q, r):
    '''
    Identifies the direction of the hull between 3 points: colinear, clockwise, counterclockwise
    :param p: 
    :param q: 
    :param r: 
    :return: int representing orientation
    '''
    #finds the determinate
    orient = (p[0] * q[1] + q[0] * r[1] + r[0] * p[1]) - (p[1] * q[0] + q[1] * r[0] + r[1] * p[0])

    #if 0, the set of points is colinear: return 0
    if orient == 0:
        return 0
    #if < 0, the set of points is heading in a clockwise direction: return -1
    if orient < 0:
        return -1
    # set of points is heading in a counterclockwise direction: return 1
    else:
        return 1
def grahams(points):
    '''
    Performs the Graham Scan Algorithm on the set of points
    :param points: list[(x,y)] Set of points
    :return: list[(x,y)] Points making up the Convex Hull
    '''
    start = time.time()
    #finds lowest, leftmost point to use as starting point
    p0 = min(points, key=lambda p: (p[1],p[0]))
    #sort points by polar angle from starting point
    #if more than one point has the same polar angle, sort by distances to starting point
    points.sort(key=lambda p: (pa(p0,p), dist(p0, p)))
    
    #store points in hull
    hull = []
    
    for i in range(len(points)):
        #if there are at least 2 points in the hull and last two points and current point are not in a counterclockwise
        #direction, remove the last point in the hull
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], points[i]) != 1:
            hull.pop()
        hull.append(points[i])
    end = time.time()
    #return completed hull
    return hull
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
    #find conex hull
    hull = grahams(points)
    end = time.time()

    #write results to output file and print
    hullSize = len(hull)
    outputFile = open("grahamsOutput.txt", "w")
    print(hullSize)
    toWrite = [f"{hullSize}\n"]

    for point in hull:
        points = f"{point[0]} {point[1]}"
        print(points)
        toWrite.append(points +"\n")
    outputFile.writelines(toWrite)
    outputFile.close()

    print("The time of execution of above program is :",
          (end - start) * 10 ** 3, "ms")

if __name__ == '__main__':
    main()