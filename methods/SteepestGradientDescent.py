import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

sys.path.append(os.path.abspath('./functions'))

import Ackley

arrAckley = {"f": Ackley.f, "dfdx": Ackley.dfdx, "dfdy": Ackley.dfdy}

arrFunc = {"Ackley": arrAckley}

def optimization(func, x, y, eps):
    func = arrFunc[func]

    x_plt = np.arange(-30.0, 30.0, 0.1)
    y_plt = np.arange(-30.0, 30.0, 0.1)

    f_plt = np.array([[func["f"](x, y) for x in x_plt] for y in y_plt])

    plt.ion()
    fig = plt.figure()
    ax = Axes3D(fig)

    ox, oy = np.meshgrid(x_plt, y_plt)
    ax.plot_surface(ox, oy, f_plt, color="y", alpha=0.5)

    ax.set_xlabel("a")
    ax.set_ylabel("b")
    ax.set_zlabel("f")

    point = ax.scatter(x, y, func["f"](x, y), c="red")

    while True:
        dfdx = func["dfdx"](x, y)
        dfdy = func["dfdy"](x, y)

        module = np.sqrt(dfdx ** 2 + dfdy ** 2)

        # print(x, y)
        # print(dfdx, dfdy)

        if module < eps:
            break

        steps = []
        func_values = []

        for i in np.arange(0.01, 10.01, 0.01):
            steps.append(i)
            func_values.append(func["f"](x - i * dfdx, y - i * dfdy))

        step = steps[func_values.index(min(func_values))]

        x = x - step * dfdx
        y = y - step * dfdy

        ax.scatter(x, y, func["f"](x, y), c = "red")

        fig.canvas.draw()
        fig.canvas.flush_events()

    plt.ioff()

    print(x, y)
    ax.scatter(x, y, func["f"](x, y), c = "blue")
    plt.show()