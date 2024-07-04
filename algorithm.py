import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import directed_hausdorff
import argparse
import os

def symmetry_coefficient(track1, track2, method='pearson'):
    """
    Вычисляет коэффициент симметрии между двумя треками.
    Использует метод Пирсона или Хаусдорфа в зависимости от указанного метода.
    """
    if method == 'pearson':
        merged_data = pd.merge(track1, track2, on='x', suffixes=('_track1', '_track2'), how='inner')
        if not merged_data.empty:
            points1 = merged_data['y_track1'].values
            points2 = merged_data['y_track2'].values
            if np.std(points1) == 0 or np.std(points2) == 0:
                return 0
            correlation_coeff = np.corrcoef(points1, points2)[0, 1]
            return abs(correlation_coeff) * 100
        else:
            hausdorff_symmetry_coeff = hausdorff_symmetry(track1, track2)
            return hausdorff_symmetry_coeff
    elif method == 'hausdorff':
        hausdorff_symmetry_coeff = hausdorff_symmetry(track1, track2)
        normalized_coeff = 100 - hausdorff_symmetry_coeff
        return max(0, min(100, normalized_coeff))

def hausdorff_symmetry(track1, track2):
    """
    Вычисляет расстояние Хаусдорфа между двумя треками и нормализует результат.
    """
    distance1 = directed_hausdorff(track1[['x', 'y']].values, track2[['x', 'y']].values)[0]
    distance2 = directed_hausdorff(track2[['x', 'y']].values, track1[['x', 'y']].values)[0]
    max_distance = max(np.max(track1['x']), np.max(track2['x']), np.max(track1['y']), np.max(track2['y']))
    symmetry = (1 - (max(distance1, distance2) / max_distance)) * 100
    return max(0, min(100, symmetry))

def transform_symmetry_coefficient(value):
    """
    Преобразует значение коэффициента симметрии в интервал от 0 до 100%.
    """
    transformed_value = max(0, min(100, value))
    return transformed_value

def main(file_path):
    """
    Главная функция, выполняющая загрузку данных, расчет коэффициентов симметрии и вывод результатов.
    """
    file_path = os.path.abspath(file_path)
    data = pd.read_csv(file_path, delimiter=';', header=None, skiprows=1, names=['track', 'time', 'x', 'y'])
    tracks = [data[data['track'] == i] for i in range(1, 5)]
    pairs = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    
    results = {}
    for pair in pairs:
        track1, track2 = tracks[pair[0] - 1], tracks[pair[1] - 1]
        coefficient = symmetry_coefficient(track1, track2, method='pearson')
        if coefficient == 0:
            method = 'hausdorff'
            coefficient = symmetry_coefficient(track1, track2, method=method)
        else:
            method = 'pearson'
        results[(pair[0], pair[1], method)] = transform_symmetry_coefficient(coefficient)
    
    for pair, coeff in results.items():
        method = pair[2]
        if coeff == 100:
            description = "траектории полностью совпадают"
        elif coeff >= 90:
            description = "незначительное отличие траекторий"
        elif coeff <= 30:
            description = "значительное отличие траекторий"
        else:
            description = "траектории отличаются"
        print(f"Коэффициент симметрии между линиями {pair[0]} и {pair[1]} (метод {method}): {coeff:.2f}%, вывод: {description}")

    plt.figure(figsize=(10, 6))
    for pair, color, marker, label in zip([1, 2, 3, 4], ['blue', 'red', 'green', 'purple'], ['o', 'x', 's', '^'], ['Трек 1', 'Трек 2', 'Трек 3', 'Трек 4']):
        plt.plot(data[data['track'] == pair]['x'], data[data['track'] == pair]['y'], label=label, color=color, marker=marker)
    
    plt.title('Сравнение ломаных линий')
    plt.xlabel('X координата')
    plt.ylabel('Y координата')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    """
    Основной блок программы, выполняемый при запуске скрипта через командную строку.
    """
    parser = argparse.ArgumentParser(description="Calculate and plot symmetry coefficients for tracks.")
    parser.add_argument('file_path', type=str, help='Path to the CSV file containing track data.')
    args = parser.parse_args()
    main(args.file_path)
