from matplotlib import pyplot as plt
import matplotlib.animation
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
from math import *
import numpy as np
import pandas as pd
from tqdm import tqdm
import argparse

def drop_wave_function(x):
    # sphere_function with random center
    center = np.random.randint(-10, 10, 1)
    s = sum([(i-center[0])**2 for i in x])

    # drop_wave_function
    rtn = -(1 + cos(12*sqrt(s)))/(0.5*s + 2)

    # limit max depth
    if rtn < -0.2:
        rtn = -0.2

    return rtn*1275

def generateZ(function, lb, ub, sr=False):

    side = np.linspace(lb, ub, 45)
    X, Y = np.meshgrid(side, side)
    zs = np.array([function([x, y]) for x, y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    if sr:
        plot(X, Y, Z, lb, ub)
    return Z
    

def plot(X, Y, Z, lb, ub):

    fig = plt.figure()

    ax = Axes3D(fig)
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='inferno',
                           linewidth=0, antialiased=False, alpha=0.5)
    ax.set_xlim(lb, ub)
    ax.set_ylim(lb, ub)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)

    #figname = 'render/scale{}.jpg'.format(ub)
    #plt.savefig(figname)
    plt.show()

def main(sr):
    Z = []
    L = []

    for i in tqdm(range(2000)):
        scale = np.random.randint(10,42)
        Z += [ generateZ(drop_wave_function, -scale, scale, sr) ]
        label = 0
        L += [label] 
    for i in tqdm(range(2000)):
        scale = np.random.randint(42,77)
        Z += [ generateZ(drop_wave_function, -scale, scale, sr) ]
        label = 1
        L += [label] 
    for i in tqdm(range(2000)):
        scale = np.random.randint(76,110)
        Z += [ generateZ(drop_wave_function, -scale, scale, sr) ]
        label = 2
        L += [label] 

    Z = np.array(Z)
    L = np.array(L)
    #print(Z.shape)
    np.save('deep_Z_6000.npy', Z)
    #print(L.shape)
    np.save('deep_L_6000.npy', L)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--render',
        help='render damage data or not',
        type=int,
        dest='render',
        default=0,
    )
    args = parser.parse_args()
    sr = bool(args.render)
    main(sr)