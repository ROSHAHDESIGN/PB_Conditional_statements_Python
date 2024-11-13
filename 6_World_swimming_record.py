# На конзолата се въвежда рекордът в секунди, който Иван трябва да подобри,
import math

swimm_record_in_seconds =  float(input())
# разстоянието в метри,
distance_in_meters = float(input())
# което трябва да преплува и времето в секунди, за което плува разстояние от 1 м.
swimmingtime_sec_per_meter = float(input())

#съпротивлението на водата го забавя
# на всеки 15 м. с 12.5 секунди.
swimm_time1 = distance_in_meters * swimmingtime_sec_per_meter
resistance_time_each_15m = (math.floor(distance_in_meters / 15)) * 12.5
total_time = swimm_time1 + resistance_time_each_15m

if total_time < swimm_record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
if total_time >= swimm_record_in_seconds:
    needed_seconds = total_time- swimm_record_in_seconds
    print(f"No, he failed! He was {needed_seconds:.2f} seconds slower.")
