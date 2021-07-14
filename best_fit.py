import matplotlib.pyplot as plt

x = np.array(df['last_eruption_year'])
x = x.astype(int)
x = 2021 - x

y = df['population_within_10_km']
y = y.astype(int)

plt.scatter(x, y, color = 'darkblue')
plt.xlabel("Years since last eruption")
plt.ylabel("Population within 10 km")

m, b = np.polyfit(x, y, 1)
ind = np.arange(max(x))
plt.plot(ind, m*ind + b, color = 'turquoise')
