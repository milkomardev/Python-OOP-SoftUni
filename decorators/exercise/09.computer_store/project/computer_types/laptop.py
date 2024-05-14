from project.computer_types.computer import Computer


class Laptop(Computer):

    @property
    def type(self):
        return "laptop"

    @property
    def av_processors(self):
        return {"AMD Ryzen 9 5950X": 900,
                "Intel Core i9-11900H": 1050,
                "Apple M1 Pro": 1200}

    @property
    def av_ram(self):
        return [2**n for n in range(1, 7)]