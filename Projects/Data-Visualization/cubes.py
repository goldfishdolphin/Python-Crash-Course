import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [x**3 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(x_values, y_values)
ax.set_title("Cube Numbers")
ax.set_xlabel('Values')
ax.set_ylabel('Cube of the value')
plt.show()
