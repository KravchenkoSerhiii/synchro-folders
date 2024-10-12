import argparse
import time


def parse_arguments():
    parser = argparse.ArgumentParser(description="Synchronize two folders")

    parser.add_argument("source", type=str, help="Path to the source folder")

    parser.add_argument("replica", type=str, help="Path to the replica folder")

    parser.add_argument(
        "--interval",
        type=int,
        default=60,
        help="Synchronization interval in seconds",
    )

    parser.add_argument(
        "--log",
        type=str,
        default="sync.log",
        help="Path to the log file",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
