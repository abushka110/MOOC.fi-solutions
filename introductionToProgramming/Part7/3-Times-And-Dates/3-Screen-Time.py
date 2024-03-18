# solution
from datetime import timedelta, datetime

filename = input("Filename: ")
start_date = input("Starting date: ")
start_date = datetime.strptime(start_date, "%d.%m.%Y")
print(start_date)
days_plus = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")

screen_time_data = []

with open(filename, "a") as write_file:
    for i in range(days_plus):
        current_date = start_date + timedelta(days = i)
        screen_time = input(f'Screen time {current_date.strftime("%d.%m.%Y")}: ')
        screen_time_data.append(f'{current_date.strftime("%d.%m.%Y")}: {screen_time.replace(" ", "/")}')

# # Calculating total and average minutes
# total_minutes = 0
# for day in screen_time_data:
#     for minutes in day.split('/'):
#         total_minutes += int(minutes)

# average_minutes = total_minutes / days_plus

# # Writing summary to the file
# with open(filename, "a") as write_file:
#     write_file.write(f'Time period: {start_date.strftime("%d.%m.%Y")}-{(start_date + timedelta(days=days_plus-1)).strftime("%d.%m.%Y")}\n')
#     write_file.write(f'Total minutes: {total_minutes}\n')
#     write_file.write(f'Average minutes: {average_minutes}\n')

#     # Writing screen time data
#     for i in range(days_plus):
#         current_date = start_date + timedelta(days=i)
#         write_file.write(f'{current_date.strftime("%d.%m.%Y")}: {screen_time_data[i].replace(" ", "/")}\n')

print("Data stored in file late_june.txt")

# test
if __name__ == "__main__":
    pass  # Add your test code here
