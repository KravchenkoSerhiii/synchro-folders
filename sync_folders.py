import os
import shutil
import time
import argparse


def sync_folders(source, replica, log_file):
    for root, dirs, files in os.walk(source):
        relative_path = os.path.relpath(root, source)
        replica_root = os.path.join(replica, relative_path)

        if not os.path.exists(replica_root):
            os.makedirs(replica_root)
            log_action(log_file, f"Created directory: {replica_root}")

        for file in files:
            source_file = os.path.join(root, file)
            replica_file = os.path.join(replica_root, file)

            if not os.path.exists(replica_file) or not files_are_equal(
                source_file, replica_file
            ):
                shutil.copy2(source_file, replica_file)
                log_action(log_file, f"Copied file: {source_file} to {replica_file}")

    for root, dirs, files in os.walk(replica):
        relative_path = os.path.relpath(root, replica)
        source_root = os.path.join(source, relative_path)

        if not os.path.exists(source_root):
            shutil.rmtree(root)
            log_action(log_file, f"Deleted directory: {root}")
            continue

        for file in files:
            replica_file = os.path.join(root, file)
            source_file = os.path.join(source_root, file)

            if not os.path.exists(source_file):
                os.remove(replica_file)
                log_action(log_file, f"Deleted file: {replica_file}")


def files_are_equal(file1, file2):
    if os.path.getsize(file1) != os.path.getsize(file2):
        return False

    with open(file1, "rb") as f1, open(file2, "rb") as f2:
        return f1.read() == f2.read()


def log_action(log_file, message):
    with open(log_file, "a") as log:
        log.write(f"{time.ctime()}: {message}\n")
    print(message)


def parse_arguments():
    parser = argparse.ArgumentParser(description="Folder Synchronizer")
    parser.add_argument("source", help="Path to the source folder")
    parser.add_argument("replica", help="Path to the replica folder")
    parser.add_argument("log", help="Path to the log file")
    parser.add_argument(
        "interval", type=int, help="Synchronization interval in seconds"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    while True:
        sync_folders(args.source, args.replica, args.log)
        time.sleep(args.interval)
