import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from mpl_toolkits.mplot3d import Axes3D


myfont = fm.FontProperties(fname=r"C:\\Windows\\Fonts\\simsun.ttc", size=14)
matplotlib.rcParams["axes.unicode_minus"] = False


# 动态曲线
def simple_plot():
    # 生成画布
    plt.figure(figsize=(8, 6), dpi=80)
    # 打开交互模式
    plt.ion()

    for index in range(100):
        # 清除原有图像
        plt.cla()

        plt.title("动态曲线图", fontproperties=myfont)
        plt.grid(True)

        x = np.linspace(-np.pi + 0.1*index, np.pi + 0.1*index, 256, endpoint=True)
        y_cos, y_sin = np.cos(x), np.sin(x)

        plt.xlabel("X轴", fontproperties=myfont)
        plt.xlim(-4 + 0.1*index, 4 + 0.1*index)
        plt.xticks(np.linspace(-4 + 0.*index, 4 + 0.1*index, 9, endpoint=True))

        plt.ylabel("Y轴", fontproperties=myfont)
        plt.ylim(-1.0, 1.0)
        plt.yticks(np.linspace(-1, 1, 9, endpoint=True))

        plt.plot(x, y_cos, "b--", linewidth=2.0, label="cos示例")
        plt.plot(x, y_sin, "g-", linewidth=2.0, label="sin示例")

        plt.legend(loc="upper left", prop=myfont, shadow=True)
        
        plt.pause(0.1)

    plt.ioff()

    plt.show()
    return
# simple_plot()


def scatter_plot():
    plt.ion()

    for index in range(50):
        plt.title("动态散点图", fontproperties=myfont)
        plt.grid(True)

        point_count = 5
        x_index = np.random.random(point_count)
        y_index = np.random.random(point_count)

        color_list = np.random.random(point_count)
        scale_list = np.random.random(point_count)

        plt.scatter(x_index, y_index, s=scale_list, c=color_list, marker="o")

        plt.pause(0.2)

    plt.ioff()

    plt.show()
    return
# scatter_plot()


# 动态三维散点图
def three_dimension_scatter():
    fig = plt.figure()

    plt.ion()

    for index in range(50):
        fig.clf()

        fig.suptitle("三维动态散点图", fontproperties=myfont)

        point_count = 100
        x = np.random.random(point_count)
        y = np.random.random(point_count)
        z = np.random.random(point_count)
        color = np.random.random(point_count)
        scale = np.random.random(point_count) * 100

        ax = fig.add_subplot(111, projection="3d")

        ax.scatter(x, y, z, s=scale, c=color, marker=".")
        
        ax.set_xlabel("X Label")
        ax.set_ylabel("Y Label")
        ax.set_zlabel("Z Label")
        
        plt.pause(0.2)

    plt.ioff()

    plt.show()
    return
three_dimension_scatter()        