import os
import tarfile
import datetime

# Function to create a backup of a directory


def backup_directory(source_dir, backup_dir):
    # Check if source dir exists
    if not os.path.isdir(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"backup_{current_time}.tar.gz"
    backup_filepath = os.path.join(backup_dir, backup_filename)

    # create a tar.gz archive of the source directory
    with tarfile.open(backup_filepath, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

    print(f"Backup of '{source_dir}' created at '{backup_filepath}'.")


# Main Function
if __name__ == "__main__":
    source_dir = input("Enter the directory to back up: ")
    backup_dir = input("Enter the directory where backup should be saved: ")
    backup_directory(source_dir, backup_dir)
