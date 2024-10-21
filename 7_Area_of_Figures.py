import math

figure_type = input()

if figure_type == "square":
    figure_size = float(input()) #ако е квадрат да напишем една страна
    figure_area = figure_size * figure_size #формула
    print(f"{figure_area:.3f}") #да намерим лицето на фигурата

elif figure_type == "rectangle":
    figure_size = float(input()) #ако е прав. да напишем две страни
    figure_size2 = float(input())
    figure_area = figure_size * figure_size2
    print(f"{figure_area:.3f}")

elif figure_type == "circle":
    radius = float(input()) #ако е кръг на въведем радиус и import math(pi)
    figure_area = (radius ** 2) * math.pi
    print(f"{figure_area:.3f}")

elif figure_type == "triangle":
    figure_size1 = float(input())
    figure_size2 = float(input())
    figure_area = ( figure_size1 * figure_size2) / 2
    print(f"{figure_area:.3f}")


