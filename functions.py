import os
from PIL import Image
from pathlib import Path


def create_subdirs(dirpath):
    directory_path = Path(dirpath)

    for path in list(directory_path.iterdir()):

        full_name = os.path.basename(path)
        name = os.path.splitext(full_name)[0]
        # print(str(name))
        subdir = Path(dirpath + "\\" + name)
        print(str(subdir))

        try:
            os.makedirs(subdir)
        except OSError:
            print ("Создать директорию %s не удалось" % subdir)
        else:
            print ("Успешно создана директория %s" % subdir)


def cut_image(parentdir):

    parent_dir = Path(parentdir)

    for elem in list(parent_dir.iterdir()):
        if elem.is_dir():

            full_name = os.path.basename(elem)
            name = os.path.splitext(full_name)[0]
            # print(str(name))
            subdir = Path(parentdir + "\\" + name)
            print(str(subdir))

            for item in list(subdir.iterdir()):
                print(str(item))
                img = Image.open(item)
                w, h = img.size
                # Ахтунг! Для разрешения 300 px/inch
                # area = (10, 70, 4940, 3300)
                area = (10, 70, w-20, h-195)
                cropped_img = img.crop(area)
    
                # cropped_img.show()
                cropped_img.save(item)
    return
