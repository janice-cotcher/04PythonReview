# Prints an arbitrary number of arguments

def make_pizza(*toppings):
  """Print the list of toppings that have been requested."""
  print("\nMaking a pizza with the following toppings:")
  for topping in toppings:
    print(f"- {topping}")

  
# Make a pizza with a few toppings

make_pizza("cheese", "pepperoni", "pineapple", "onions")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')