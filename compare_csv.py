import os
from _utils import(make_dir, write_output_csv_file, read_input_csv_file)
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--origin_csv', type=str, help='원본이 되는 CSV 파일',     
        default='./csv/Sun-Apr--4-22_13_14-2021_output-wrist_fix.csv')
    parser.add_argument('--target_csv', type=str, help='비교대상이 되는 CSV 파일',     
        default='./csv/Sun-Apr--4-22_13_14-2021_output-wrist_fix.csv')
    parser.add_argument('--output_folder_path', type=str, help='출력물이 있을 폴더',
        default='./csv_compare')
    return parser.parse_args()


if __name__ == '__main__':
    global args
    args = parse_args()
    make_dir(args.output_folder_path)