import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE


data = pd.read_parquet('data.parquet')
labels = pd.read_parquet('labels.parquet')

encoding_dict = {
    'BRCA': 0,
    'KIRC': 1,
    'COAD': 2,
    'LUAD': 3,
    'PRAD': 4
}

labels['Class'] = labels['Class'].map(encoding_dict)

data.rename(columns={'Unnamed: 0': 'sample_id'}, inplace=True)
labels.rename(columns={'Unnamed: 0': 'sample_id'}, inplace=True)

merged_data = pd.merge(data, labels, on='sample_id')

print(merged_data.head())

data = data.drop(columns=['sample_id'])
labels = labels.drop(columns=['sample_id'])


### Found no missing values in data

### Adding Visualizations :

# label distribution
plt.figure(figsize=(8, 6))
sns.countplot(x=labels['Class'], palette='viridis')
plt.title('Distribution of Cancer Types')
plt.xlabel('Cancer Type (Encoded)')
plt.ylabel('Count')
plt.xticks(ticks=[0, 1, 2, 3, 4], labels=['BRCA', 'KIRC', 'COAD', 'LUAD', 'PRAD'])
plt.show()

# t-SNE results
tsne = TSNE(n_components=2, random_state=42, perplexity=30)
data_tsne = tsne.fit_transform(data)

plt.figure(figsize=(8, 6))
sns.scatterplot(x=data_tsne[:, 0], y=data_tsne[:, 1], hue=labels['Class'], palette='viridis', legend='full')
plt.title('t-SNE Visualization')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.legend(title='Cancer Type', labels=['BRCA', 'KIRC', 'COAD', 'LUAD', 'PRAD'])
plt.show()

