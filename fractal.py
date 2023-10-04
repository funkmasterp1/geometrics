import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for i in range(max_iter):
        if abs(z) > 2.0:
            return i
        z = z * z + c
    return max_iter

def create_mandelbrot(width, height, zoom, x_off, y_off, max_iter):
    img = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            zx = 1.5 * (x - width / 2) / (0.5 * zoom * width) + x_off
            zy = 1.0 * (y - height / 2) / (0.5 * zoom * height) + y_off
            c = complex(zx, zy)
            img[x, y] = mandelbrot(c, max_iter)
    return img

# Define the parameters for the Mandelbrot set
width = 800
height = 800
zoom = 1.0
x_offset = 0.0
y_offset = 0.0
max_iterations = 100

# Generate the Mandelbrot set
fractal_img = create_mandelbrot(width, height, zoom, x_offset, y_offset, max_iterations)

# Display the fractal image
plt.imshow(fractal_img.T, cmap='hot', extent=[-2.0, 1.0, -1.5, 1.5])
plt.title('Mandelbrot Set')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()
