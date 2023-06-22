# ========================================
# FileName: plot.py
# Date: 21 juin 2023 - 12:51
# Author: Ammar Mian
# Email: ammar.mian@univ-smb.fr
# GitHub: https://github.com/ammarmian
# Brief: Export histogram of each feature of
#        the IRIS dataset to LaTeX code
# =========================================

import argparse
import os
import pickle
import plotly.express as px

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
        fig = px.bar(x=center, y=hist)
        fig.update_layout(
            xaxis_title=feature,
            yaxis_title='Count',
            bargap=0.1,  # gap between bars of adjacent location coordinates
            bargroupgap=0.1  # gap between bars of the same location coordinate
        )
        feature_str = feature.replace(' ', '_')
        path_to_save = os.path.join(args.storage_path,
                                    f'histogram_{feature_str}.html')
        fig.write_html(path_to_save)
