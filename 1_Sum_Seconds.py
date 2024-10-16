seconds_first = int(input())
seconds_second = int(input())
seconds_third = int(input())

total_seconds = seconds_first + seconds_second + seconds_third
minutes = total_seconds // 60  #121 // 60 == 2 deli i dava cyaloto chisto, bez ostatyk
seconds = total_seconds % 60 #121 % 60 == 1  dava ni ostatyka

if seconds >= 10:
    print(f"{minutes}:{seconds}")
else:
    print(f"{minutes}:0{seconds}")