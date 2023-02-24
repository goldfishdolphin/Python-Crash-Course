import csv
import matplotlib.pyplot as plt
filename = 'data/sikta_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Get high temprature from this file
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
print(highs)
# Plot high tempratures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(highs, c='red')
# Format plot
ax.set_title('Daily high tempratures, July 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temprature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.show()
