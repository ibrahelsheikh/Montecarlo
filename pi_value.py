import random
import time

def main():
    global total
    total = 0
    global inside
    inside = 0

    while True:
        x = random.random()
        y = random.random()

        total = total + 1

        if x ** 2 + y ** 2 <= 1:
            inside = inside + 1
            print(x, y, total, inside)

        # area from monte carlo
        area_of_circle = inside / total
        area_of_square = 1

        # area of circle from math Area = pi * r^2
        pi = 4 * area_of_circle / area_of_square

        print(pi)
        #time.sleep(0.01)

if __name__ == '__main__':
    main()
