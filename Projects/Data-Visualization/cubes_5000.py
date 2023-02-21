import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.turbo, s=5)
ax.set_title("Cube Numbers")
ax.set_xlabel('Values')
ax.set_ylabel('Cube of the value')
plt.show()
