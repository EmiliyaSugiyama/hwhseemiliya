import requests
from bs4 import BeautifulSoup
import numpy as np
import random


def load_countries_name(data_len):
    url = "https://randomuser.me/api/"
    params = {'results': data_len}
    response = requests.get(url, params=params)
    data = response.json()
    result = list(map(lambda x: x['location'], data['results']))
    title = [country['country'] for country in result]
    return title


def generate_product_id(data_len):
    return list(np.array([random.randint(1, 25) for i in range(data_len)]))


def generate_region_sales(data_len):
    return list(np.array([random.randint(100, 500) for i in range(data_len)]))


def generate_regions(size, city_names = []):
    regions = []
    index = 1
    unique_cities = list(set(city_names))
    for i in range(size):
        if len(unique_cities) > 0:
            city = unique_cities.pop()
            regions.append(f"Region {index}")
        else:
            regions.append(f"Region {index}")
            index += 1
            if index > 5:
                index = 1
                random.shuffle(regions)
    return regions


data_len = 50
data = np.column_stack((generate_product_id(data_len), generate_region_sales(data_len), generate_regions(data_len, [])))

# 1) общая сумма продаж
total_sales = np.sum(data[:, 1].astype(int))
print("Общая сумма продаж:", total_sales)

# 2) Сколько уникальных регионов продаж существует?
unique_regions = len(np.unique(data[:, 2]))
print("Количество уникальных регионов продаж:", unique_regions)

# 3) Средняя сумма продаж на продукт
average_sales_per_product = np.average(data[:, 1].astype(int))
print("Средняя сумма продаж на продукт:", average_sales_per_product)

# 4) Продукт с наибольшей суммой продаж
max_sale_idx = np.argmax(data[:, 1].astype(int))
max_sale_product_id = data[max_sale_idx, 0]
print("ID продукта с наибольшей суммой продаж:", max_sale_product_id)

# 5) Сумма продаж для каждого региона продаж (гистограмма)
import matplotlib.pyplot as plt

region_sales = {}
for region in np.unique(data[:, 2]):
    region_data = data[data[:, 2] == region]
    sales_sum = np.sum(region_data[:, 1].astype(int))
    region_sales[region] = sales_sum

region_names = list(region_sales.keys())
sales_sum = list(region_sales.values())

plt.bar(region_names, sales_sum)
plt.xlabel('Регион продаж')
plt.ylabel('Сумма продаж')
plt.title('Продажи по регионам')
plt.show()

# 6) Топ 5 продуктов по продажам (гистограмма)
sales = data[:, 1].astype(int)
top5_indices = sales.argsort()[::-1][:5]
top5_data = data[top5_indices]
other_sales = sales[5:].sum()

labels = [f"Продукт {x[0]}" for x in top5_data] + ["Другие"]
values = np.append(sales[top5_indices], other_sales)

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title('Топ 5 продуктов по продажам')
plt.show()

# Получение кодов валют для стран
url_site = 'https://www.exchangerate-api.com/docs/supported-currencies'
response = requests.get(url_site)
soup = BeautifulSoup(response.content, 'html.parser')
cu = soup.find('article', class_='mb-4 mb-md-6 px-3')
cur = cu.find_all('tr')
curr = [currency.find_all('td') for currency in cur]

country_currency_code = {}
for elem in curr:
    if len(elem[0].text) == 3:
        country_currency_code[elem[2].text] = elem[0].text

# Продажи в рублях
rub_sales = []
for region, sales in zip(data[:, 2], data[:, 1]):
    currency = country_currency_code.get(region)
    if currency == 'RUB':
        rub_sales.append(int(sales))
    else:
        rub_sales.append(int(sales) * exchange_rates[currency])

print("Продажи в рублях:", rub_sales)


