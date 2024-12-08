import numpy as np
import matplotlib.pyplot as plt
import albumentations as A
import cv2
import os

# Dataset folder paths
image_folder = "Mini_BAGLS_dataset"

# Seed for reproducibility
matriculation_number = 23310950
np.random.seed(matriculation_number)

# Filter out image and mask files
image_files = [f for f in os.listdir(image_folder) if f.endswith(".png") and not f.endswith("_seg.png")]
mask_files = [f for f in os.listdir(image_folder) if f.endswith("_seg.png")]

# Extract base IDs for comparison
image_ids = [os.path.splitext(f)[0] for f in image_files]
mask_ids = [os.path.splitext(f)[0].replace("_seg", "") for f in mask_files]

# Match valid image-mask pairs
valid_image_files = []
valid_mask_files = []
for img_id, img_file in zip(image_ids, image_files):
    if img_id in mask_ids:
        valid_image_files.append(img_file)
        valid_mask_files.append(img_id + "_seg.png")

# Check if there are valid pairs
if not valid_image_files:
    raise ValueError("No matching images and masks were found in the dataset!")

# Randomly select an image and its corresponding mask
random_index = np.random.choice(len(image_files))
selected_image_name = image_files[random_index]
selected_mask_name = selected_image_name.replace(".png", "_seg.png")

# Load the selected image and mask
selected_image_path = os.path.join(image_folder, selected_image_name)
selected_mask_path = os.path.join(image_folder, selected_mask_name)

image = cv2.imread(selected_image_path, cv2.IMREAD_COLOR)
mask = cv2.imread(selected_mask_path, cv2.IMREAD_GRAYSCALE)

# Display original image and mask
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(mask, cmap='gray')
plt.title("Original Mask")
plt.axis('off')

plt.savefig("original_image_and_mask.png")
plt.show()

# Define Albumentations augmentation pipeline
augmentations = [
    ("Vertical Flipped", A.VerticalFlip(p=1)),
    ("Horizontal Flipped", A.HorizontalFlip(p=1)),
    ("Random Rotated", A.Rotate(limit=45, p=1)),
    ("Transposed", A.Transpose(p=1))
]


# Apply augmentations and visualize
plt.figure(figsize=(15, 10))

for i, (aug_name, aug) in enumerate(augmentations, 1):
    augmented = aug(image=image, mask=mask)
    aug_image = augmented['image']
    aug_mask = augmented['mask']

    plt.subplot(2, len(augmentations), i)
    plt.imshow(cv2.cvtColor(aug_image, cv2.COLOR_BGR2RGB))
    plt.title(f"{aug_name} Image")
    plt.axis('off')

    plt.subplot(2, len(augmentations), i + len(augmentations))
    plt.imshow(aug_mask, cmap='gray')
    plt.title(f"{aug_name} Mask")
    plt.axis('off')

plt.savefig("augmented_images_and_masks.png")
plt.show()
