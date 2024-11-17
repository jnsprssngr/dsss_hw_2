import matplotlib.pyplot as plt
import numpy as np
import cv2

# Load the provided "leaves.jpg" image
leaves_image_path = "leaves.jpg"
leaves_image = cv2.imread(leaves_image_path)
leaves_image_rgb = cv2.cvtColor(leaves_image, cv2.COLOR_BGR2RGB)

# Conversion methods to grayscale
def lightness_method(img):
    max_rgb = np.max(img, axis=2)
    print(max_rgb)
    min_rgb = np.min(img, axis=2)
    print(min_rgb)
    return np.mean([max_rgb,min_rgb],axis=0).astype(np.uint8)
    #return ((max_rgb+min_rgb)/2).astype(np.uint8)
def average_method(img):
    return np.mean(img, axis=2).astype(np.uint8)

def luminosity_method(img):
    return (0.2989 * img[:, :, 0] + 0.5870 * img[:, :, 1] + 0.1140 * img[:, :, 2]).astype(np.uint8)

# Convert to grayscale using each method
lightness_gray = lightness_method(leaves_image_rgb)
average_gray = average_method(leaves_image_rgb)
luminosity_gray = luminosity_method(leaves_image_rgb)

# Plotting the original image and the grayscale variations
fig, axs = plt.subplots(1, 4, figsize=(20, 10))
axs[0].imshow(leaves_image_rgb)
axs[0].set_title("Original Image")
axs[0].axis('off')

axs[1].imshow(lightness_gray, cmap='gray')
axs[1].set_title("Lightness Method")
axs[1].axis('off')

axs[2].imshow(average_gray, cmap='gray')
axs[2].set_title("Average Method")
axs[2].axis('off')

axs[3].imshow(luminosity_gray, cmap='gray')
axs[3].set_title("Luminosity Method")
axs[3].axis('off')

plt.tight_layout()
plt.show()