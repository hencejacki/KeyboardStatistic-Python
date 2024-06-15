from pynput.keyboard import Listener, Key, KeyCode
from .constants import logger
from .statistic import statistic
from queue import Queue
from threading import Thread, Condition
import time

key_queue = Queue(20)
condition = Condition()


def on_press(key: Key | KeyCode | None):
    if key is None:
        logger.error("None of key.")
        return False

    key = key.name if type(key) is Key else key

    # Enqueue
    with condition:
        key_queue.put([key, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())])
        condition.notify()


def entry():
    with Listener(on_press=on_press) as listener:
        # Start a statistic thread
        t = Thread(target=statistic, args=[condition, key_queue])
        t.start()
        t.join()
        listener.join()
