import os
import csv

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

KEYPOINT_LIST = ["nose", "left_eye", "right_eye", "left_ear", "right_ear",\
                "left_shoulder", "right_shoulder", "left_elbow", "right_elbow",\
                "left_wrist", "right_wrist", "left_hip", "right_hip",\
                "left_knee", "right_knee", "left_ankle", "right_ankle",\
                "neck", "left_palm", "right_palm","spine2(back)","spine1(waist)",\
                "left_instep", "right_instep"]



MY_TEST = "TEST"
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (0, 0, 255)