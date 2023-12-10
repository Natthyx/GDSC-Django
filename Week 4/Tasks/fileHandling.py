import os
import shutil
import time

def is_file_recent(file_path):
    current_time = time.time()
    file_stat = os.stat(file_path)
    creation_time = file_stat.st_ctime
    modification_time = file_stat.st_mtime
    time_diff = current_time - max(creation_time, modification_time)
    if time_diff <= 24 * 60 * 60:
        return True
    else:
        return False

def update_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'a') as file:
            timestamp = time.strftime("[%Y-%m-%d %H:%M:%S] ")
            file.write(timestamp)

def main():
    folder_name = "last_24hours"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    files = os.listdir()
    for file_name in files:
        file_path = os.path.join(os.getcwd(), file_name)
        if os.path.isfile(file_path) and is_file_recent(file_path):
            update_file(file_path)
            destination = os.path.join(os.getcwd(), folder_name, file_name)
            shutil.move(file_path, destination)

if __name__ == "__main__":
    main()