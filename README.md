# Data Science (MSAI339) Main Project

## Group Formation & Proposal

### 1. Team Name: *K-Mean Girls*

### 2. Team Members: *Nicole Birova, Jack Hanke, Daniel Plotkin, Hanna Zelis*

### 3. Project Title: *Common Cancer Classification via Gene Expression*

### 4. Project Description: 

Our decided dataset is the [TCGA-PANCAN](https://archive.ics.uci.edu/datasets?search=gene%20expression%20cancer%20RNA-Seq)** dataset, which is an $801$ sample, $20531$ feature dataset that seeks to predict the following $5$ types of cancers
- BRCA: Breast Cancer
- KIRC: Kidney renal clear cell carcinoma
- COAD: Colon adenocarcinoma
- LUAD: Lung adenocarcinoma
- PRAD: Prostate adenocarcinoma

** TCGA stands for The Cancer Genome Atlas 

** The dataset is a subset of the larger PANCAN dataset. 

We encode the cancer numerically as follows: 
```
encoding_dict = {
    'BRCA':0, 
    'KIRC':1, 
    'COAD':2, 
    'LUAD':3, 
    'PRAD':4
}
```

Papers that use this dataset:
- [This one](https://link.springer.com/article/10.1007/s41870-023-01688-8)

### 5. Data Source: Where you plan to get your data.

For setting up your project, [download](https://archive.ics.uci.edu/dataset/401/gene+expression+cancer+rna+seq) the data, then move the `data.csv` and `labels.csv` into the `data` directory.

### 6. Project Goals: What you hope to achieve, or what findings you expect with your project.

TODO
