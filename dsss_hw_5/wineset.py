import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap.umap_ as umap
from sklearn.preprocessing import StandardScaler

# Load the dataset
file_path = 'winequality-red.csv'
data = pd.read_csv(file_path)

# Separate features and target
features = data.drop(columns=['quality'])
target = data['quality']

# Standardize the features
scaler = StandardScaler()
features_standardized = scaler.fit_transform(features)

# Convert the features_standardized array back into a DataFrame with column names
standardized_df = pd.DataFrame(features_standardized)

# Export to Excel
#standardized_df.to_excel('standardized_wine_data.xlsx', index=False)

# ---- Dimensionality Reduction ----

# PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(features_standardized)

# t-SNE
tsne = TSNE(n_components=2, random_state=42, perplexity=50)
tsne_result = tsne.fit_transform(features_standardized)

# UMAP
umap_model = umap.UMAP(n_neighbors=15, random_state=42)
umap_result = umap_model.fit_transform(features_standardized)

def plot_2d_projection(data, labels, title):
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', alpha=0.7)
    plt.colorbar(scatter, label='Quality')
    plt.title(title)
    plt.xlabel('PC1')
    plt.ylabel('PC 2')
    #plt.grid(True)
    plt.show()

# Generate the plots
plot_2d_projection(pca_result, target, 'PCA Projection - features standardized')
plot_2d_projection(tsne_result, target, 't-SNE Projection - features standardized')
plot_2d_projection(umap_result, target, 'UMAP Projection - features standardized')

from scipy.stats import spearmanr

# Hypothesis: Residual sugar contributes to wine quality
# Null hypothesis (H0): Residual sugar does not significantly affect wine quality

# Select the feature for hypothesis testing
feature = 'residual sugar'

# Spearman correlation test
correlation, p_value = spearmanr(data[feature], target)

print(f"Spearman Correlation: {correlation:.3f}")
print(f"P-value: {p_value:.3f}")

# Interpretation
if p_value < 0.05:
    print("Reject the null hypothesis: Residual sugar significantly contributes to wine quality.")
else:
    print("Fail to reject the null hypothesis: No significant contribution from residual sugar to wine quality.")
