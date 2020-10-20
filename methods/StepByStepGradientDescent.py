import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

sys.path.append(os.path.abspath('./functions'))

import Ackley

arrAckley = {"f": Ackley.f, "dfdx": Ackley.dfdx, "dfdy": Ackley.dfdy}

arrFunc = {"Ackley": arrAckley}

def optimization(func, x, y, eps, step, coef):
    # step == крок
    # coef == коефіцієнт дроблення

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
        
        if module < eps:
            break
        
        while True:
            x_1 = x - step * dfdx
            y_1 = x - step * dfdy

            if (func["f"](x, y) - func["f"](x_1, y_1)) >= 0.5 * step * (module ** 2):
                x = x_1
                y = y_1
                break

            step = coef * step

        print(x, y)

        ax.scatter(x, y, func["f"](x, y), c = "red")

        fig.canvas.draw()
        fig.canvas.flush_events()

    plt.ioff()  # выключение интерактивного режима отображения графиков

    print(x, y)
    ax.scatter(x, y, func["f"](x, y), c = "blue")
    plt.show()