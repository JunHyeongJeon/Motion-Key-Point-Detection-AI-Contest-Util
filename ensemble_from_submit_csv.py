#-*- coding:utf-8 -*-
import os
from tqdm import tqdm 
from _utils import (make_dir, write_output_csv_file, 
                    write_output_json_file, write_list_to_txt_file,
                    read_input_csv_file, KEYPOINT_XY_LIST, current_time)
import argparse
import copy
import numpy as np


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv_files_path', type=str, help=' CSV파일들이 있는 경로',     
        default='./csv')
    parser.add_argument('--output_folder_path', type=str, help='출력물이 있을 폴더',
        default='./ensemble')
    parser.add_argument('--ensemble', type=str, help='어떤 방식으로 앙상블 [median, average]',
        default='median')
    return parser.parse_args()

def ensemble_algorithm(in_data):
    temp = copy.deepcopy(in_data)
    np_data = np.array(temp)
    int_np_data = np_data.astype(np.float64)
    
    result = 0
    if args.ensemble == "median":
        result = np.median(int_np_data)
    elif args.ensemble == "average":
        result = np.average(int_np_data)
    return result 

def ensemble(annotations):  
    ensemble_result = copy.deepcopy(annotations)
    for image_name in tqdm(annotations):
        for keypoint in KEYPOINT_XY_LIST:
            ensemble_result[image_name][keypoint] = \
                ensemble_algorithm(annotations[image_name][keypoint])

    return ensemble_result 

def reshape_ensemble_result_to_output_csv(ensemble_result):
    reshape_output = []
    for image_name in ensemble_result:
        temp = ensemble_result[image_name]
        temp["image"] = image_name
        reshape_output.append(temp)
        # for keypoint in KEYPOINT_XY_LIST:

    return reshape_output

def reshape_csv_list_for_cancat_input(csv_list_object):
    reshape_dict = {}
    for index, row in enumerate(csv_list_object):
        image_name = row["image"]
        del row["image"]
        reshape_dict[image_name] = row

    return reshape_dict

def cancat(csv_file_list):
    image_name_and_list_dict = {}

    for index, csv_file in enumerate(tqdm(csv_file_list)):          
        csv_file_path = os.path.join(args.csv_files_path, csv_file)
        csv_list = read_input_csv_file(csv_file_path)
        image_meta = reshape_csv_list_for_cancat_input(csv_list)

        image_name_list = image_meta.keys()
        if index == 0:
            keypoint_name_and_list_dict = \
                    ({keypoint_xy : [] for keypoint_xy in KEYPOINT_XY_LIST})
            image_name_and_list_dict = \
                    ({image_name : copy.deepcopy(keypoint_name_and_list_dict) for image_name in image_name_list})
        for im_name in (image_name_and_list_dict):
            for ky_name in image_name_and_list_dict[im_name]:
                if len(image_meta[im_name][ky_name]) == 0:
                    continue
                if float(image_meta[im_name][ky_name]) > 0: 
                    image_name_and_list_dict[im_name][ky_name].append(image_meta[im_name][ky_name])
    return image_name_and_list_dict
  


if __name__ == '__main__':
    global args
    args = parse_args()
    make_dir(args.output_folder_path)
    csv_file_list = os.listdir(args.csv_files_path)
  
    cancat_result = cancat(csv_file_list)
    write_list_to_txt_file(os.path.join(args.output_folder_path, current_time()+"_meta.txt"), csv_file_list)
    write_output_json_file(os.path.join(args.output_folder_path, current_time()+"_cancat.json"), cancat_result)
    
    print("Ensemble processing...")
    ensemble_result = ensemble(cancat_result)

    print("Output file processing...")
    write_output_json_file(os.path.join(args.output_folder_path, current_time()+"_ensemble.json"), ensemble_result)
    
    reshape_result = reshape_ensemble_result_to_output_csv(ensemble_result)
    write_output_csv_file(os.path.join(args.output_folder_path, current_time()+ "_output.csv"), reshape_result)
    print("Done!")