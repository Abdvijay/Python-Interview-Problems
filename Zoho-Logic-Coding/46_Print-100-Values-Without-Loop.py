def printing(number):
    if number > 100:
        return
    print(number)
    printing(number+1)
printing(1)