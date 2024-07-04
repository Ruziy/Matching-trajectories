import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Функция для расчета коэффициента симметрии между двумя ломаными линиями
def symmetry_coefficient(track1, track2):
    # Объединяем данные по времени (x-координате), используя внутреннее соединение
    merged_data = pd.merge(track1, track2, on='x', suffixes=('_track1', '_track2'), how='inner')
    
    if merged_data.empty:
        return float('NaN')  # Если нет общих точек, возвращаем NaN
    
    points1 = merged_data['y_track1'].values
    points2 = merged_data['y_track2'].values
    
    # Вычисляем среднеквадратичное отклонение (MSE)
    mse = np.mean((points1 - points2) ** 2)
    
    # Рассчитываем коэффициент симметрии как обратное среднеквадратичное отклонение
    symmetry_coeff = 1 - mse / np.mean(points1 ** 2)
    
    return symmetry_coeff

# Загрузим данные из CSV файла
file_path = r'data\traks_x_y_1_2_3.csv'  # Укажите полный или относительный путь к вашему CSV файлу
data = pd.read_csv(file_path, delimiter=';', header=None, skiprows=1, names=['track', 'x', 'y'])

# Разделение данных на три ломаные линии (track1, track2, track3)
track1 = data[data['track'] == 1].copy()
track2 = data[data['track'] == 2].copy()
track3 = data[data['track'] == 3].copy()

# Рассчитываем коэффициенты симметрии между парами линий
symmetry_coeff_1_2 = symmetry_coefficient(track1, track2)
symmetry_coeff_1_3 = symmetry_coefficient(track1, track3)
symmetry_coeff_2_3 = symmetry_coefficient(track2, track3)

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

