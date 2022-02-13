import argparse
import os
from pprint import pprint

from src.utils.display import stream

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--detector",
        default="RetinaFace",
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
    parser.add_argument(
        "-t",
        "--track-face",
        action="store_true",
        default=False,
        help="track extracted faces from video",
    )
    parser.add_argument(
        "-r",
        "--recognize-face",
        action="store_true",
        default=False,
        help="recognize faces in the video",
    )
    parser.add_argument(
        "-c",
        "--webcam",
        action="store_true",
        default=False,
        help="recognize faces in the video",
    )

    args = parser.parse_args()
    videos = os.listdir("data/test-videos/")
    pprint(args)
    if args.align_face is True and args.extract_face is False:
        print("You need to extract faces first. Alignment disabled for now.")
    
    videopath = None if args.webcam else "data/test-videos/" + videos[8]

    stream(
        filepath=videopath,
        model=args.detector,
        extract_face=args.extract_face,
        align_face=args.align_face,
        track_face=args.track_face,
        recognize_face=args.recognize_face,
        padding=0,
    )

