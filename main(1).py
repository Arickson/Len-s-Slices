# Define toppings and their respective prices
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

# Calculate the number of toppings priced at $2
num_two_dollar_slices = prices.count(2)

# Calculate the total number of pizza varieties
num_pizza = len(toppings)

# Print the message about the different kinds of pizza sold
print(f"We sell {num_pizza} different kinds of pizza!")

# Define a list of lists containing prices and toppings
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

# Sort the list based on price (ascending order)
pizza_and_prices.sort()

# Identify the cheapest and priciest pizza
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

# Remove the last item from the list
pizza_and_prices.pop()

# Insert a new pizza with price $2.5 and topping "peppers" at index 1
pizza_and_prices.insert(1, [2.5, "peppers"])

# Sort the list again after modification
pizza_and_prices.sort()

# Get the three cheapest pizzas
three_cheapest = pizza_and_prices[0:3]

# Print the three cheapest pizzas and the modified list
print("Updated Pizza List:", pizza_and_prices)