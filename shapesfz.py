import asyncio
import random
import matplotlib.pyplot as plt
import numpy as np

# Define shapes and their drawing functions
def draw_circle(ax, color):
    circle = plt.Circle((random.uniform(0.1, 0.9), random.uniform(0.1, 0.9)), 0.1, color=color)
    ax.add_artist(circle)

def draw_square(ax, color):
    square = plt.Rectangle((random.uniform(0.1, 0.5), random.uniform(0.1, 0.5)), 0.2, 0.2, color=color)
    ax.add_artist(square)

def draw_triangle(ax, color):
    triangle = plt.Polygon([(random.uniform(0.1, 0.5), random.uniform(0.1, 0.5)),
                             (random.uniform(0.1, 0.5), random.uniform(0.5, 0.9)),
                             (random.uniform(0.5, 0.9), random.uniform(0.3, 0.7))],
                            color=color)
    ax.add_artist(triangle)

async def generate_image():
    shapes = ['circle', 'square', 'triangle']
    colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']

    fig, ax = plt.subplots()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    for _ in range(random.randint(1, 5)):  # Generate 1 to 5 shapes
        shape = random.choice(shapes)
        color = random.choice(colors)
        if shape == 'circle':
            draw_circle(ax, color)
        elif shape == 'square':
            draw_square(ax, color)
        elif shape == 'triangle':
            draw_triangle(ax, color)

    plt.axis('off')
    plt.savefig('shapes.png')
    plt.close(fig)

async def main():
    while True:
        await generate_image()
        await asyncio.sleep(5)  # Wait for 5 seconds before generating the next image

if __name__ == '__main__':
    asyncio.run(main())
