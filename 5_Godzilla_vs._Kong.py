budget = float(input())
actors_count = int(input())
price_cloths = float(input())

decors_cost = budget * 0.1
cloths_costs = actors_count * price_cloths
if actors_count > 150:
    cloths_costs *= 0.9
movie_costs = decors_cost + cloths_costs
left_money = budget - movie_costs

if budget >= movie_costs:
    print("Action!")
    print(f"Wingard starts filming with {left_money:.2f} leva left.")

else:
    print("Not enough money!")
    print(f"Wingard needs {abs(left_money):.2f} leva more.")
