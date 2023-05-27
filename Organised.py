import os
import shutil

list_of_files=os.listdir("C102_assets-main")

print(list_of_files)

for file in list_of_files:
    name,ext=os.path.splitext(file)
    #print(name)
    #print(ext)
    if ext==" ":
        continue
    if ext in [".gif",".png",".jfif",".jpg",".jpeg"]:
        path1="C102_assets-main"+"/"+file
        path2="C102_assets-main"+"/"+"imageFiles"
        path3="C102_assets-main"+"/"+"imageFiles"+file

        if os.path.exists(path2):
            print("moving  "+file+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving  "+file+"...")
            shutil.move(path1,path3)