import datetime
import subprocess

def log_commit():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("tracker.txt", "a") as f:
        f.write(f"Committed on {now}\n")

    subprocess.run(["git", "add", "tracker.txt"])
    subprocess.run(["git", "commit", "-m", f"Daily commit on {now}"])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    log_commit()