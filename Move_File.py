import os
import shutil
from_dir = "C:/Users/kush2/Downloads"
to_dir = "C:/Users/kush2/OneDrive/Desktop/Kush_Projects/Document_Files"
list_of_files = os.listdir(from_dir)
#print(list_of_files)
for file in list_of_files:
    name, extension = os.path.splitext(file)
    print(name)
    print(extension)
