"""
Exploración personal de Scikit Spatial.

frgonzalezb, 18 noviembre 2024.

Intentaré dibujar un "mono de palo".
"""


import matplotlib.pyplot as plt
from skspatial.objects import Point, Line, Circle


head: Circle = Circle(point=Point([0, 5]), radius=2)
eye_l: Point = Point([-0.5, 5.5])
eye_r: Point = Point([0.5, 5.5])
mouth: Line = Line.from_points([-0.5, 4], [0.5, 4])
body: Line = Line.from_points([0, 3], [0, -3])
arms: Line = Line.from_points([-5, 2.5], [5, 2.5])
leg_l: Line = Line.from_points([0, -3], [-5, -8])
leg_r: Line = Line.from_points([0, -3], [5, -8])

fig, ax = plt.subplots()
head.plot_2d(ax, edgecolor='black', facecolor='white', zorder=1)
eye_l.plot_2d(ax, color='black', zorder=2)
eye_r.plot_2d(ax, color='black', zorder=2)
mouth.plot_2d(ax, color='black', zorder=2)
body.plot_2d(ax, color='black')
arms.plot_2d(ax, color='black')
leg_l.plot_2d(ax, color='black')
leg_r.plot_2d(ax, color='black')
plt.axis((-10, 10, -10, 10))
plt.show()
