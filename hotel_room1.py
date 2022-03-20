month = input()
number_of_days = int(input())
price_per_day_studio = 0
price_per_day_apartment = 0

if month == "May" or month == "October":
    price_per_day_studio = 50
    price_per_day_apartment = 65
elif month == "June" or month == "September":
    price_per_day_studio = 75.20
    price_per_day_apartment = 68.70
elif month == "July" or month == "August":
    price_per_day_studio = 76
    price_per_day_apartment = 77

if 7 < number_of_days <= 14 and month == "May" or month == "October":
    price_per_day_studio *= 0.95
elif number_of_days > 14 and month == "May" or month == "October":
    price_per_day_studio *= 0.70

if number_of_days > 14 and month == "June" or month == "September":
    price_per_day_studio *= 0.80

if number_of_days > 14:
    price_per_day_apartment *= 0.90

total_price_apartment = number_of_days * price_per_day_apartment
total_price_studio = number_of_days * price_per_day_studio

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
