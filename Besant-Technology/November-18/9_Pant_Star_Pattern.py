rows = 8            # number of lines
total_width = 16    # total characters per line

for i in range(rows):
    side_stars = (total_width // 2) - i        # 8 - i
    middle_underscores = total_width - 2 * side_stars  # 0,2,4,...
    line = "*" * side_stars + "_" * middle_underscores + "*" * side_stars
    print(line)

# OUTPUT

# ****************
# *******__*******
# ******____******
# *****______*****
# ****________****
# ***__________***
# **____________**
# *______________*