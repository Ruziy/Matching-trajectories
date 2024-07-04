import pandas as pd
import matplotlib.pyplot as plt

# Функция для расчета коэффициента симметрии между двумя ломаными линиями
def symmetry_coefficient(track1, track2, axis='y=x'):
    points1 = track1[['x', 'y']].values
    points2 = track2[['x', 'y']].values
    
    if axis == 'y=x':
        deviations = [(abs(x1 - y1), abs(x2 - y2)) for (x1, y1), (x2, y2) in zip(points1, points2)]
    # Добавляем поддержку других осей симметрии при необходимости
    # elif axis == 'другая ось':
    #     deviations = [(abs(...), abs(...)) for (...), (...)]
    else:
        raise ValueError("Неподдерживаемая ось симметрии")
    
    # Вычисляем среднее отклонение
    avg_deviation = sum((x_dev + y_dev) / 2 for x_dev, y_dev in deviations) / len(deviations)
    
    # Рассчитываем коэффициент симметрии
    symmetry_coeff = 1 - avg_deviation / max(track1['x'].max() - track1['x'].min(), track1['y'].max() - track1['y'].min())
    
    return symmetry_coeff

# Загрузим данные из CSV файла
file_path = r'data\traks_x_y_1_2_3.csv'  # Путь к вашему CSV файлу
data = pd.read_csv(file_path, delimiter=';', header=None, skiprows=1, names=['track', 'x', 'y'])

# Разделение данных на три ломаные линии (track1, track2, track3)
track1 = data[data['track'] == 1]
track2 = data[data['track'] == 2]
track3 = data[data['track'] == 3]

# Рассчитываем коэффициенты симметрии между парами линий
symmetry_coeff_1_2 = symmetry_coefficient(track1, track2, axis='y=x')
symmetry_coeff_1_3 = symmetry_coefficient(track1, track3, axis='y=x')
symmetry_coeff_2_3 = symmetry_coefficient(track2, track3, axis='y=x')

# Выводим результаты коэффициентов симметрии
print(f"Коэффициент симметрии между линиями 1 и 2: {symmetry_coeff_1_2:.2f}")
print(f"Коэффициент симметрии между линиями 1 и 3: {symmetry_coeff_1_3:.2f}")
print(f"Коэффициент симметрии между линиями 2 и 3: {symmetry_coeff_2_3:.2f}")

# Построение графика для наглядности
plt.figure(figsize=(10, 6))

# Отображение ломаных линий с различными цветами и маркерами
plt.plot(track1['x'], track1['y'], label='Трек 1', color='blue', marker='o')
plt.plot(track2['x'], track2['y'], label='Трек 2', color='red', marker='x')
plt.plot(track3['x'], track3['y'], label='Трек 3', color='green', marker='s')

# Настройка графика
plt.title('Сравнение ломаных линий')
plt.xlabel('X координата')
plt.ylabel('Y координата')
plt.legend()
plt.grid(True)

# Отображение графика
plt.show()












