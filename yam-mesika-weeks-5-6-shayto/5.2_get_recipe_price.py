
def get_recipe_price(ingredients_prices=dict, optional_ingredients=list(), **ingredients_quantity):

    """
    function to get ingredients, optionals ingredients and their quantity.
    the function returns the total price it costs to make the recipe.
    :param ingredients_prices: Map of ingredients and their price per 100 grams
    :param optional_ingredients: List of optional ingredients from the list which will not be calculated
    :param ingredients_quantity: The quantity in grams needed for each ingredient.
    :return: The price for making the recipe.
    """
    return sum(ingredients_quantity[key] / 100 * ingredients_prices[key]
               for key in ingredients_prices.keys() if key not in optional_ingredients)


if __name__ == '__main__':
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
