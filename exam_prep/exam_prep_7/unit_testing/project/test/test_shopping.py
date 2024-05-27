from unittest import TestCase, main

from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart("Test", 100)

    def test_constructor(self):
        self.assertEqual("Test", self.shopping_cart.shop_name)
        self.assertEqual(100, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_name_start_with_lowercase_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart = ShoppingCart("test", 100)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_name_contains_non_letters_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart = ShoppingCart("Test1", 100)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_method_price_higher_than_100_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart("product", 120)
        self.assertEqual("Product product cost too much!", str(ve.exception))

    def test_add_to_cart_method_price_100_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart("product", 100)
        self.assertEqual("Product product cost too much!", str(ve.exception))

    def test_add_to_cart_method_updates_products_dict(self):
        result = self.shopping_cart.add_to_cart("product", 80)
        self.assertEqual("product product was successfully added to the cart!", result)
        self.assertEqual({"product": 80}, self.shopping_cart.products)

    def test_remove_from_cart_method_product_not_in_cart_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart("product")
        self.assertEqual("No product with name product in the cart!", str(ve.exception))

    def test_remove_from_cart_method_product_updates_products_dict(self):
        self.shopping_cart.add_to_cart("product", 80)
        result = self.shopping_cart.remove_from_cart("product")
        self.assertEqual("Product product was successfully removed from the cart!", result)
        self.assertEqual({}, self.shopping_cart.products)

    def test__add__method_creates_new_instance(self):
        self.other_shopping_cart = ShoppingCart("Other", 100)
        result = self.shopping_cart.__add__(self.other_shopping_cart)
        self.assertEqual("TestOther", result.shop_name)
        self.assertEqual(200, result.budget)
        self.assertEqual({}, result.products)
        self.assertIsInstance(result, ShoppingCart)

    def test__add__method_creates_new_instance_and_adds_all_products_to_its_dict(self):
        self.other_shopping_cart = ShoppingCart("Other", 100)
        self.shopping_cart.add_to_cart("product", 10)
        self.other_shopping_cart.add_to_cart("other product", 20)
        result = self.shopping_cart.__add__(self.other_shopping_cart)
        self.assertEqual({"product": 10, "other product": 20}, result.products)

    def test__add__method_creates_new_instance_and_adds_other_products_to_its_dict(self):
        self.other_shopping_cart = ShoppingCart("Other", 100)
        self.other_shopping_cart.add_to_cart("other product", 20)
        result = self.shopping_cart.__add__(self.other_shopping_cart)
        self.assertEqual({"other product": 20}, result.products)

    def test_buy_products_method_total_sum_bigger_than_budget_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart('product', 80)
            self.shopping_cart.add_to_cart('product2', 80)
            self.shopping_cart.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 60.00lv!", str(ve.exception))

    def test_buy_products_returns_correct_message(self):
        self.shopping_cart.add_to_cart('product', 80)
        result = self.shopping_cart.buy_products()
        self.assertEqual("Products were successfully bought! Total cost: 80.00lv.", result)


if __name__ == "__main__":
    main()