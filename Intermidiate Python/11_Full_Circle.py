import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    input_radius = float(input('Enter the radius of the circle: '))
    area = calculate_circle_area(input_radius)
    print(f' Area of the circle: {area:.2f}')