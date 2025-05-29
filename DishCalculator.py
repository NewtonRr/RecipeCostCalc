#dish cost calculator (somehow useful)
#used to calculate the aprox. cost of a recipe.
import os

costs = {}

def calculate_cost_single_ingredient():
    ingredient_name = input("Enter the name of the ingredient: ")
    ingredient_cost = input("Enter the cost of the ingredient: ")
    ingredient_unit = input("Enter the unit of the ingredient (g, u(unit), ml): ").lower().strip()
    ingredient_quantity = input(f"Enter the quantity of the ingredient (in {ingredient_unit}): ")

    #check if unit is valid
    valid_units = ['g', 'u', 'ml']
    if ingredient_unit not in valid_units:
        print(f"Invalid unit '{ingredient_unit}'. Valid units are: {', '.join(valid_units)}")
        return

    #check if ingredient already exists
    if ingredient_name in costs:
        print(f"{ingredient_name} already exists with a cost of {costs[ingredient_name]:.2f}.")
        return costs
    
    # Check if the ingredient name is valid
    if not ingredient_name.strip():
        print("Ingredient name cannot be empty. Please try again.")
        return

    # check if Validate inputs
    try:
        ingredient_cost = float(ingredient_cost)
        ingredient_quantity = float(ingredient_quantity)
    except ValueError:
        print("Invalid input. Please enter numeric values for cost and quantity.")
        return

    # Calculate cost per amount
    try:
        cost_per_unit = ingredient_cost / ingredient_quantity
        costs[ingredient_name] = [cost_per_unit, ingredient_unit]
        print(f"Added {ingredient_name} with cost {cost_per_unit:.4f} per {ingredient_unit}.")
    
    except ZeroDivisionError:
        print("Quantity cannot be zero. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Cost calculation complete.")
    return costs

def current_costs():
    if not costs:
        print("No ingredients have been added yet.")
    else:
        print("Current ingredient costs:")
        for ingredient, (cost, unit) in costs.items():
            print(f"{ingredient}: {cost:.2f} per {unit}")

def calculate_total_cost():
    total_cost = 0
    for ingredient, (cost, unit) in costs.items():
        print(f"{ingredient}: {cost:.2f} per {unit}")
        amount = input(f"Enter the amount of {ingredient} you want to use (in {unit}): ")
        try:
            amount = float(amount)
            cost *= amount
        except ValueError:
            print(f"Invalid amount for {ingredient}. Please enter a numeric value.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
        total_cost += cost
    return total_cost

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Dish Cost Calculator")
    calculate_cost_single_ingredient()

    ask = input("Do you want to see the current costs? (yes/no): ").strip().lower()
    if ask == 'yes':
        current_costs()
    ask = input("Do you want to add another ingredient? (yes/no): ").strip().lower()
    if ask == 'yes':
        continue
    ask = input("Do you want to calculate the total cost of the dish? (yes/no): ").strip().lower()
    if ask == 'yes':
        total_cost = calculate_total_cost()
        print(f"The total cost of the dish is: {total_cost:.2f}")
        ask = input("Do you want to exit? (yes/no): ").strip().lower()
        if ask == 'yes':
            print("Exiting the Dish Cost Calculator. Goodbye!")
            break

