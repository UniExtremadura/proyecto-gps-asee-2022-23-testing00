import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    rng = np.random.default_rng()
    rand_x = rng.normal(size=150)
    rand_y = rng.normal(size=150)
    plt.scatter(rand_x, rand_y)
    plt.show()