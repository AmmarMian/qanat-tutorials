import numpy as np
import argparse
import os

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--nbins", type=int, default=10)
    parser.add_argument("--storage_path", type=str, required=True)
    args = parser.parse_args()

    rng = np.random.RandomState(args.seed)
    data = rng.randn(1000)
    hist, bins = np.histogram(data, bins=args.nbins)

    results_path = os.path.join(args.storage_path, 'results.npz')
    np.savez(results_path, hist=hist, bins=bins)
