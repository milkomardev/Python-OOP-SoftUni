from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, name):
        try:
            products = next(filter(lambda p: p.name == name, self.products))
            return products
        except StopIteration:
            pass

    def remove(self, name):
        product = self.find(name)
        if product in self.products:
            self.products.remove(product)

    def __repr__(self):
        result = []
        for p in self.products:
            result.append(f"{p.name}: {p.quantity}")
        return '\n'.join(result)