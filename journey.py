budget = float(input())
season = input()

if season == "summer":
    if budget <= 100:
        hotel = budget * 0.30
        print("Somewhere in Bulgaria")
        print(f'Camp - {hotel:.2f}')
    elif budget <= 1000:
        hotel = budget * 0.40
        print("Somewhere in Balkans")
        print(f'Camp - {hotel:.2f}')
    else:
        hotel = budget * 0.90
        print("Somewhere in Europe")
        print(f'Hotel - {hotel:.2f}')

if season == "winter":
    if budget <= 100:
        hotel = budget * 0.70
        print("Somewhere in Bulgaria")
        print(f'Hotel - {hotel:.2f}')
    elif budget <= 1000:
        hotel = budget * 0.80
        print("Somewhere in Balkans")
        print(f'Hotel - {hotel:.2f}')
    else:
        hotel = budget * 0.90
        print("Somewhere in Europe")
        print(f'Hotel - {hotel:.2f}')
