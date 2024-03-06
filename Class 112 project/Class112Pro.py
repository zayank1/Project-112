import os
import shutil

from_dir = "C:/Users/Zayan.K/Downloads"
to_dir = "C:/Users/Zayan.K/Desktop/BYJUS/Class112 downloads"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension=='':
        continue
    if extension in ['.pdf','.docx','.doc','.txt']:
         path1 = from_dir + '/' + file_name
         path2 = to_dir + '/' + "ImageFiles"
         path3 = to_dir + '/' + "ImageFiles" + '/' + file_name

         if os.path.exists(path2):
             print("Moving" + file_name + "......")
             shutil.move(path1,path3)
         else:
             os.makedirs(path2)
             print("Moving" + file_name + "......." )  
             shutil.move(path1,path3)  
          