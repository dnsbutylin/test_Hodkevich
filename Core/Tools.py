import os, os.path, shutil
import hashlib

#PATH_TO_PICTURE = "C:\\Vg3bhs0RG1g.jpg"
PICTURE_NAME = 'Vg3bhs0RG1g.jpg'
USERNAME = 'testaccount.2000'
PASSWORD = 'qwe321!qwe'


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def remove_folder_contents(path):
    shutil.rmtree(path)
    os.makedirs(path)



