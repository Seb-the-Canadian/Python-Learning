# 2025-11-17.pß

# creating a dictionary

# recipe = {
# "pasta": 500,
# "tomatoes": 400,
# "garlic": 15,
# "basil": 20,
# "olive oil": 30,
# "salt": 5,
# }

# How much pasta do we need? - Find the quantity.

# print(recipe["pasta"])

# To get all values from a dictionary, use the .values function.

# print(recipe.values())

# To get all keys from a dictionary, use the .keys function.

# print(recipe.keys())

# To get all items as key-value pairs, we can use the .items function.

# print(recipe.items())

# To add a new key-value pair:

# recipe["parmesan"] = 50
# print(recipe)

# To update a new key-value:

# recipe["pasta"] = 1000
# print(recipe)

# You can store and print the values returned.

# Get all ingredient names
# ingredient_names = print(recipe.keys())

# Get all quantities
# quantities = print(recipe.values())

# Get all key-value pairs
# recipe_items = print(recipe.items())

# ingredient_names = recipe.keys()
# quantities = recipe.values()
# recipe_items = recipe.items()

# print("Ingredient names:", ingredient_names)
# print("Quantities:", quantities)
# print("Recipe items:", recipe_items)


# Creating a set of ingredients
ingredients = {"pasta", "tomatoes", "pasta", "basil", "garlic", "olive oil", "salt"}
# print(ingredients)

# Existing list vairable
# ingredients_list = ["pasta", "tomatos", "garlic", "basil", "olive oil", "pasta", "salt"]

# Convert to a set
# unique_ingredients = set(ingredients_list)

# Check the data type
# print(type(unique_ingredients))

# print(unique_ingredients)

# Sorting a set
# print(sorted(ingredients))

# Creating a tuple
# serving_sizes = (1, 2, 4, 6, 8)

# Convert another data structure into a tuple

# ingredients_tuple = tuple(ingredients_list)

# Access tuple elements

# print(serving_sizes[1])
