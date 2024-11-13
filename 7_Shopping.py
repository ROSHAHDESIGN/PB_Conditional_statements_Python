budget = float(input())
vc_count = int(input())
processors_count = int(input())
RAM_memory_count = int(input())

#•	Видеокарта – 250 лв./бр.
# •	Процесор – 35% от цената на закупените видеокарти/бр.
# •	Рам памет – 10% от цената на закупените видеокарти/бр.
VC_PRICE = 250

total_vc_cost = vc_count * VC_PRICE
total_processors_cost = processors_count * (total_vc_cost * 0.35)
total_ram_memory_cost = RAM_memory_count * (total_vc_cost * 0.10)

total_cost = total_vc_cost + total_processors_cost + total_ram_memory_cost

if vc_count > processors_count:
    total_cost = total_cost * 0.85

if total_cost <= budget:
    left_budget = budget - total_cost
    print(f"You have {left_budget:.2f} leva left!")
else:
    needed_money = total_cost - budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")
