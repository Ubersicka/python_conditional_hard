user_input_day_to_stay = int(input())
user_input_type_of_room = input()
user_input_score = input()

price_modefyer = 1
price_for_stay = 0
if user_input_type_of_room == "president apartment":
    price_for_stay = 35
    if user_input_day_to_stay < 10:
        price_modefyer = 0.90
    elif user_input_day_to_stay < 15:
        price_modefyer = 0.85
    else:
        price_modefyer = 0.80
elif user_input_type_of_room == "apartment":
    price_for_stay = 25
    if user_input_day_to_stay < 10:
        price_modefyer = 0.70
    elif user_input_day_to_stay < 15:
        price_modefyer = 0.65
    else:
        price_modefyer = 0.50
else:
    price_for_stay = 18

total_price_for_stay = (user_input_day_to_stay - 1) * price_for_stay * price_modefyer
if user_input_score == "positive":
    total_price_for_stay += total_price_for_stay * 0.25
else:
    total_price_for_stay -= total_price_for_stay * 0.1

print(f"{total_price_for_stay:.2f}")
