# ========================================
# FileName: plot.py
# Date: 21 juin 2023 - 12:51
# Author: Ammar Mian
# Email: ammar.mian@univ-smb.fr
# GitHub: https://github.com/ammarmian
# Brief: Export histogram of each feature of
#        the IRIS dataset to LaTeX code
# =========================================

import matplotlib.pyplot as plt
import argparse
import os
import pickle
import tikzplotlib

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
            description="Export histogram of each feature of the "
            "IRIS dataset to LaTeX code")
    parser.add_argument('--storage_path', type=str,
                        help='Path to the storage folder',
                        required=True)
    args = parser.parse_args()

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
        feature_str = feature.replace(' ', '_')

        plt.savefig(os.path.join(args.storage_path,
                                 f'histogram_{feature_str}.png'))
        path_to_save = os.path.join(args.storage_path,
                                    f'histogram_{feature_str}.tex')
        print(f'Exporting histogram of {feature} to '
              f'{path_to_save}')
        tikzplotlib.save(path_to_save)
