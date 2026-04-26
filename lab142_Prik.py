class Terytoriya:
    def __init__(self, назва="", площа=0):
        self.назва = назва
        self.площа = площа

    def get_info(self):
        return f"Територія: {self.назва}, Площа: {self.площа} км²"

    def status(self):
        return "Загальна територія"

class Oblast(Terytoriya):
    def __init__(self, назва="", площа=0, код_регіону=0):
        super().__init__(назва, площа)
        self.код_регіону = код_регіону

    def get_info(self):
        return f"Область: {self.назва} (Код: {self.код_регіону}), Площа: {self.площа} км²"

    def status(self):
        return "Адміністративна одиниця (Область)"

class Misto(Oblast):
    def __init__(self, назва="", площа=0, код_регіону=0, населення=0):
        super().__init__(назва, площа, код_регіону)
        self.населення = населення

    def get_info(self):
        return f"Місто: {self.назва}, Населення: {self.населення} осіб"

    def status(self):
        return "Населений пункт (Місто)"

    def density(self):
        """Власний метод класу Місто: розрахунок щільності населення."""
        return self.населення / self.площа if self.площа > 0 else 0

class Megapolis(Misto):
    def __init__(self, назва="", площа=0, код_регіону=0, населення=0, кількість_метро=0):
        super().__init__(назва, площа, код_регіону, населення)
        self.кількість_метро = кількість_метро

    def get_info(self):
        return f"Мегаполіс: {self.назва}, Населення: {self.населення}, Метро: {self.кількість_метро} ліній"

    def status(self):
        return "Особливий статус (Мегаполіс)"

# Демонстраційна програма з використанням однієї змінної
objects = [
    Terytoriya("Полісся", 15000),
    Oblast("Львівська", 21833, 13),
    Misto("Львів", 182, 13, 720000),
    Megapolis("Київ", 839, 11, 2900000, 3)
]

print("\nІєрархія територій:")
for obj in objects:
    # Поліморфний виклик методів через одну змінну 'obj'
    print(f"--- {obj.status()} ---")
    print(obj.get_info())