# Data Science (MSAI339) Main Project
## Common Cancer Classification via Gene Expression
A project to predict types of cancers associated with genomic data. 

### The K-Mean Girls: Nicole Birova, Jack Hanke, Daniel Plotkin, Hanna Zelis*

## Project Setup:

> Note: All scripts must be ran from the root "project" directory.

1. Create venv:

```bash
python -m venv venv
```
This should only be ran once.

2. Activate venv:
```bash
source venv/bin/activate
```
This should be ran everytime before you start writing/running any code.

3. Install packages:
```bash
pip install -r requirements.txt
```

4. Download the raw data at [this link](https://archive.ics.uci.edu/dataset/401/gene+expression+cancer+rna+seq). Move the downloaded file (`gene+expression+cancer+rna+seq.zip`) to the `data` directory in the root of the project directory. 

```bash
cd data && ./create_data.sh && cd ..
```

5. View the exploratory data analysis by running through the Jupyter Notebook called `eda.ipynb`. This file shows the analysis conducted to write a representative data preprocessor. 


6. TODO `main.ipynb`

