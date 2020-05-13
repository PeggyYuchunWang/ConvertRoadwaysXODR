from src.open_drive_parser import OpenDriveParser
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--filename', default="test_data/Town02.xodr")
    args = parser.parse_args()
    odp = OpenDriveParser()
    odp.parse_file(args.filename)
