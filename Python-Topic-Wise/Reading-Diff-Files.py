import pandas as pd

# 1. Read CSV file in Python

file_path = 'Python-Topic-Wise/CSV_File_Imported.csv'
readcsv = pd.read_csv(file_path)
print("-----Reading CSV file in Python-----\n")
print(readcsv)
print("")

#      Name Language       City
# 0   Vijay   Python     Nellai
# 1  Swathi     Java  Thanjavur
# 2   Raman      SQL    Chennai

# 2. Read Excel file in Python

file_path = 'Python-Topic-Wise/Excel_File_Imported.xlsx'
readexcel = pd.read_excel(file_path)
print("-----Reading Excel file in Python-----\n")
print(readexcel.head())
print("")

#          Train Name           From       To
# 0         Nellai SF         Nellai  Chennai
# 1  Kanniyakumari SF  Kanniyakumari  Chennai
# 2        Uzhavan SF      Thanjavur  Chennai
# 3       Pandiyan SF        Madurai  Chennai
# 4       Rockfort SF         Trichy  Chennai

# 3. Read Text file in Python

file_data = open('Python-Topic-Wise/Text_File_Imported.txt','r')
print("-----Reading Text file in Python using simple method-----\n")
print(file_data.read())
file_data.close()
print("")

# Hi this is Vijay
# From Tirunelveli

with open('Python-Topic-Wise/Text_File_Imported.txt','r') as file:
    print("-----Reading Text file in Python using with method-----\n")
    print(file.readlines())
    print("")

# ['Hi this is Vijay\n', 'From Tirunelveli']

# 4. Copying Image file in Python - This will print the binary code of Image you can copied image using this

# read_img = open('Python-Topic-Wise/Image.jpg','rb')
# # print(read_img.read())

# copied_img = open('Python-Topic-Wise/Copied_File_Image.jpg','wb')
# for byt in read_img:
#     copied_img.write(byt)

# 5. Importing an Image in Python using cv2 library

import cv2

 # Load an image
img = cv2.imread("Python-Topic-Wise/Image.jpg") # Replace "your_image.png" with your image file path

# Check if the image was loaded successfully
if img is None:
    print("Error: Could not load the image.")
else:
    print("Image loaded successfully!")
    new_width = 1000
    new_height = 700
    resized_image = cv2.resize(img, (new_width, new_height))
    # Display the image
    cv2.imshow("Resized Image", resized_image)
    cv2.waitKey(0) # Waits indefinitely until a key is pressed
    cv2.destroyAllWindows() # Destroys all opened OpenCV windows