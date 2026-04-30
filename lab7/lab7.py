class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = year

    def __str__(self):
        return f"VID: {self.vid} | {self.model} ({self.year})"

    def __eq__(self, other):
        if isinstance(other, Vehicle):
            return self.vid == other.vid
        return False

    def is_new(self, n):

        return self.year >= (2026 - n - 1)


class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
        super().__init__(vid, model, year)
        self.fuel_type = fuel_type
        self.doors = doors

    def __str__(self):
        return f"[Car] {super().__str__()} | Fuel: {self.fuel_type} | {self.doors} Doors"


class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        super().__init__(vid, model, year)
        self.max_load = max_load
        self.axles = axles

    def __str__(self):
        return f"[Truck] {super().__str__()} | Load: {self.max_load}kg | {self.axles} Axles"


class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, bike_type):
        super().__init__(vid, model, year)
        self.engine_cc = engine_cc
        self.bike_type = bike_type

    def __str__(self):
        return f"[Motorcycle] {super().__str__()} | Eng: {self.engine_cc}cc | Type: {self.bike_type}"


def save_fleet_to_file(vehicles, filename):
    with open(filename, 'w') as f:
        for v in vehicles:
            if isinstance(v, Car):
                f.write(f"Car, {v.vid}, {v.model}, {v.year}, {v.fuel_type}, {v.doors}\n")
            elif isinstance(v, Truck):
                f.write(f"Truck, {v.vid}, {v.model}, {v.year}, {v.max_load}, {v.axles}\n")
            elif isinstance(v, Motorcycle):
                f.write(f"Motorcycle, {v.vid}, {v.model}, {v.year}, {v.engine_cc}, {v.bike_type}\n")


def load_fleet_from_file(filename):
    reconstructed_vehicles = []
    print(f"Loading fleet data from '{filename}'...")
    try:
        with open(filename, 'r') as f:
            for line in f:
                parts = [p.strip() for p in line.split(',')]
                v_type = parts[0]

                if v_type == "Car":
                    obj = Car(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5]))
                elif v_type == "Truck":
                    obj = Truck(parts[1], parts[2], int(parts[3]), int(parts[4]), int(parts[5]))
                elif v_type == "Motorcycle":
                    obj = Motorcycle(parts[1], parts[2], int(parts[3]), int(parts[4]), parts[5])

                reconstructed_vehicles.append(obj)
        print(f" {len(reconstructed_vehicles)} vehicles loaded successfully.")
    except FileNotFoundError:
        print("File not found.")
    return reconstructed_vehicles



my_fleet = [
    Car("V001", "Tesla Model 3", 2023, "Electric", 4),
    Truck("T101", "Volvo FH16", 2019, 25000, 6),
    Motorcycle("M301", "Yamaha R1", 2024, 998, "Sport"),
    Car("V002", "Toyota Corolla", 2018, "Petrol", 4),
    Truck("T102", "Mercedes Actros", 2021, 18000, 4),
    Motorcycle("M302", "Harley Davidson", 2015, 1200, "Cruiser")
]


save_fleet_to_file(my_fleet, "fleet.txt")


loaded_fleet = load_fleet_from_file("fleet.txt")


print("\n--- All Vehicles ---")
for vehicle in loaded_fleet:
    print(vehicle)


print("\n--- Recent Vehicles (Last 4 Years) ---")
for vehicle in loaded_fleet:
    if vehicle.is_new(4):
        print(vehicle)


print("\n--- Electric Cars Only ---")
for vehicle in loaded_fleet:
    if isinstance(vehicle, Car) and vehicle.fuel_type == "Electric":
        print(vehicle)