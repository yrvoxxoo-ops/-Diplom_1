import allure
import pytest


@allure.feature("Burger")
class TestBurger:

    @allure.title("Проверка установки булки в бургер")
    def test_set_buns_sets_bun(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    @allure.title("Проверка добавления ингредиента в бургер")
    def test_add_ingredient_adds_ingredient(self, burger, sauce):
        burger.add_ingredient(sauce)
        assert burger.ingredients == [sauce]

    @allure.title("Проверка добавления нескольких ингредиентов в бургер")
    def test_add_several_ingredients_adds_all_ingredients(self, burger, sauce, filling):
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        assert burger.ingredients == [sauce, filling]

    @allure.title("Проверка удаления ингредиента из бургера по индексу")
    def test_remove_ingredient_removes_ingredient_by_index(self, burger, sauce, filling):
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        burger.remove_ingredient(0)
        assert burger.ingredients == [filling]

    @allure.title("Проверка ошибки при удалении ингредиента по несуществующему индексу")
    def test_remove_ingredient_with_invalid_index_raises_error(self, burger, sauce):
        burger.add_ingredient(sauce)
        with pytest.raises(IndexError):
            burger.remove_ingredient(5)

    @allure.title("Проверка перемещения ингредиента в бургере")
    def test_move_ingredient_moves_ingredient_to_new_index(self, burger, sauce, filling):
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [filling, sauce]

    @allure.title("Проверка перемещения ингредиента на несуществующий новый индекс")
    def test_move_ingredient_to_invalid_new_index_moves_ingredient_to_end(self, burger, sauce, filling):
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        burger.move_ingredient(0, 10)
        assert burger.ingredients == [filling, sauce]

    @allure.title("Проверка ошибки при перемещении ингредиента с несуществующего индекса")
    def test_move_ingredient_with_invalid_index_raises_error(self, burger, sauce):
        burger.add_ingredient(sauce)
        with pytest.raises(IndexError):
            burger.move_ingredient(5, 0)

    @allure.title("Проверка расчета цены бургера с булкой и ингредиентами")
    def test_get_price_returns_sum_of_bun_twice_and_ingredients(self, burger, bun, sauce, filling):
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        assert burger.get_price() == 320

    @allure.title("Проверка расчета цены бургера без ингредиентов")
    def test_get_price_without_ingredients_returns_bun_price_twice(self, burger, bun):
        burger.set_buns(bun)
        assert burger.get_price() == 200

    @allure.title("Проверка ошибки при расчете цены бургера без булки")
    def test_get_price_without_bun_raises_error(self, burger, sauce):
        burger.add_ingredient(sauce)
        with pytest.raises(AttributeError):
            burger.get_price()

    @allure.title("Проверка формирования рецепта бургера с булкой и ингредиентами")
    def test_get_receipt_returns_correct_receipt(self, burger, bun, sauce, filling):
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 320")

        assert burger.get_receipt() == expected_receipt

    @allure.title("Проверка формирования рецепта бургера без ингредиентов")
    def test_get_receipt_without_ingredients_returns_receipt_with_only_bun(self, burger, bun):
        burger.set_buns(bun)

        expected_receipt = (
            "(==== black bun ====)\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 200")

        assert burger.get_receipt() == expected_receipt

    @allure.title("Проверка ошибки при формировании рецепта без булки")
    def test_get_receipt_without_bun_raises_error(self, burger, sauce):
        burger.add_ingredient(sauce)
        with pytest.raises(AttributeError):
            burger.get_receipt()