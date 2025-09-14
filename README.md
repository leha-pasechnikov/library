### Библиотека geometry

---

содержит код для создания своих фигур и предоставляет базовые фигуры (треугольник круг).
Поддерживает вычисление площади у всех фигур и проверку прямоугольности треугольника.
---
Структура
```
geometry/
├── geometry/
│   ├── __init__.py
│   ├── figures.py      # Определение классов Circle и Triangle, FigureBase
│   └── create.py       # Фабрика Create для динамического создания фигур
├── test/
│   ├── __init__.py
│   └── test.py         # Тесты для Circle, Triangle и Create
├── htmlcov/
│   └── index.html      # Отчёт об покрытии тестов
├── main.py             # Пример использования библиотеки
└── __init__.py
```
---

запуск тестов unittest
``` 
python -m unittest geometry.test.test
```
покрытие coverage в [htmlcov/index.html](htmlcov/index.html)