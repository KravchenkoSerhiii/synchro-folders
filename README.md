# Folder Synchronization Program

## Overview
This Python program synchronizes two folders: source and replica. The goal of the synchronization is to ensure that the replica folder maintains an identical copy of the source folder. The synchronization process is one-way, meaning that changes only flow from the source folder to the replica folder. Any new files in the source folder are copied to the replica, and files that no longer exist in the source are deleted from the replica.

## Features
- **One-Way Synchronization**: After each sync, the replica folder exactly mirrors the contents of the source folder.
- **Periodic Sync**: The synchronization process can be run periodically based on a user-defined interval.
- **Logging**: File operations (creation, copying, and deletion) are logged both to a file and to the console for easy monitoring.
- **Command-Line Arguments**: The paths to the source and replica folders, as well as the synchronization interval and log file path, are provided via command-line arguments.

## Usage
To run the program, use the following command:

        python sync_folders.py --source /path/to/source --replica /path/to/replica --interval 60 --log /path/to/logfile.log
        --source: Path to the source folder.
        --replica: Path to the replica folder.
        --interval: Synchronization interval in seconds.
        --log: Path to the log file for recording file operations.

## Example
To synchronize two folders every 60 seconds and log the operations to sync.log, you would run:

    python sync_folders.py --source ./source --replica ./replica --interval 60 --log ./sync.log

## Requirements
- Python 3.x
- No third-party libraries are required for folder synchronization.
