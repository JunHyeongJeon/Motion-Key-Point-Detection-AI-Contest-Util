import os
from tqdm import tqdm 
from _utils import(make_dir, KEYPOINT_XY_LIST, 
    write_output_csv_file, read_input_csv_file)
import argparse
import copy
import time
import numpy as np
import csv

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv_file_path', type=str, help=' CSV파일이 있는 경로',     
        default='./csv/Sun-Apr--4-22_13_14-2021_output-wrist_fix.csv')
    parser.add_argument('--output_folder_path', type=str, help='출력물이 있을 폴더',
        default='./csv_fix')
    return parser.parse_args()

def fix_palm_coordinate(csv_reader):
    output_list = []
    for index, row in enumerate(csv_reader):
        if float(row["left_elbow_y"]) < float(row["left_wrist_y"]):
            row["left_palm_y"] = float(row["left_palm_y"]) + 20
        else :
            row["left_palm_y"] = float(row["left_palm_y"]) - 20
        
        if float(row["right_elbow_y"]) < float(row["right_wrist_y"]):
            row["right_palm_y"] = float(row["right_palm_y"]) + 20
        else :
            row["right_palm_y"] = float(row["right_palm_y"]) - 20
        output_list.append(row)

    return output_list

if __name__ == '__main__':
    global args
    args = parse_args()
    make_dir(args.output_folder_path)

    csv_list = read_input_csv_file(args.csv_file_path)
    fix_list = fix_palm_coordinate(csv_list)
    write_output_csv_file(os.path.join(args.output_folder_path, "test.csv"), fix_list)
    print("Done!")