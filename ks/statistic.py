from .constants import logger, DB_OUTPUT
from tinydb import TinyDB, where

"""
    Table structure:
    +----------+-----------+-------------+
    | key_name | use_count | latest_time |
    +----------+-----------+-------------+
"""
_db = TinyDB(DB_OUTPUT)


def _record(key_info: list):
    key_name, latest_time = str(key_info[0]), key_info[1]
    db_key = _db.get(where("key_name") == key_name)
    use_count = 1 if db_key is None else db_key["use_count"] + 1
    doc = {"key_name": key_name, "use_count": use_count, "latest_time": latest_time}
    update_docs = _db.upsert(doc, where('key_name') == key_name)
    if not update_docs:
        logger.error(f"Upsert operation for {key_name} failed.")


def statistic(condition, key_queue):
    logger.debug("Statistic thread started.")
    while True:
        with condition:
            while key_queue.empty():
                condition.wait()
            key_info = key_queue.get(block=False)
            if key_info is None:
                break
            _record(key_info)
