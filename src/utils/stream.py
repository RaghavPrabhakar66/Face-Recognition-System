import time
from queue import Queue
from threading import Thread

import cv2


class Stream:
    def __init__(self, filepath, function=None, queue_size=128):
        """[summary]

        Args:
            filepath (str): Absolute path of video file.
            function (object, optional): Defaults to None.
            queue_size (int, optional): Defaults to 128.
        """
        self.stream = cv2.VideoCapture(filepath)
        self.function = function
        self.frame_queue = Queue(maxsize=queue_size)
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True

    def start(self):
        self.thread.start()
        return self

    def update(self):
        if self.frame_queue.full():
            return

        while True:
            ret, frame = self.stream().read()
            if not ret:
                break
            self.frame_queue.put(frame)
            time.sleep(0.01)
        self.stream().release()
