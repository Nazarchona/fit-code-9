import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Визначаємо табличні дані
x = np.array([0.4, 0.6, 0.9, 1.4, 2.0])
y = np.array([2.45, 1.63, 0.95, 0.73, 1.95])

# Створюємо кубічний сплайн
cs = CubicSpline(x, y)

# Створюємо нові точки для побудови графіка
x_new = np.linspace(0.4, 2, 100)
y_new = cs(x_new)

# Візуалізація результату
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Дані')
plt.plot(x_new, y_new, '-', label='Кубічний сплайн')
plt.title('Кубічний сплайн для таблично заданих даних')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
