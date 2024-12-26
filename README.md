# PConvex Hull
This project finds the minimum number of points needed to encampsulate all points in a set within a convex hull.
The following programs due so using two algorithms: 
1. A brute force algorithm to compare all points to each other and identify if there
points to the left and/or the right of the line created. This algorithm has a time complexity of O(n^3).

2. The Graham's Scam algorithm to find the lowest point within a set of points, calculates and
sorts by the distance and polar angle between the lowest point and all other points, the evaluates the orientation new
points to the existing hull. This algorithm has a time complexity of O(nlogn).

## Language & Libraries

Both programs were built using Python3, and both make use of the math module. If you use the optional ``point_gen.py``
file, the random module is used.

## Run the Brute Force Convex Hall Program

The program can be ran with ``python3 brute_hull.py``

When prompted, the program accepts a txt filename as a single input. The first line contains n, the number of points in the 
set, followed by n number of lines containing a pair of numbers, separated by a single space, representing n points.

Once the program has finished execution, it will produce a txt file following the same format as the input file, 
displaying n, the number of points along the hull, on the first line, followed by n number of points, in 
counterclockwise order

## Run the Graham's Scan Convex Null Program

The program can be ran with ``python3 grahams.py``

When prompted, the program accepts a txt filename as a single input. The first line contains n, the number of points in the 
set, followed by n number of lines containing a pair of numbers, separated by a single space, representing n points.

Once the program has finished execution, it will produce a txt file following the same format as the input file, 
displaying n, the number of points along the hull, on the first line, followed by n number of points, in 
counterclockwise order


## Sample Points
Random points can be generated using ``python3 point_gen.py``. You will be prompted to enter the number of desired 
points you want generated. The sample points will be saved to ``examplePoints.txt`` in the proper format.
