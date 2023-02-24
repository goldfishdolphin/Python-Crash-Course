import csv
from datetime import datetime
import matplotlib.pyplot as plt
filename = 'Projects/Data-Visualization/chapter_16/data/sikta_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get date,high and low temprature from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot high tempratures, highs and lows.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='purple', alpha=0.1)
# Format plot
ax.set_title('Daily high, lowtempratures, July 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temprature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.show()
