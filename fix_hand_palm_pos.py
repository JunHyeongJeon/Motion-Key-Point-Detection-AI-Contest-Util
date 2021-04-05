import os
from tqdm import tqdm 
import csv
from _utils import make_dir
import argparse
from itertools import chain
from collections import defaultdict
import json
import copy
import time
import numpy as np


KEYPOINT_XY_LIST = ["image","nose_x", "nose_y", 
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
    parser.add_argument('--csv_file_path', type=str, help=' CSV파일이 있는 경로',     
        default='./csv/Sun-Apr--4-22_13_14-2021_output-wrist_fix.csv')
    parser.add_argument('--output_folder_path', type=str, help='출력물이 있을 폴더',
        default='./csv_fix')
    return parser.parse_args()


def read_input_csv_file(csv_file_path):
    output_list = []
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for index, row in enumerate(reader):
            if float(row["left_elbow_y"]) < float(row["left_wrist_y"]):
                row["left_palm_y"] = float(row["left_palm_y"]) + 20
            else :
                row["left_palm_y"] = float(row["left_palm_y"]) - 20
            
            if float(row["right_elbow_y"]) < float(row["right_wrist_y"]):
                row["right_palm_y"] = float(row["right_palm_y"]) + 20
            else :
                row["right_palm_y"] = float(row["right_palm_y"]) - 20


            output_list.append(row)

        with open(os.path.join(args.output_folder_path, "test.csv"), "w", newline="") as csvfile:
            fieldnames = copy.deepcopy(KEYPOINT_XY_LIST)
        
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()     
            for element in output_list:
                writer.writerow(element)


def write_output_csv_file(csv_file_path, data):
    with open(csv_file_path, "w", newline="") as csvfile:
        fieldnames = copy.deepcopy(KEYPOINT_XY_LIST)
        fieldnames.insert(0, "image")

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()     
        for element in data:
            writer.writerow(element)


if __name__ == '__main__':
    global args
    args = parse_args()
    make_dir(args.output_folder_path)

    output = read_input_csv_file(args.csv_file_path)

    print("Done!")