import math

class Figura:
   
    def volume(self):
      
        return 0

class Paralelepiped(Figura):
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def volume(self):
        # Об'єм паралелепіпеда: V = a * b * c
        return self.a * self.b * self.c

class Tetraedr(Figura):
    def __init__(self, a=0):
        self.a = a

    def volume(self):
        # Формула згідно із завданням: V = (a^3 * sqrt(2)) / 12
        return (self.a**3 * math.sqrt(2)) / 12

class Kulya(Figura):
    def __init__(self, r=0):
        self.r = r

    def volume(self):
        # Формула згідно із завданням: V = 4/3 * pi * r^3
        return (4/3) * math.pi * (self.r**3)

# Демонстрація роботи
figures = [
    Paralelepiped(2, 3, 4),
    Tetraedr(3),
    Kulya(5)
]

print("Об'єми фігур:")
for fig in figures:
    print(f"{type(fig).__name__}: {fig.volume():.2f}")