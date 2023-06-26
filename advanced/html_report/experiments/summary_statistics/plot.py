# ========================================
# FileName: plot.py
# Date: 21 juin 2023 - 12:51
# Author: Ammar Mian
# Email: ammar.mian@univ-smb.fr
# GitHub: https://github.com/ammarmian
# Brief: Plot summary statistics of
#        IRIS dataset
# =========================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os
import pickle

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Plot summary statistics of IRIS dataset')
    parser.add_argument('--storage_path', type=str,
                        help='Path to the storage folder',
                        required=True)
    args = parser.parse_args()

    # Load summary.csv
    summary = pd.read_csv(os.path.join(args.storage_path, 'summary.csv'))
    print(summary)

    # Load histogram.pkl
    with open(os.path.join(args.storage_path, 'histogram.pkl'), 'rb') as f:
        histogram = pickle.load(f)

    # Plot histograms
    for feature in histogram.keys():
        hist, bin, width, center = histogram[feature]
        plt.figure()
        plt.bar(center, hist, align='center', width=width)
        plt.title(f'Histogram of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Count')

    plt.show()



