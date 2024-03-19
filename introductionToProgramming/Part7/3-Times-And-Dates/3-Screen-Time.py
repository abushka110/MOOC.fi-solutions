# solution
from datetime import timedelta, datetime

filename = input("Filename: ")
start_date = input("Starting date: ")
start_date = datetime.strptime(start_date, "%d.%m.%Y")
print(start_date)
days_plus = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")

screen_time_data = {}

end_date = start_date
screen_time = input(f'Screen time {end_date.strftime("%d.%m.%Y")}: ')
screen_time_data[end_date.strftime("%d.%m.%Y")] = screen_time.replace(" ", "/")

for i in range(days_plus - 1):
    end_date += timedelta(days = 1)
    screen_time = input(f'Screen time {end_date.strftime("%d.%m.%Y")}: ')
    screen_time_data[end_date.strftime("%d.%m.%Y")] = screen_time.replace(" ", "/")

print(screen_time_data)

with open(filename, "w") as write_file:
    write_file.write(f'Time period: {start_date.strftime("%d.%m.%Y")}-{end_date.strftime("%d.%m.%Y")}\n')
    # write total minutes
    total_time = 0
    for key in screen_time_data.keys():
        time = screen_time_data[key].split("/")
        total_time += int(time[0]) + int(time[1]) + int(time[2])
    write_file.write(f'Total minutes: {total_time}\n')
    write_file.write(f'Average minutes: {total_time / days_plus}\n')
    
    for key in screen_time_data.keys():
        write_file.write(f'{key}: {screen_time_data[key]}\n')

print("Data stored in file late_june.txt")