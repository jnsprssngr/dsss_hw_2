import numpy as np
import matplotlib.pyplot as plt
import flammkuchen

# Function to calculate IoU score
def calculate_iou(rect1, rect2):
    """
    Calculate the Intersection over Union (IoU) score between two rectangles.
    rect1, rect2: Tuples representing (x_coordinate, y_coordinate, width, height).
    """
    # Extract coordinates and dimensions
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2

    # Calculate the (x, y) coordinates of the intersection rectangle
    x_max1 = max(x1, x2)
    y_max1 = max(y1, y2)
    x_min2 = min(x1 + w1, x2 + w2)
    y_min2 = min(y1 + h1, y2 + h2)

    # Calculate intersection area
    intersection_width = max(0, x_min2 - x_max1)
    intersection_height = max(0, y_min2 - y_max1)
    intersection = intersection_width * intersection_height

    # Calculate union area
    area1 = w1 * h1
    area2 = w2 * h2
    union = area1 + area2 - intersection

    # Avoid division by zero
    if union == 0:
        return 0.0

    # IoU score
    return intersection / union

# Load rectangles data from the file
rectangles_file_path = "rectangles_dsss.sec"
data = flammkuchen.load(rectangles_file_path)

ground_truth = data['ground_truth']
predicted = data['predicted']

# Ensure both lists have the same length
assert len(ground_truth) == len(predicted), "Mismatch in ground truth and predicted rectangles!"

# Calculate IoU scores
iou_scores = [calculate_iou(gt, pr) for gt, pr in zip(ground_truth, predicted)]

# Plot IoU scores in a histogram
plt.figure(figsize=(10, 6))
plt.hist(iou_scores, bins=30, edgecolor='black', alpha=0.7)
plt.title("Distribution of IoU scores")
plt.xlabel("IoU")
plt.ylabel("Number of rectangles")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("iou_scores_histogram.png")
plt.show()

# Save the IoU scores for review
np.save("iou_scores.npy", iou_scores)

