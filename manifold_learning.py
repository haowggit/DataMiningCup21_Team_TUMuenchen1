import numpy as np
import os
from collections import OrderedDict
from functools import partial
from time import time
import numpy as np
import scipy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter
from sklearn import manifold
from sklearn.decomposition import TruncatedSVD


# Next line to silence pyflakes. This import is needed.
Axes3D

# sparse_data = scipy.sparse.load_npz('OHE_sparse_matrix.npz')
#
# svd = TruncatedSVD(n_components= 1200, n_iter= 10, random_state=42, algorithm= 'randomized')
# svd.fit(sparse_data)
# dense_data = sparse_data
# print(svd.explained_variance_ratio_.sum())
# X = svd.fit_transform(sparse_data)
X = np.load('svd_dataset_2500.npy')

# fig = plot_2dhist(['80000038'], 'matsum', 'internal_energy', curves_ndarray, stats_plot = True, save = False)

n_neighbors = 10
n_components = 3

# Create figure
fig = plt.figure(figsize=(15, 8))
fig.suptitle("Manifold Learning", fontsize=14)

# Add 3d scatter plot
# ax = fig.add_subplot(251, projection='3d')
# ax.scatter(t, X, cmap=plt.cm.Spectral)
# ax.view_init(4, -72)

# Set-up manifold methods

# LLE = partial(manifold.LocallyLinearEmbedding,
#               n_neighbors, n_components, eigen_solver='auto')
methods = OrderedDict()
# methods['LLE'] = LLE(method='standard')
# methods['LTSA'] = LLE(method='ltsa')
# methods['Hessian LLE'] = LLE(method='hessian')
# methods['Modified LLE'] = LLE(method='modified')
# methods['Isomap'] = manifold.Isomap(n_neighbors, n_components)
# methods['MDS'] = manifold.MDS(n_components, max_iter=100, n_init=1)
# methods['SE'] = manifold.SpectralEmbedding(n_components=n_components,
#                                            n_neighbors=n_neighbors)
methods['t-SNE'] = manifold.TSNE(n_components=n_components, init='random',
                                 random_state=0)
print('start')
# Plot results
for i, (label, method) in enumerate(methods.items()):
    t0 = time()
    Y = method.fit_transform(X)
    t1 = time()
    print("%s: %.2g sec" % (label, t1 - t0))
    # ax = fig.add_subplot(2, 5, 2 + i + (i > 3))
    ax = fig.add_subplot( projection='3d')

    ax.scatter(Y[:, 0], Y[:, 1], Y[:, 2], s = 1, cmap=plt.cm.Spectral)
    ax.set_title("%s (%.2g sec)" % (label, t1 - t0))
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_formatter(NullFormatter())
    ax.axis('tight')


