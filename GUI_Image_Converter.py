import os
from PIL import Image
import glob
from tkinter import Tk, filedialog

print("Welcome to Photo Resize and Converter V1.0")
print("Loading...")

print('''
What do you want?
(1) Resize images and convert to JPG
(2) Convert to JPG Only
Copyright (c) Ehab Nada 2022
''')

while True:
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    choice = input("Choice: ")

    if choice == "1":
        open_file = filedialog.askdirectory()
        images = glob.glob(open_file+ "/"+"*.*")
        for image in images:
            img = Image.open(image)
            img_name = img.filename[29:37]
            with open(image, 'rb') as file:
                img_2 = Image.open(file)
                resized_img = img_2.resize((292, 400))
                new_path = open_file + "/"+"resized"
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                resized_img_path = new_path + f"\\"
                resized_img.save(resized_img_path + img_name + '.jpg')
        print('Done ...')
        break

    elif choice == "2":
        open_file = filedialog.askdirectory()
        images = glob.glob(open_file+ "/"+"*.*")
        for image in images:
            img = Image.open(image)
            img_name = img.filename[29:37]
            with open(image, 'rb') as file:
                img_2 = Image.open(file)
                new_path = open_file + "/"+"converted"
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                converted_img_path = new_path + f"\\"
                img_2.save(converted_img_path + img_name + '.jpg')
        print('Done ... ')
        break
    else:
        print("Invalid input! pLease Enter A valid Input...")