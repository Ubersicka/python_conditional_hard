#"I'ts {градуси} degrees, get your {облекло} and {обувки}."

degrees = int(input())
time_of_the_day = input()

outfit = ""
shoes = ""

if time_of_the_day == "Morning":
    if 10 <= degrees <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degrees >= 25: # else:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif time_of_the_day == "Afternoon":
    if 10 <= degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < degrees <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif degrees >= 25: # else:
        outfit = "Swim Suit"
        shoes = "Barefoot"
elif time_of_the_day == "Evening":  #може и да е else: вместо elif
    outfit = "Shirt"
    shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
