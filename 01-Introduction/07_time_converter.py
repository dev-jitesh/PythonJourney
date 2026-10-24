total_time = float(input("Enter time in large number of seconds: "))

time_in_hours = total_time // 3600
remaining_seconds = total_time % 3600

time_in_minutes = remaining_seconds // 60
time_in_seconds = remaining_seconds % 60

print("The time is " , time_in_hours, " hours" , time_in_minutes, " minutes" , time_in_seconds, " seconds")