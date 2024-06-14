import json
import os

def check_file(file_path):
    if not os.path.exists(file_path):
        print(f"{file_path} does not exist.")
        return False

    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            if not data:
                print(f"{file_path} is empty.")
                return False
            else:
                print(f"{file_path} contains data.")
                return True
        except json.JSONDecodeError:
            print(f"{file_path} is not a valid JSON file.")
            return False

if __name__ == "__main__":
    data_files = [
        'data/movies.json',
        'data/in_theater_movies.json',
        'data/tv_shows.json'
    ]

    all_files_valid = True

    for file_path in data_files:
        if not check_file(file_path):
            all_files_valid = False

    if all_files_valid:
        print("All data files are valid and contain data.")
    else:
        print("Some data files are missing, empty, or invalid.")