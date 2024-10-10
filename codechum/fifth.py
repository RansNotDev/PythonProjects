days_of_week = {
    'Sunday': 0,
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6
}
reverse_days_of_week = {v: k for k, v in days_of_week.items()}
def calculate_day_of_week(today, days_ahead):
    current_day = days_of_week[today]
    future_day = (current_day + days_ahead) % 7
    weeks_later = days_ahead // 7
    future_day_name = reverse_days_of_week[future_day]
    if weeks_later == 0:
        print(f"{days_ahead} days later will be {future_day_name}")
    else:
        print(f"{days_ahead} days later will be {future_day_name}, {weeks_later} week/s later.")
today = input("What day is today? ").capitalize()
days_ahead = int(input("How many days ahead? "))
calculate_day_of_week(today, days_ahead)