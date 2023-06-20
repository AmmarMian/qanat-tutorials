import numpy as np
import matplotlib.pyplot as plt
import argparse
import os

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--storage_path", type=str, required=True)
    args = parser.parse_args()

    results_path = os.path.join(args.storage_path, "results.npz")
    results = np.load(results_path)
    hist = results["hist"]
    bins = results["bins"]

    plt.bar(bins[:-1], hist, width=bins[1] - bins[0])
    plt.savefig(os.path.join(args.storage_path, "histogram.png"))
    plt.show()
