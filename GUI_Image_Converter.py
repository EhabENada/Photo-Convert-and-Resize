import progressbar
import os
from PIL import Image, ImageFile
import glob
from tkinter import Tk, filedialog
import tqdm
import time
import readchar
import shutil

def animated_marker():
    widgets = ['Please Wait while starting program :) : ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
    for i in range(20):
        time.sleep(0.1)
        bar.update(i)


print('')

print('''
                                    Welcome to Photo Resize and Converter V 1.0
                                            Copyright (c) \x1b[6;30;42mEhab Nada\x1b[0m 2022
''')


# for i in tqdm.tqdm(range(20), colour="Green", desc='Please Wait while the program loading'):
#     time.sleep(0.5)


error_log = []
root = Tk()
root.withdraw()
root.attributes('-topmost', True)

animated_marker()

open_file = filedialog.askdirectory()
images = glob.glob(open_file + r"\\"+ "*.*")
img_count = len(next(os.walk(open_file))[-1])
progress_bar = tqdm.tqdm(range(img_count),  colour="YELLOW", desc='Please Wait while the program Converting Photos')

for i, image in zip(progress_bar,images):
    img = Image.open(image)
    img_name = os.path.splitext(os.path.basename(img.filename))[0]
    try:
        with open(image, 'rb') as file:
            img_1 = Image.open(file)
            ImageFile.LOAD_TRUNCATED_IMAGES = True
            rgb_im = img_1.convert('RGB')
            resized_img = rgb_im.resize((292, 400))
            new_path = open_file + "/"+"Resized"
            if not os.path.exists(new_path):
                os.makedirs(new_path)
            resized_img_path = new_path + f"\\"
            resized_img.save(resized_img_path + img_name + '.jpg')
            img_count2 = len(os.listdir(resized_img_path))
            time.sleep(0.01)
    except:
        error_path = open_file + "/"+"Errors"
        if not os.path.exists(error_path):
            os.makedirs(error_path)
        extension = os.path.splitext(os.path.basename(img.filename))[-1]
        shutil.copy(open_file+"/"+img_name+extension, error_path)

print(f"Total Number of selected Photos {img_count}")
print(f"Total Number of Converted Photos {img_count2}")
print(f"Total Number of Errors {img_count-img_count2}")

if img_count-img_count2 > 0 :
    print('''                            ##########################################################################
                            ##                    Please check Errors folder                        ##
                            ##              If there is no folder or files This Means               ##
                            ##       \33[41mthat there are duplicated Photos with another extension\33[0m        ##
                            ########################################################################## ''')
else:
    print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')

print("Press Any Key To Exit")
readchar.readchar()


