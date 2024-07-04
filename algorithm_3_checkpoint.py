import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def symmetry_coefficient(track1, track2):
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
        # Если общих точек нет, используем метод ближайших соседей
        return nearest_neighbor_symmetry(track1, track2)

def nearest_neighbor_symmetry(track1, track2):
    differences = []
    
    for idx1, row1 in track1.iterrows():
        x1 = row1['x']
        y1 = row1['y']
        # Найдем ближайшую точку по x на track2
        closest_row = track2.iloc[(track2['x'] - x1).abs().argsort()[:1]]
        x2 = closest_row['x'].values[0]
        y2 = closest_row['y'].values[0]
        
        # Вычислим разницу по y
        differences.append(abs(y1 - y2))
    
    # Возьмем среднюю разницу по y
    mean_difference = np.mean(differences)
    max_difference = max(track1['y'].max(), track2['y'].max())
    normalized_difference = (1 - (mean_difference / max_difference)) * 100  # Преобразуем в проценты
    return normalized_difference

# Загрузим данные из CSV файла
file_path = r'data\traks_x_y_1_2_3.csv'  # Укажите полный или относительный путь к вашему CSV файлу
data = pd.read_csv(file_path, delimiter=';', header=None, skiprows=1, names=['track', 'x', 'y'])

# Разделение данных на три ломаные линии (track1, track2, track3)
track1 = data[data['track'] == 1].copy()
track2 = data[data['track'] == 2].copy()
track3 = data[data['track'] == 3].copy()

# Проверяем на наличие пустых значений
track1.dropna(inplace=True)
track2.dropna(inplace=True)
track3.dropna(inplace=True)

# Рассчитываем коэффициенты симметрии между парами линий
symmetry_coeff_1_2 = symmetry_coefficient(track1, track2)
symmetry_coeff_1_3 = symmetry_coefficient(track1, track3)
symmetry_coeff_2_3 = symmetry_coefficient(track2, track3)

# Выводим результаты коэффициентов симметрии
print(f"Коэффициент симметрии между линиями 1 и 2: {symmetry_coeff_1_2:.2f}%")
print(f"Коэффициент симметрии между линиями 1 и 3: {symmetry_coeff_1_3:.2f}%")
print(f"Коэффициент симметрии между линиями 2 и 3: {symmetry_coeff_2_3:.2f}%")

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
