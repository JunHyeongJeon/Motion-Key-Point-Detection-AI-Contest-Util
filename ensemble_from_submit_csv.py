#-*- coding:utf-8 -*-
import os
from tqdm import tqdm 
import csv
from _utils import *
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv_files_path', type=str, help=' CSV파일들이 있는 경로',     
        default='C:\\Users\\Jun\\Downloads\\csv')
    parser.add_argument('--output_folder_path', type=str, help='출력물이 있을 폴더',
        default='.\\ensemble')
    return parser.parse_args()

if __name__ == '__main__':
    pass