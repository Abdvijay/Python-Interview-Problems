def printing(number, limit = 100):
    if number > 100:
        return
    print(number)
    printing(number+1,limit)
printing(1)