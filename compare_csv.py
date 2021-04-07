import os
from _utils import(make_dir, write_output_csv_file, 
    read_input_csv_file, KEYPOINT_XY_LIST, current_time,
    write_list_to_txt_file)
import argparse
import copy 
from collections import Counter

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--origin_csv', type=str, help='원본이 되는 CSV 파일',     
        default='./csv/Sun-Apr--4-22_13_14-2021_output.csv')
    parser.add_argument('--target_csv', type=str, help='비교대상이 되는 CSV 파일',     
        default='./csv/Sun-Apr--4-22_13_14-2021_output-wrist_fix.csv')
    parser.add_argument('--output_folder_path', type=str, help='출력물이 있을 폴더',
        default='./csv_compare')
    return parser.parse_args()

def compare_two_list(csv_list1, csv_list2):
    origin_csv_list = copy.deepcopy(csv_list1)
    for row1 in origin_csv_list:
        for row2 in csv_list2:
            if row1["image"] == row2["image"]:
                for keypoint in KEYPOINT_XY_LIST:
                    row1[keypoint] = float(row1[keypoint]) - float(row2[keypoint])
            else : 
                continue

    return origin_csv_list

if __name__ == '__main__':
    global args
    args = parse_args()
    make_dir(args.output_folder_path)
    csv_list1 = read_input_csv_file(args.origin_csv)
    csv_list2 = read_input_csv_file(args.target_csv)
    csv_meta = [args.origin_csv.split("/")[-1], args.target_csv.split("/")[-1]]
    result = compare_two_list(csv_list1, csv_list2)
    write_list_to_txt_file(os.path.join(args.output_folder_path, current_time()+"_compare.txt"), csv_meta)
    write_output_csv_file(os.path.join(args.output_folder_path, current_time()+"_compare.csv"), result)