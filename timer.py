import datetime
import time


class Timer:
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time.time()
        now = datetime.datetime.now()
        print(f'Started at: {now}')
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = (time.time() - self.start)
        now = datetime.datetime.now()
        print(f"Ended at: {now}\n", self.message.format(elapsed_time))
