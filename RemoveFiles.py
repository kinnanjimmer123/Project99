import os
import shutil
import time

days = 30
seconds = time.time()

if os.path.exists(path+'/'+ext):
        os.walk(path)
        for file in list_of_files:
        name, ext = os.path.splitext(file)
        os.path.join()

        ext = ext[1:]
        if days > 30:
             os.remove(path)

        else:
          
            print("Not found")
            break



list_of_files = os.listdir(path)