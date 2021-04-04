#-*- coding:utf-8 -*-
import cv2
import os
from tqdm import tqdm 
from _utils import *
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_folder_path', type=str, help='이미지들이 있는 경로', 
        default='C:\\Users\\Jun\\Downloads\\1. open\\test_imgs') 
    parser.add_argument('--csv_file_path', type=str, help=' CSV파일이 있는 경로',     
        default='C:\\Users\\Jun\\Downloads\\submission_new_version_2_bugfix.csv')
    parser.add_argument('--output_folder_path', type=str, help='출력물이 있을 폴더',
        default='.\\output')
    parser.add_argument('--how_many', type=int, help='몇개나 이미지를 처리할지 0이면 전체',
        default=10)
    return parser.parse_args()

def visualize_image_annotation(image_metas):
    target_image_name = image_meta["image_name"]
    target_image_path = os.path.join(args.image_folder_path, target_image_name)
 
    img = cv2.imread(target_image_path, cv2.IMREAD_COLOR)
    for index, keypoint_name in enumerate(KEYPOINT_LIST):
        target_coordinate = set_coordinate_as_int(image_meta[keypoint_name]) 
        if is_xy_list_coordinate_exist(target_coordinate):
            continue    
        img = cv2.circle(img, target_coordinate, 3, COLOR_RED, 1)
        cv2.putText(img,  keypoint_name, target_coordinate, cv2.FONT_HERSHEY_SIMPLEX, 0.4, COLOR_WHITE, 1, cv2.LINE_AA)

    make_dir(args.output_folder_path)
    output_folder_path_with_csv_name = os.path.join(args.output_folder_path, get_csv_file_name(args.csv_file_path))
    make_dir(output_folder_path_with_csv_name)

    output_image_path = os.path.join(output_folder_path_with_csv_name, target_image_name)
    cv2.imwrite(output_image_path, img)

def get_image_meta_for_visualize(csv_file_path):
    image_meta_list = []
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for index, row in enumerate(reader):
            image_meta = {}
            image_meta["image_name"] = row['image']
            for keypoint in KEYPOINT_LIST:
                image_meta[keypoint] = get_row_data(row, keypoint)  
            image_meta_list.append(image_meta)

    return image_meta_list


if __name__ == "__main__":
    global args
    args = parse_args()

    metas = get_image_meta_for_visualize(args.csv_file_path)
    for index, image_meta in enumerate(tqdm(metas)):
        if (index > args.how_many) and args.how_many != 0:
            break
        visualize_image_annotation(image_meta)