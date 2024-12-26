'''
Nilan Lovelace (@njl8879)
Computational Geometry, Fall 2024
Convex Hull: Point Set Generator

Produces a set of points formatted to be used with brute_hull.py and grahams.py
'''
import random
def generate():
    return random.randint(-20, 20)
def main():
    n = int(input("Enter number of points: "))

    points = []

    for num in range(n):
        point = f"{generate()} {generate()}\n"
        points.append(point)

    toWrite = [str(n) +"\n"] + points
    outputFile = open("examplePoints.txt", "w")
    outputFile.writelines(toWrite)
    outputFile.close()

if __name__ == '__main__':
    main()