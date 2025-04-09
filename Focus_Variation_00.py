import numpy as np
import cv2
import matplotlib.pyplot as plt

# 1. Synthetischen Fokus-Stack erzeugen
def generate_synthetic_focus_stack(num_images=10, image_size=(200, 200)):
    h, w = image_size
    focus_stack = []
    for i in range(num_images):
        img = np.zeros((h, w), dtype=np.uint8)
        center = (w // 2, h // 2)
        radius = 30 + i * 2
        cv2.circle(img, center, radius, (255), -1)
        blurred = cv2.GaussianBlur(img, (0, 0), sigmaX=3.0 - i * 0.2)
        focus_stack.append(blurred)
    return focus_stack

# 2. Fokusmaß berechnen (Laplace)
def compute_focus_stack(images):
    h, w = images[0].shape
    num_images = len(images)
    focus_stack = np.zeros((num_images, h, w))

    for i, img in enumerate(images):
        lap = cv2.Laplacian(img, cv2.CV_64F)
        focus_stack[i] = np.abs(lap)

    focus_measure = np.max(focus_stack, axis=0)
    depth_map = np.argmax(focus_stack, axis=0)
    return focus_measure, depth_map

# 3. Ergebnisse anzeigen
def show_results_corrected(images, focus_measure, depth_map):
    num_images = len(images)
    fig, axes = plt.subplots(2, max(num_images, 2), figsize=(20, 5))

    for i in range(num_images):
        axes[0, i].imshow(images[i], cmap='gray')
        axes[0, i].set_title(f"Image {i}")
        axes[0, i].axis('off')

    axes[1, 0].imshow(focus_measure, cmap='gray')
    axes[1, 0].set_title("Focus Measure")
    axes[1, 0].axis('off')

    axes[1, 1].imshow(depth_map, cmap='viridis')
    axes[1, 1].set_title("Depth Map")
    axes[1, 1].axis('off')

    for j in range(2, num_images):
        axes[1, j].axis('off')

    plt.tight_layout()
    plt.show()

# 4. Hauptprogramm
if __name__ == "__main__":
    print("Erzeuge synthetischen Fokus-Stack...")
    synthetic_stack = generate_synthetic_focus_stack()

    print("Berechne Fokusmaß und Tiefenkarte...")
    focus_measure, depth_map = compute_focus_stack(synthetic_stack)

    print("Zeige Ergebnisse...")
    show_results_corrected(synthetic_stack, focus_measure, depth_map)
