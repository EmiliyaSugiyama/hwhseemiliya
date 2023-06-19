import matplotlib.pyplot as plt

# Годы и объемы торговли для каждой страны
years = [2018, 2019, 2020, 2021]
trade_volume = {
    'Country1': [100, 150, 200, 180],
    'Country2': [80, 120, 160, 140],
    'Country3': [120, 100, 80, 90]
}

# Построение графика
plt.figure(figsize=(10, 6))  # Размер графика
colors = ['red', 'green', 'blue']  # Цвета для каждой страны

for country, volumes in trade_volume.items():
    plt.plot(years, volumes, label=country, marker='o', linewidth=2)

plt.xlabel('Годы')
plt.ylabel('Объемы торговли')
plt.title('Объемы торговли по годам и странам')
plt.legend()
plt.grid(True)

plt.savefig('trade_volume.png', dpi=300)  # Сохранение графика в файл
plt.show()
