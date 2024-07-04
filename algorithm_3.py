import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import directed_hausdorff

# Функция для вычисления коэффициента симметрии методом Пирсона
def pearson_symmetry(track1, track2):
    # Объединяем данные по времени (x-координате), используя внутреннее соединение
    merged_data = pd.merge(track1, track2, on='x', suffixes=('_track1', '_track2'), how='inner')
    
    # Проверяем, есть ли общие точки
    if not merged_data.empty:
        # Если есть общие точки, проверяем на NaN и вычисляем коэффициент корреляции Пирсона
        points1 = merged_data['y_track1'].values
        points2 = merged_data['y_track2'].values
        if np.std(points1) == 0 or np.std(points2) == 0:
            return 0  # Если дисперсия нулевая, возвращаем коэффициент 0
        correlation_coeff = np.corrcoef(points1, points2)[0, 1]
        return abs(correlation_coeff) * 100  # Преобразуем в проценты
    else:
        return 0  # Если общих точек нет, возвращаем 0

# Функция для вычисления коэффициента симметрии методом Хаусдорфа
def hausdorff_symmetry(track1, track2):
    # Вычисляем расстояние Хаусдорфа между двумя линиями
    distance1 = directed_hausdorff(track1[['x', 'y']].values, track2[['x', 'y']].values)[0]
    distance2 = directed_hausdorff(track2[['x', 'y']].values, track1[['x', 'y']].values)[0]
    
    # Нормализуем расстояние от 0 до 100%
    max_distance = max(np.max(track1['x']), np.max(track2['x']), np.max(track1['y']), np.max(track2['y']))
    symmetry = (1 - (max(distance1, distance2) / max_distance)) * 100
    
    return max(0, min(100, symmetry))

# Функция для вычисления коэффициента симметрии с использованием выбранного метода
def symmetry_coefficient(track1, track2, method='pearson'):
    if method == 'pearson':
        return pearson_symmetry(track1, track2)
    elif method == 'hausdorff':
        return hausdorff_symmetry(track1, track2)
    else:
        raise ValueError("Unsupported symmetry method. Supported methods are 'pearson' and 'hausdorff'.")

# Функция для преобразования значения в интервал от 0 до 100%
def transform_symmetry_coefficient(value):
    transformed_value = max(0, min(100, value))
    return transformed_value

# Загрузим данные из CSV файла
file_path = r'data\traks_x_y_1_2_3_4.csv'  # Укажите полный или относительный путь к вашему CSV файлу
data = pd.read_csv(file_path, delimiter=';', header=None, skiprows=1, names=['track', 'x', 'y'])

# Разделение данных на четыре ломаные линии (track1, track2, track3, track4)
track1 = data[data['track'] == 1].copy()
track2 = data[data['track'] == 2].copy()
track3 = data[data['track'] == 3].copy()
track4 = data[data['track'] == 4].copy()

# Проверяем на наличие пустых значений
track1.dropna(inplace=True)
track2.dropna(inplace=True)
track3.dropna(inplace=True)
track4.dropna(inplace=True)

# Рассчитываем коэффициенты симметрии между парами линий с указанием метода
symmetry_coeff_1_2 = transform_symmetry_coefficient(symmetry_coefficient(track1, track2, method='pearson'))
symmetry_coeff_1_3 = transform_symmetry_coefficient(symmetry_coefficient(track1, track3, method='pearson'))
symmetry_coeff_1_4 = transform_symmetry_coefficient(symmetry_coefficient(track1, track4, method='hausdorff'))
symmetry_coeff_2_3 = transform_symmetry_coefficient(symmetry_coefficient(track2, track3, method='pearson'))
symmetry_coeff_2_4 = transform_symmetry_coefficient(symmetry_coefficient(track2, track4, method='hausdorff'))
symmetry_coeff_3_4 = transform_symmetry_coefficient(symmetry_coefficient(track3, track4, method='hausdorff'))

# Выводим результаты коэффициентов симметрии с указанием метода
print(f"Коэффициент симметрии между линиями 1 и 2 (метод Пирсона): {symmetry_coeff_1_2:.2f}%")
print(f"Коэффициент симметрии между линиями 1 и 3 (метод Пирсона): {symmetry_coeff_1_3:.2f}%")
print(f"Коэффициент симметрии между линиями 1 и 4 (метод Хаусдорфа): {symmetry_coeff_1_4:.2f}%")
print(f"Коэффициент симметрии между линиями 2 и 3 (метод Пирсона): {symmetry_coeff_2_3:.2f}%")
print(f"Коэффициент симметрии между линиями 2 и 4 (метод Хаусдорфа): {symmetry_coeff_2_4:.2f}%")
print(f"Коэффициент симметрии между линиями 3 и 4 (метод Хаусдорфа): {symmetry_coeff_3_4:.2f}%")

# Построение графика для наглядности
plt.figure(figsize=(10, 6))

# Отображение ломаных линий с различными цветами и маркерами
plt.plot(track1['x'], track1['y'], label='Трек 1', color='blue', marker='o')
plt.plot(track2['x'], track2['y'], label='Трек 2', color='red', marker='x')
plt.plot(track3['x'], track3['y'], label='Трек 3', color='green', marker='s')
plt.plot(track4['x'], track4['y'], label='Трек 4', color='purple', marker='^')

# Настройка графика
plt.title('Сравнение ломаных линий')
plt.xlabel('X координата')
plt.ylabel('Y координата')
plt.legend()
plt.grid(True)

# Отображение графика
plt.show()
