puzzle = 2.60
doll = 3
teddy_bear = 4.10
minion = 8.20
truck = 2

#входни данни
vacation_cost = float(input())
puzzle_count = int(input())
dolls_count = int(input())
teddy_bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

#общия брой играчк(печалбата)
income = (puzzle_count * 2.6 + dolls_count * 3 +
          teddy_bear_count * 4.1 + minion_count * 8.20 +
          truck_count * 2)
# това е дискаунта и се дефинира като променлива
discount = 0

#тук се изчисляваобщият брой поръчки
total_count = (puzzle_count + dolls_count + teddy_bear_count +
                minion_count + truck_count)
if total_count >= 50:
    discount = 0.25

total_income = income * (1 - discount)

#10 % за наема се изваждат
final_income = total_income * 0.9

if final_income >= vacation_cost:
    # ако парите са повече(=) да се изчислят и отпечатат
    money_left = final_income - vacation_cost
    print(f"Yes! {money_left:.2f} lv left.")
else:
    # ако парите са по-малко да се изчислят и отпечатат
    needed_money = vacation_cost - final_income
    print(f"Not enough money! {needed_money :.2f} lv needed.")
