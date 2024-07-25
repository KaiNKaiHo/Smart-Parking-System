from FaceID.Check_id import check_ID
from PLDetect.pl_detect import run_and_detect
from Read_PL.read_pl import read_pl
from SupaBase import database as db


def run_pl(image_path):
    crop_img = run_and_detect(img_path=image_path)
    pl_text = read_pl(crop_img)
    return pl_text

def get_img_name(img_path):
    img_name = ''
    count = -1
    i = img_path[count]
    while i != '/':
        img_name += img_path[count]
        count -= 1
        i = img_path[count]
        if -count == len(img_path):
            img_name += img_path[count]
            break
    return img_name[::-1]
        
def insert_data(pl_img_path, face_img_path, table_name):
    pl_text = run_pl(pl_img_path)
    db.insert(table_name, pl_text, get_img_name(pl_img_path), get_img_name(face_img_path))

# Code for run_pl
# text = run_pl('D:/Cuong/Project/Face/PLDetect/yolov9/data/test/images/0002_02183_b.jpg')
# print(text)

def run_face(image_path1, image_path2):
    return check_ID(img_path1=image_path1, img_path2=image_path2)