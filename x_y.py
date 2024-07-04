import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
file_path = r'data\traks_x_y_4.csv'  # Укажите полный или относительный путь к вашему CSV файлу
data = pd.read_csv(file_path, delimiter=';')  # Укажите символ разделителя, если это не запятая

# Предполагается, что в CSV файле есть колонки 'x' и 'y'
x = data['x']
y = data['y']

# Построение траектории
plt.figure(figsize=(8, 6))  # Размеры графика
plt.plot(x, y, marker='o', linestyle='-', color='b')  # Маркеры точек, линия и цвет

# Настройка графика
plt.title('Траектория по точкам')
plt.xlabel('X координата')
plt.ylabel('Y координата')
plt.grid(True)

# Сохранение графика в файл
plt.savefig('trajectory_plot_4_TRC.png')  # Укажите имя и формат файла (например, PNG, JPG)

# Показать график (необязательно, если нужно только сохранить файл)
plt.show()




