from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180
    ADDITIONAL_PERCENT = 5

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=CargoVan.MAX_MILEAGE)

    #TODO: could be the other calculation for % or the rounding (sum or only perc_to_reduce)
    def drive(self, mileage: float) -> None:
        percentage_to_reduce_with = round((mileage / CargoVan.MAX_MILEAGE) * 100)
        self.battery_level -= percentage_to_reduce_with + CargoVan.ADDITIONAL_PERCENT