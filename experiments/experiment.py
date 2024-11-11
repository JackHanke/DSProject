from models import * # bring in models


# Metrics for Evaluation:
#   F-1 Score: Balances Precision & Recall 
#       Make sure that we account for class imbalance
#       Ensure that both false positives and false negatives are minimized
#   AUC-ROC
#       High AUC-ROC would indicate strong discrimination ability

# Feature importance:
#   Tree Based: XGBoost (built-in feature importance) or LightGBM (allows us to print)
#   SHAP Values: allow us to gain more detailed insights
#       Which specific genes are driving the prediction for each cancer type?
#       How do gene expression levels of individual patients contribute to predicted class?
#       Which genes are consistently important across all samples?

# Additional Analysis: 
#   Misclassification analysis, additional visualization techniques, multicollinearity, etc.

if __name__ == '__main__':
    pass
