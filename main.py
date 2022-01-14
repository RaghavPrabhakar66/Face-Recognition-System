import argparse
import os
from pprint import pprint

from src.utils.display import display_video_motpy

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--detector",
        default="Mediapipe",
        help="model used for face detection",
    )
    parser.add_argument(
        "-e",
        "--extract-face",
        action="store_true",
        default=False,
        help="extract faces from video",
    )
    parser.add_argument(
        "-a",
        "--align-face",
        action="store_true",
        default=False,
        help="align extracted faces from video",
    )
    args = parser.parse_args()
    videos = os.listdir("dataset/test/detection/videos")
    pprint(args)
    display_video_motpy(
        filepath=None,
        model=args.detector,
        extract_face=args.extract_face,
        align_face=args.align_face,
    )

'''"dataset/test/detection/videos/" + videos[4]'''