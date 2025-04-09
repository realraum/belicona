# belicona
Focus Variation 3 D Imaging

https://en.wikipedia.org/wiki/Focus_variation

Focus Variation Measurement is an image-based method for 3D surface measurement, primarily used in industrial metrology (e.g., with Alicona systems). It combines the advantages of optical microscopy with precise 3D acquisition based on focus shift. In Python, you can implement a simplified version using OpenCV and NumPy that creates a focus map and derives a depth map from it .

Here is a simple, functional approach using an image stack (e.g., multiple images of the same scene, each with a slightly different focus):

Basic idea
Load all Images.

Calculate a sharpness value (e.g., Laplace variance) per pixel per image.

For each pixel: Determine the image with the highest sharpness value → this image corresponds to the best focus → results in a depth map.



Notes:
The more images you have (e.g. 10–30 focus planes), the better the depth map will be.

For better results, you can use other focus metrics (e.g. Sobel, Brenner, etc.).

For professional applications, hardware-supported systems and calibration are necessary.

