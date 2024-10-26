# Данные
Nail_style = ["Шеллак", "Френч", "Обычный лак", "Гель-лак", "Акрил"]
Price = [2000, 1500, 1000, 3000, 3500]
Week = [4, 5, 4, 8, 6]

# 1. Среднее значение посещений салона
average_visits = sum(Week) / len(Week)
print(f'Среднее количество посещений: {average_visits:.2f}')

# 2. Общее количество посещений салона
total_visits = sum(Week)
print(f'Общее количество посещений за неделю: {total_visits}')

# 3. Выручка салона
total_revenue = sum(Price[i] * Week[i] for i in range(len(Nail_style)))
print(f'Общая выручка салона за неделю: {total_revenue} руб.')

# 4. Выручка по видам маникюра
print('Выручка по видам маникюра:')
for i in range(len(Nail_style)):
    revenue_by_style = Price[i] * Week[i]
    print(f'{Nail_style[i]}: {revenue_by_style} руб.')

# 5. Средняя выручка в день по видам маникюра
print('Средняя выручка в день по видам маникюра:')
days_in_week = 7
for i in range(len(Nail_style)):
    daily_revenue = (Price[i] * Week[i]) / days_in_week
    print(f'{Nail_style[i]}: {daily_revenue:.2f} руб. в день')
