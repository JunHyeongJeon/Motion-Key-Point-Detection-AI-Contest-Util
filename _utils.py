import os
import csv
import copy
import json

KEYPOINT_LIST = ["nose", "left_eye", "right_eye", "left_ear", "right_ear",\
                "left_shoulder", "right_shoulder", "left_elbow", "right_elbow",\
                "left_wrist", "right_wrist", "left_hip", "right_hip",\
                "left_knee", "right_knee", "left_ankle", "right_ankle",\
                "neck", "left_palm", "right_palm","spine2(back)","spine1(waist)",\
                "left_instep", "right_instep"]
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
CSV_HEAD = ["image", "nose_x", "nose_y", 
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
MY_TEST = "TEST"
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (0, 0, 255)

def make_dir(dir_name):
    try:
        if not(os.path.isdir(dir_name)):
            os.makedirs(os.path.join(dir_name))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!!!!!")
            raise

def get_csv_file_name(csv_full_path):
    return csv_full_path.split("\\")[-1].split(".")[0]

def get_row_data(row, target_keypoint):
    return [row[target_keypoint+"_x"], row[target_keypoint+"_y"]]

def set_coordinate_as_int(image_keypoint):
    return (int(float(image_keypoint[0])), int(float(image_keypoint[1])))


def is_xy_list_coordinate_exist(coordinate):
    if (coordinate[0] == 0) and (coordinate[1] == 0):
        return True
    else:
        return False 

def write_output_csv_file(csv_file_path, data):
    with open(csv_file_path, "w", newline="") as csvfile:
        fieldnames = CSV_HEAD 
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()     
        for element in data:
            writer.writerow(element)

def write_output_json_file(json_file_path, data):
    with open(json_file_path, "w") as json_file:
        json.dump(data, json_file)

def write_list_to_txt_file(txt_file_path, data):
    with open(txt_file_path, "w") as txt_file:
        txt_file.write('\n'.join(data))

def read_input_csv_file(csv_file_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)