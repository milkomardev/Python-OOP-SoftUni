from typing import List

from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {'MainService': MainService, 'SecondaryService': SecondaryService}
    VALID_ROBOTS = {'FemaleRobot': FemaleRobot, 'MaleRobot': MaleRobot}

    def __init__(self):
        self.robots: List[MaleRobot, FemaleRobot] = []
        self.services: List[MainService, SecondaryService] = []

    def get_robot_by_name(self, name):
        existing_robot = [r for r in self.robots if r.name == name]
        if existing_robot:
            return existing_robot[0]
        return None

    def get_robot_by_name_in_service(self, name, service):
        existing_robot = [r for r in service.robots if r.name == name]
        if existing_robot:
            return existing_robot[0]
        return None

    def get_service_by_name(self, name):
        existing_service = [s for s in self.services if s.name == name]
        if existing_service:
            return existing_service[0]
        return None

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")

        service = self.VALID_SERVICES[service_type](name)
        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")

        robot = self.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        current_robot = self.get_robot_by_name(robot_name)
        current_service = self.get_service_by_name(service_name)

        if (current_robot.__class__.__name__ == "MaleRobot" and current_service.__class__.__name__ == "SecondaryService") \
                or (current_robot.__class__.__name__ == "FemaleRobot" and current_service.__class__.__name__ == "MainService"):
            return "Unsuitable service."

        if len(current_service.robots) >= current_service.capacity:
            raise Exception("Not enough capacity for this robot!")

        current_service.robots.append(current_robot)
        self.robots.remove(current_robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        current_service = self.get_service_by_name(service_name)
        current_robot = self.get_robot_by_name_in_service(robot_name, current_service)
        if not current_robot:
            raise Exception("No such robot in this service!")

        self.robots.append(current_robot)
        current_service.robots.remove(current_robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        current_service = self.get_service_by_name(service_name)
        robots_fed = 0

        if current_service.robots:
            for r in current_service.robots:
                r.eating()
                robots_fed += 1

        return f"Robots fed: {robots_fed}."

    def service_price(self, service_name: str):
        current_service = self.get_service_by_name(service_name)
        total_price = 0

        if current_service.robots:
            for r in current_service.robots:
                total_price += r.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []
        for service in self.services:
            result.append(service.details())

        return '\n'.join(result)