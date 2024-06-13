import os
from pathlib import Path

OUTPUT_DIR = ".ks"
PID_FILE = "ks.pid"


# Init directory of statistic report
def init_dir():
    output_path = os.path.join(str(Path.home()), OUTPUT_DIR)
    pid_path = os.path.join(str(Path.home()), OUTPUT_DIR, PID_FILE)
    monthly_out = os.path.join(output_path, "monthly")
    biannually_out = os.path.join(output_path, "biannually")
    yearly_out = os.path.join(output_path, "yearly")
    try:
        if not os.path.exists(output_path):
            for dir in [output_path, monthly_out, biannually_out, yearly_out]:
                os.mkdir(dir)
        with open(pid_path, "w") as f:
            f.write(str(os.getpid()))
    except OSError:
        print("Create output directory failed.")


init_dir()
