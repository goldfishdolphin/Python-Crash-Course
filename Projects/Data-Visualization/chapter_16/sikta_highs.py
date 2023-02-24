import csv
from datetime import datetime
import matplotlib.pyplot as plt
filename = 'Projects/Data-Visualization/chapter_16/data/sikta_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get date and high temprature from this file
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)
print(dates)
# Plot high tempratures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
# Format plot
ax.set_title('Daily high tempratures, July 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temprature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.show()
