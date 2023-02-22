import matplotlib.pyplot as plt
from random_walk import Randomwalk
while True:
    rw = Randomwalk()
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, s=15, c=point_numbers,
               cmap=plt.cm.Blues, edgecolors='none')
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1],
               c='red', edgecolors='none', s=100)

    plt.show()
    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
