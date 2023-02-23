from die import Die
# Create a D6
die = Die()

results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)
