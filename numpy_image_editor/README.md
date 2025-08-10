# Mini Image Editor Using Python, OpenCV & NumPy

## Project Overview

This project is a simple mini image editor built in Python that demonstrates practical usage of NumPy and OpenCV for image processing. It allows users to load an image, perform operations like grayscale conversion, brightness increase/decrease, and view the results—all through a modular command-line interface.

## Features

- Load and validate images using OpenCV
- Convert color images to grayscale manually using NumPy weighted sum
- Increase or decrease image brightness with user input
- Modular design with functions for easy extension
- Safe pixel value handling with NumPy’s `clip` to avoid overflow/underflow
- Interactive CLI to choose operations without opening GUI windows automatically

## Learning Journey

This project was part of my learning path in Python for AI and Machine Learning, focusing on:

- Understanding image representation as NumPy arrays
- Manipulating pixel data with NumPy for practical image edits
- Using OpenCV for image I/O and display
- Implementing modular code for maintainability and scalability
- Handling user inputs safely and interactively

## Technologies & Libraries

- Python 3.x
- OpenCV (`cv2`)
- NumPy

## How to Use

1. Clone the repo and navigate to the project folder.
2. Ensure you have Python 3 installed with OpenCV and NumPy:
   ```bash
   pip install opencv-python numpy
