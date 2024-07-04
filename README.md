# Matching trajectories
Разработан алгоритм для оценки симметрии траекторий на основе двух методов: коэффициента корреляции Пирсона и расстояния Хаусдорфа. Программа анализирует четыре различные траектории, загруженные из CSV файла, и вычисляет коэффициенты симметрии для всех возможных пар траекторий. Если коэффициент корреляции Пирсона равен 0%, то используется метод расстояния Хаусдорфа для более точной оценки симметрии. Результаты вычислений выводятся на экран, включая указание метода и оценку симметрии между парами траекторий.

## Структура проекта:
```
OPENCODE_TZ/
│
├── algorithm.py
├── requirements.txt
├── README.md
└── data/
    ├── task-computer-vision.pdf
    ├── traks.csv
```
    
## Установка
1. Склонируйте репозиторий.
    ```bash
    git clone https://github.com/Ruziy/openCode_TZ
    cd OPENCODE_TZ
    ```
2. Установите необходимые библиотеки:
    ```bash
    pip install -r requirements.txt
    ```

## Использование
1.Поместите входной CSV файл с данными траекторий в папку data и назовите его traks.csv.
2.Запустите скрипт algorithm.py с указанием пути к CSV файлу:
    
    ```bash
    python algorithm.py data\\traks.csv
    ```

3.Результаты вычислений коэффициентов симметрии между траекториями будут выведены в консоль, включая указание метода (Пирсона или Хаусдорфа) и оценку симметрии.

4.График, иллюстрирующий сравнение ломаных линий, также будет отображен после вычислений.
