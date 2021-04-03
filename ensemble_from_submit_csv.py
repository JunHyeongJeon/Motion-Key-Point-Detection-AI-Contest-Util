#-*- coding:utf-8 -*-
import os
from tqdm import tqdm 
import csv
from _utils import *
import argparse
from itertools import chain
from collections import defaultdict
import json
import copy

KEYPOINT_XY_LIST = ["nose_x", "nose_y", 
                "left_eye_x", "left_eye_y", "right_eye_x", "right_eye_y", 
                "left_ear_x", "left_ear_y", "right_ear_x", "right_ear_y", 
                "left_shoulder_x", "left_shoulder_y", "right_shoulder_x", "right_shoulder_y", 
                "left_elbow_x", "left_elbow_y", "right_elbow_x", "right_elbow_y", 
                "left_wrist_x", "left_wrist_y", "right_wrist_x", "right_wrist_y", 
                "left_hip_x", "left_hip_y", "right_hip_x", "right_hip_y", 
                "left_knee_x", "left_knee_y", "right_knee_x", "right_knee_y", 
                "left_ankle_x", "left_ankle_y", "right_ankle_x", "right_ankle_y", 
                "neck_x", "neck_y", 
                "left_palm_x", "left_palm_y", "right_palm_x", "right_palm_y", 
                "spine2(back)_x", "spine2(back)_y", "spine1(waist)_x", "spine1(waist)_y", 
                "left_instep_x", "left_instep_y", "right_instep_x", "right_instep_y"]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv_files_path', type=str, help=' CSV파일들이 있는 경로',     
        default='C:\\Users\\Jun\\Downloads\\csv')
    parser.add_argument('--output_folder_path', type=str, help='출력물이 있을 폴더',
        default='.\\ensemble')
    return parser.parse_args()

def ensemble(in_data):
    
    return ensemble_result 
def cancat_result(csv_file_list):
    image_name_and_list_dict = {}

    for index, csv_file in enumerate(tqdm(csv_file_list)):          
        csv_file_path = os.path.join(args.csv_files_path, csv_file)
        image_meta = read_input_csv_file(csv_file_path)
        # print(image_meta)
        image_name_list = image_meta.keys()
        if index == 0:
            keypoint_name_and_list_dict = \
                    ({keypoint_xy : [] for keypoint_xy in KEYPOINT_XY_LIST})
            image_name_and_list_dict = \
                    ({image_name : copy.deepcopy(keypoint_name_and_list_dict) for image_name in image_name_list})
        for im_name in (image_name_and_list_dict):
            for ky_name in image_name_and_list_dict[im_name]:
                image_name_and_list_dict[im_name][ky_name].append(image_meta[im_name][ky_name])
    return image_name_and_list_dict

def write_output_csv_file(input_dict, meta):
    pass

def read_input_csv_file(csv_file_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        reshape_dict = {}
        for index, row in enumerate(reader):
            image_name = row["image"]
            del row["image"]
            reshape_dict[image_name] = row

        return reshape_dict

if __name__ == '__main__':
    global args
    args = parse_args()
    make_dir(args.output_folder_path)
    csv_file_list = os.listdir(args.csv_files_path)

    result = cancat_result(csv_file_list)
    with open(os.path.join(args.output_folder_path, "output.json"), "w") as json_file:
        json.dump(result, json_file)
    
    # print(image_name_and_list_dict)
        
    # dict1 = {'bookA': 2, 'bookB': 2, 'bookC': {"1":4, "2":3}}
    # dict2 = {'bookC': {"1":1, "2":2}, 'bookD': 4, 'bookE': 5}
    # dict3 = defaultdict(list)
    # for k, v in chain(dict1.items(), dict2.items()):
    #     dict3[k].append(v)
     
    # for k, v in dict3.items():
    #     print(k, v)

    # metas = get_image_meta()
