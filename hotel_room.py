month = input()
count_nights = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartament_price = 65
    if count_nights <= 7:
        pass
    elif count_nights <= 14:
        studio_price *= 0.95
    elif count_nights > 14:
        studio_price *= 0.70
        apartament_price *= 0.90
elif month == "June" or month == "September":
    studio_price = 75.20
    apartament_price = 68.70
    if count_nights <= 14:
        pass
    elif count_nights > 14:
        studio_price *= 0.80
        apartament_price *= 0.90
elif month == "July" or month == "August":
    studio_price = 76
    apartament_price = 77
    if count_nights <= 14:
        pass
    elif count_nights > 14:
        apartament_price *= 0.90

total_price_apartment = count_nights * apartament_price
total_price_studio = count_nights * studio_price
print(f'Apartment: {total_price_apartment:.2f} lv.')
print(f'Studio: {total_price_studio:.2f} lv.')
