import matplotlib.pyplot as plt
from random_walk import Randomwalk
rw = Randomwalk()
rw.fill_walk()
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15, c=rw.y_values)
plt.show()
