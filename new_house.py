type_flowers = input()
count_flowes = int(input())
budget = int(input())

#Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.
#Not enough money, you need {нужната сума} leva more.

if type_flowers == "Roses":
    roses = 5
    total_price = count_flowes * roses
    if count_flowes > 80:
        discount = roses - roses * 0.10
        total_price = count_flowes * discount
elif type_flowers == "Dahlias":
    dahlias = 3.80
    total_price = count_flowes * dahlias
    if  count_flowes > 90:
        discount = dahlias - dahlias * 0.15
        total_price = count_flowes * discount
elif type_flowers == "Tulips":
    tulips = 2.80
    total_price = count_flowes * tulips
    if count_flowes > 80:
        discount = tulips - tulips * 0.15
        total_price = count_flowes * discount
elif type_flowers == "Narcissus":
    narcissus = 3
    total_price = count_flowes * narcissus
    if count_flowes < 120:
        discount = narcissus + narcissus * 0.15
        total_price = count_flowes * discount
elif type_flowers == "Gladiolus":
    gladious = 2.50
    total_price = count_flowes * gladious
    if count_flowes < 80:
        discount = gladious + gladious * 0.20
        total_price = count_flowes * discount

result = abs(total_price-budget)

if total_price <= budget:
    print (f'Hey, you have a great garden with {count_flowes} {type_flowers} and {result:.2f} leva left.')
elif total_price > budget:
    print (f'Not enough money, you need {result:.2f} leva more.')







