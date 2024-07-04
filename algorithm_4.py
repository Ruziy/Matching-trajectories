import pandas as pd
import matplotlib.pyplot as plt


def symmetry_coefficient(track1, track2):
    # Вычисляем средние значения Y для каждой линии
    mean_y1 = track1['y'].mean()
    mean_y2 = track2['y'].mean()
    
    # Вычисляем коэффициент симметрии как процент отклонения между средними значениями Y
    symmetry_percent = (1 - abs(mean_y1 - mean_y2) / ((mean_y1 + mean_y2) / 2)) * 100
    
    return symmetry_percent


# Загрузим данные из CSV файла
file_path = r'data\traks_x_y_1_2_3_4.csv'  # Укажите полный или относительный путь к вашему CSV файлу
data = pd.read_csv(file_path, delimiter=';', header=None, skiprows=1, names=['track', 'x', 'y'])

# Разделение данных на четыре ломаные линии (track1, track2, track3, track4)
track1 = data[data['track'] == 1].copy()
track2 = data[data['track'] == 2].copy()
track3 = data[data['track'] == 3].copy()
track4 = data[data['track'] == 4].copy()

# Рассчитываем коэффициенты симметрии между парами линий
symmetry_coeff_1_2 = symmetry_coefficient(track1, track2)
symmetry_coeff_1_3 = symmetry_coefficient(track1, track3)
symmetry_coeff_1_4 = symmetry_coefficient(track1, track4)
symmetry_coeff_2_3 = symmetry_coefficient(track2, track3)
symmetry_coeff_2_4 = symmetry_coefficient(track2, track4)
symmetry_coeff_3_4 = symmetry_coefficient(track3, track4)

# Выводим результаты коэффициентов симметрии
print(f"Коэффициент симметрии между линиями 1 и 2: {symmetry_coeff_1_2:.2f}")
print(f"Коэффициент симметрии между линиями 1 и 3: {symmetry_coeff_1_3:.2f}")
print(f"Коэффициент симметрии между линиями 1 и 4: {symmetry_coeff_1_4:.2f}")
print(f"Коэффициент симметрии между линиями 2 и 3: {symmetry_coeff_2_3:.2f}")
print(f"Коэффициент симметрии между линиями 2 и 4: {symmetry_coeff_2_4:.2f}")
print(f"Коэффициент симметрии между линиями 3 и 4: {symmetry_coeff_3_4:.2f}")

# Построение четырех графиков для наглядности
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# График 1: Трек 1
axs[0, 0].plot(track1['x'], track1['y'], label='Трек 1', color='blue', marker='o')
axs[0, 0].set_title('Трек 1')
axs[0, 0].set_xlabel('X координата')
axs[0, 0].set_ylabel('Y координата')
axs[0, 0].legend()
axs[0, 0].grid(True)

# График 2: Трек 2
axs[0, 1].plot(track2['x'], track2['y'], label='Трек 2', color='red', marker='x')
axs[0, 1].set_title('Трек 2')
axs[0, 1].set_xlabel('X координата')
axs[0, 1].set_ylabel('Y координата')
axs[0, 1].legend()
axs[0, 1].grid(True)

# График 3: Трек 3
axs[1, 0].plot(track3['x'], track3['y'], label='Трек 3', color='green', marker='s')
axs[1, 0].set_title('Трек 3')
axs[1, 0].set_xlabel('X координата')
axs[1, 0].set_ylabel('Y координата')
axs[1, 0].legend()
axs[1, 0].grid(True)

# График 4: Трек 4
axs[1, 1].plot(track4['x'], track4['y'], label='Трек 4', color='purple', marker='d')
axs[1, 1].set_title('Трек 4')
axs[1, 1].set_xlabel('X координата')
axs[1, 1].set_ylabel('Y координата')
axs[1, 1].legend()
axs[1, 1].grid(True)

# Размещение графиков
plt.tight_layout()
plt.show()












