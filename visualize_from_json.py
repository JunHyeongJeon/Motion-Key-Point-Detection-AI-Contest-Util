#-*- coding:utf-8 -*-

# TODO: need refactoring

import numpy as np
import cv2
import json
import os
from tqdm import tqdm 

# IMAGE_FOLDER_PATH = "D:\\keypoint\\daycon\\train_imgs"
# JSON_FILE_PATH = "D:\\keypoint\\daycon\\person_keypoints_train_daycon.json"
IMAGE_FOLDER_PATH = "D:\\keypoint\\val2017"
JSON_FILE_PATH = "D:\\keypoint\\annotations\\person_keypoints_val2017.json"

OUTPUT_FOLDER_PATH = ".\\val"
HOW_MANY = 0 # all = 0

COLOR_WHITE = (255, 255, 255)
COLOR_RED = (0, 0, 255)

def get_image_meta(json_file_path):
    with open(json_file_path) as json_file:
        json_data = json.load(json_file, encoding='utf-8')
        return json_data

def tag_image_annotation(image_meta, image_annotation_list):
    # TODO: for문으로 수정


    target_image_name = image_meta["file_name"]
    target_image_id = image_meta["id"]
    target_image_path = os.path.join(IMAGE_FOLDER_PATH, target_image_name)
    target_image_keypoints = []
    for image_annotation in image_annotation_list :
        if image_annotation["id"] == target_image_id:
            if image_annotation["category_id"] != 1:
                return 
            print(int(image_annotation["category_id"]))
            target_image_keypoints = list(divide_list(image_annotation["keypoints"], 3))
            break
    if len(target_image_keypoints) == 0:
        return 

    img = cv2.imread(target_image_path, cv2.IMREAD_COLOR)
    for index, keypoint in enumerate(target_image_keypoints):
        target_point = (int(keypoint[0]), int(keypoint[1]))
        if (target_point[0] == 0) and (target_point[1] == 0):
            continue
        img = cv2.circle(img, target_point, 10, COLOR_RED, 1)
        cv2.putText(img,  str(index), target_point, cv2.FONT_HERSHEY_SIMPLEX, 0.6, COLOR_WHITE, 1, cv2.LINE_AA)


    output_image_path = os.path.join(OUTPUT_FOLDER_PATH, target_image_name)
    cv2.imwrite(output_image_path, img)
    k = cv2.waitKey()


def divide_list(l, n): 
    for i in range(0, len(l), n): 
        yield l[i:i + n] 


if __name__ == "__main__":
    meta = get_image_meta(JSON_FILE_PATH)
    image_meta_list = meta["images"]
    image_annotation_list = meta["annotations"]
    for index, image_meta in enumerate(tqdm(image_meta_list)):
        if (index > HOW_MANY) and HOW_MANY != 0:
            break
        tag_image_annotation(image_meta, image_annotation_list)