import logging
from pathlib import Path
import os

OUTPUT_DIR = ".ks"
LOG_OUTPUT = os.path.join(str(Path.home()), OUTPUT_DIR, "ks.log")
DB_OUTPUT = os.path.join(str(Path.home()), OUTPUT_DIR, "db", "key.json")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=LOG_OUTPUT,
    filemode="a",
)

logger = logging.getLogger("ks_logger")
