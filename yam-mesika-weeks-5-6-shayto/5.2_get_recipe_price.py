def get_recipe_price(prices=dict, optionals=list(), **quantity):
    # function to get ingredients, optionals ingredients and their quantity
    # the function returns the price for making the recipe.
    # the function gets prices: Map of ingredients and their price per 100 grams
    # optionals: List of optional ingredients from the list which will not be calculated
    # quantity: The quantity in grams needed for each ingredient.
    # the function returns the total price it costs to make the recipe.
    sum_of_ingredients = 0
    for key in prices.keys():
        if key not in optionals:
            sum_of_ingredients += (quantity[key] / 100 * prices[key])
    return sum_of_ingredients


if __name__ == '__main__':
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
