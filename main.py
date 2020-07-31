from pyxodr.parser.open_drive_parser import OpenDriveParser
import argparse
from os import listdir
from os.path import isfile, join

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--filename', default="test_data/CarlaExs/Town02.xodr")
    parser.add_argument('--folder', default="test_data/CarlaExs/")
    args = parser.parse_args()
    odp = OpenDriveParser()
    onlyfiles = [
        f for f in listdir(args.folder) if isfile(join(args.folder, f))
    ]
    if ".DS_Store" in onlyfiles:
        onlyfiles.remove(".DS_Store")
    odp.parse_file(args.filename)
    #print(odp.data.roads["1"].lanes.lane_sections[0])
    for f in onlyfiles:
        odp.parse_file(args.folder+f)
