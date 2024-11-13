import math

movie_name = input()
movie_length = int(input())
lunch_break_length = int(input())


time_for_lunch = lunch_break_length / 8
time_for_rest = lunch_break_length /4
time_left = lunch_break_length - time_for_rest- time_for_lunch
minutes_left = abs(time_left- movie_length)

if time_left >= movie_length:
    print(f"You have enough time to watch {movie_name} and left with {math.ceil(minutes_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, "
          f"you need {math.ceil(minutes_left)} more minutes.")
