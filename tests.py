import unittest
import os
import shutil
from sync_folders import sync_folders


class TestFolderSync(unittest.TestCase):

    def setUp(self):
        self.source_folder = "test_source"
        self.replica_folder = "test_replica"
        self.log_file = "sync.log"

        os.makedirs(self.source_folder, exist_ok=True)
        os.makedirs(self.replica_folder, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.source_folder)
        shutil.rmtree(self.replica_folder)
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_file_copy(self):
        test_file = os.path.join(self.source_folder, "test.txt")
        with open(test_file, "w") as f:
            f.write("This is a test file")

        sync_folders(self.source_folder, self.replica_folder, self.log_file)

        copied_file = os.path.join(self.replica_folder, "test.txt")
        self.assertTrue(os.path.exists(copied_file))
        with open(copied_file, "r") as f:
            self.assertEqual(f.read(), "This is a test file")

    def test_file_deletion(self):
        test_file_replica = os.path.join(self.replica_folder, "file.txt")
        with open(test_file_replica, "w") as f:
            f.write("This file should be deleted")

        sync_folders(self.source_folder, self.replica_folder, self.log_file)

        self.assertFalse(os.path.exists(test_file_replica))

    def test_file_update(self):
        test_file = os.path.join(self.source_folder, "test.txt")
        with open(test_file, "w") as f:
            f.write("Initial content")

        sync_folders(self.source_folder, self.replica_folder, self.log_file)

        with open(test_file, "w") as f:
            f.write("Updated content")

        sync_folders(self.source_folder, self.replica_folder, self.log_file)

        copied_file = os.path.join(self.replica_folder, "test.txt")
        with open(copied_file, "r") as f:
            self.assertEqual(f.read(), "Updated content")


if __name__ == "__main__":
    unittest.main()
