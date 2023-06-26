# ========================================
# FileName: compute.py
# Date: 21 juin 2023 - 12:45
# Author: Ammar Mian
# Email: ammar.mian@univ-smb.fr
# GitHub: https://github.com/ammarmian
# Brief: Compute summary statistics for 
#        IRIS dataset
# =========================================

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import argparse
import os
import pickle
import matplotlib

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Compute summary statistics for IRIS dataset')
    parser.add_argument('--storage_path', type=str,
                        help='Path to store the summary statistics',
                        required=True)
    args = parser.parse_args()

    # Print the simulation
    print("Compute summary statistics for IRIS dataset")

    # Load the dataset
    iris = load_iris()

    # Create a dataframe
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target

    # Compute summary statistics
    summary = df.describe()
    print(summary)

    # Compute histogram for each feature
    histogram = {}
    for feature in iris.feature_names:
        hist, bins = np.histogram(df[feature], bins=10)
        width = 0.7 * (bins[1] - bins[0])
        center = (bins[:-1] + bins[1:]) / 2
        histogram[feature] = (hist, bins, width, center)

    # Save the summary statistics
    summary.to_csv(os.path.join(args.storage_path, 'summary.csv'), index=False)

    # Save the histogram
    with open(os.path.join(args.storage_path, 'histogram.pkl'), 'wb') as f:
        pickle.dump(histogram, f)
