from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLES = {"CargoVan": CargoVan, "PassengerCar": PassengerCar}

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def get_user_by_driving_license_number(self, driving_license_number):
        existing_user = [u for u in self.users if driving_license_number == u.driving_license_number]
        if existing_user:
            return existing_user[0]
        return None

    def get_vehicle_by_license_plate_number(self, license_plate_number):
        existing_vehicle = [v for v in self.vehicles if license_plate_number == v.license_plate_number]
        if existing_vehicle:
            return existing_vehicle[0]
        return None

    def get_damaged_vehicles(self):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        if damaged_vehicles:
            return damaged_vehicles
        return None

    def get_route_by_direction_and_length(self, start, end, length):
        existing_route = [r for r in self.routes if
                          r.start_point == start and r.end_point == end and r.length == length]
        if existing_route:
            return existing_route[0]
        return None

    def get_route_by_direction_and_shorter_length(self, start, end, length):
        existing_route = [r for r in self.routes if r.start_point == start and r.end_point == end and r.length < length]
        if existing_route:
            return existing_route[0]
        return None

    def get_route_by_direction_and_longer_length(self, start, end, length):
        existing_route = [r for r in self.routes if r.start_point == start and r.end_point == end and r.length > length]
        if existing_route:
            return existing_route[0]
        return None

    def get_route_by_route_id(self, route_id):
        existing_route = [r for r in self.routes if r.route_id == route_id]
        if existing_route:
            return existing_route[0]
        return None

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        existing_user = self.get_user_by_driving_license_number(driving_license_number)
        if existing_user:
            return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        existing_vehicle = self.get_vehicle_by_license_plate_number(license_plate_number)
        if existing_vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        vehicle = self.VALID_VEHICLES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        existing_route_same_direction_same_length = self.get_route_by_direction_and_length(start_point, end_point,
                                                                                           length)
        if existing_route_same_direction_same_length:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        existing_route_same_direction_shorter_length = self.get_route_by_direction_and_shorter_length(start_point,
                                                                                                      end_point, length)
        if existing_route_same_direction_shorter_length:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        existing_route_same_direction_longer_length = self.get_route_by_direction_and_longer_length(start_point,
                                                                                                    end_point, length)
        if existing_route_same_direction_longer_length:
            existing_route_same_direction_longer_length.is_locked = True

        route_id = len(self.routes) + 1
        route = Route(start_point, end_point, length, route_id)
        self.routes.append(route)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        current_user = self.get_user_by_driving_license_number(driving_license_number)
        if current_user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        current_vehicle = self.get_vehicle_by_license_plate_number(license_plate_number)
        if current_vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        current_route = self.get_route_by_route_id(route_id)
        if current_route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        current_vehicle.drive(current_route.length)

        if is_accident_happened:
            current_vehicle.is_damaged = True
            current_user.decrease_rating()
        else:
            current_user.increase_rating()

        return current_vehicle.__str__()

    def repair_vehicles(self, count: int):
        damaged_vehicles = self.get_damaged_vehicles()
        if damaged_vehicles:
            damaged_vehicles = sorted(damaged_vehicles, key=lambda x: (x.brand, x.model))
        else:
            damaged_vehicles = []
        repaired_vehicles = 0

        if count >= len(damaged_vehicles):
            for vehicle in damaged_vehicles:
                vehicle.is_damaged = False
                vehicle.battery_level = 100
                repaired_vehicles += 1
        else:
            for i in range(count):
                damaged_vehicles[i].is_damaged = False
                damaged_vehicles[i].battery_level = 100
                repaired_vehicles += 1

        return f"{repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        result = ["*** E-Drive-Rent ***"]
        for u in sorted(self.users, key=lambda x: -x.rating):
            result.append(u.__str__())

        return '\n'.join(result)