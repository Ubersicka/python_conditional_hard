# num = int(input())
#
# if num >= -100 and num <= 100 and num != 0:
#     print ("Yes")
# else:
#     print("No")

    #Stava i taka
if num >= -100:       #ВЛОЖЕНА ПРОВЕРКА
    if num <= 100:
        if num != 0:
            print("Yes")
        else:
            print("No")
