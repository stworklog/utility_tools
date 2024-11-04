import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def is_overlapping(center1, center2, radius):
    distance = np.sqrt((center1[0] - center2[0])**2 + (center1[1] - center2[1])**2)
    return distance < 2 * radius * 1.3

def generate_non_overlapping_center(existing_centers, radius):
    attempts = 0
    while True:
        attempts += 1
        if attempts > 1000:
            raise ValueError("Failed to generate a non-overlapping center after 1000 attempts")
        new_center = (random.random(), random.random())
        if all(not is_overlapping(new_center, center, radius) for center in existing_centers):
            return new_center

def generate_puzzle(num_arcs=50, num_circles = 1, arc_angle=300, image_size=(6, 6)):
    radius = 0.03

    fig, ax = plt.subplots(figsize=image_size)
    axis_min = 0 - radius * 2
    axis_max = 1 + radius * 2
    ax.set_xlim(axis_min, axis_max)
    ax.set_ylim(axis_min, axis_max)
    ax.set_aspect('equal')
    ax.axis('off')
    # draw a box around the figure
    ax.add_patch(plt.Rectangle((axis_min, axis_min), axis_max - axis_min, axis_max - axis_min, edgecolor='black', facecolor='none'))

    existing_centers = []

    # Generate arcs
    for _ in range(num_arcs):
        center = generate_non_overlapping_center(existing_centers, radius)
        existing_centers.append(center)
        start_angle = random.uniform(0, 360)
        end_angle = start_angle + arc_angle
        arc = Arc(center, 2 * radius, 2 * radius, angle=0, theta1=start_angle, theta2=end_angle, color='black')
        ax.add_patch(arc)

    # Generate one full circle, ensuring it doesn't overlap with arcs
    for _ in range(num_circles):
        center = generate_non_overlapping_center(existing_centers, radius)
        existing_centers.append(center)
        circle = plt.Circle(center, radius, edgecolor='black', facecolor='none')
        ax.add_patch(circle)

    plt.show()

def config_puzzle(look_for_letter = 'o', num_of_other_letters = 50, arc_angle=320):
    if look_for_letter == 'c':
        generate_puzzle(num_arcs=1, num_circles=num_of_other_letters, arc_angle=arc_angle)
    elif look_for_letter == 'o':
        generate_puzzle(num_arcs=num_of_other_letters, num_circles=1, arc_angle=arc_angle)
    return look_for_letter

if __name__ == "__main__":
    # time it
    import time
    start = time.time()
    config_puzzle('o', 100, arc_angle=320)
    end = time.time()
    print("Time taken: ", end - start)
