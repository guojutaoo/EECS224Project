import numpy as np
from matplotlib import pyplot as plt


# display the comparison time between sequential and parallel RSA algorithm
def show(sequetial, parallelize):

    plt.figure("RSA algorithm")
    plt.title('Time comparision between sequential and parallel RSA algorithm')
    plt.ylabel('Time')
    plt.xlabel('Method')
    bar = ("sequential RSA", "Parallel RSA")
    y_pos = np.array(bar)
    x = [sequetial, parallelize]
    plt.bar(y_pos, x, color=(0.5, 0.5, 0.5, 0.6))
    plt.xticks(range(4))
    plt.show()
    return
