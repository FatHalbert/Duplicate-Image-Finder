import os
from collections import defaultdict

# List of folder names to exclude from search
folders_to_exclude = ["Homework", "NotHomework"]

def find_duplicate_pictures(path):
    # Counter for total files searched
    files_searched = 0
    # Counter for total duplicates found
    duplicates_found = 0
    
    # Dictionary to store file hashes and their corresponding file paths
    file_hashes = defaultdict(list)

    # Recursively search through all files and directories in the given path
    for root, dirs, files in os.walk(path):
        # Exclude any directories that match the names in the folders_to_exclude list
        dirs[:] = [d for d in dirs if not any(folder in d for folder in folders_to_exclude)]

        for file in files:
            # Check if file is an image file (based on file extension)
            if file.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
                files_searched += 1
                # Open the file and calculate its hash
                with open(os.path.join(root, file), "rb") as f:
                    file_hash = hash(f.read())
                # Add the file path to the list of files with the same hash
                file_hashes[file_hash].append(os.path.join(root, file))
    
    # Iterate through the dictionary of file hashes
    for file_hash, file_list in file_hashes.items():
        # Check if there is more than one file with the same hash
        if len(file_list) > 1:
            duplicates_found += 1
            print("Duplicate files:")
            for file in file_list:
                print(file)
    
    # Print total number of files searched and total number of duplicates found
    print(f"Total files searched: {files_searched}")
    print(f"Total duplicates found: {duplicates_found}")

find_duplicate_pictures("C:\\")
