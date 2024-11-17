import os
import random
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Directory path where the dataset is stored
dataset_path = 'Mini_BAGLS_dataset'

# Get all available image indices by scanning the directory
all_indices = [
    int(f.split('.')[0]) for f in os.listdir(dataset_path)
    if f.split('.')[0].isdigit()
]

# Select 4 random indices
selected_indices = random.sample(all_indices, 4)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes = axes.ravel()  # Flatten axes array for easy iteration

for i, idx in enumerate(selected_indices):
    # Load image
    image_path = os.path.join(dataset_path, f'{idx}.png')
    image = Image.open(image_path).convert('RGBA')

    # Load segmentation mask
    mask_path = os.path.join(dataset_path, f'{idx}_seg.png')
    mask = Image.open(mask_path).convert('L')

    # Create an overlay with the mask in a semi-transparent color
    mask_overlay = Image.new('RGBA', image.size, (255, 0, 0, 0))
    mask_overlay_np = np.array(mask_overlay)
    mask_np = np.array(mask)
    mask_overlay_np[mask_np > 0] = [255, 0, 0, 100]  # Red color with transparency
    mask_overlay = Image.fromarray(mask_overlay_np)

    # Composite the image and mask overlay
    combined_image = Image.alpha_composite(image, mask_overlay)

    # Load metadata and extract "Subject disorder status"
    meta_path = os.path.join(dataset_path, f'{idx}.meta')
    with open(meta_path, 'r') as f:
        metadata = f.read()
    disorder_status = "Unknown"
    for line in metadata.splitlines():
        if "Subject disorder status" in line:
            disorder_status = line.split(":")[-1].strip()
            break

    # Display the image with overlay
    axes[i].imshow(combined_image)
    axes[i].set_title(f'Image {idx}: {disorder_status}')
    axes[i].axis('off')

plt.tight_layout()
plt.show()

