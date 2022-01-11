import os

from src.utils.display import display_video

if __name__ == "__main__":
    videos = os.listdir("dataset/test/detection/videos")
    display_video()

'''filepath="dataset/test/detection/videos/" + videos[4], scale=1'''