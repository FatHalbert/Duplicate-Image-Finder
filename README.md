Features
Finds and prints duplicate picture files in a given directory and its subdirectories
Excludes files in folders named "Homework" or "NotHomework" from the search
Prints the total number of files searched and the total number of duplicates found

How to use
Run the script by calling find_duplicate_pictures(path) function and passing the path of the directory to search for duplicates in as an argument.
The script will search the given directory and its subdirectories for picture files with the file extensions .jpg, .jpeg, .png, .bmp, and .gif.
For each file found, the script reads the file, computes its hash, and appends the file's path to the value list associated with the file's hash in the defaultdict.
After all files have been processed, the script iterates through the defaultdict and for each key with a value list length greater than one, it prints the duplicate file paths associated with that key.
The script will print the total number of files searched and the total number of duplicates found to help troubleshoot.

Requirements
Python 3
os module
collections module

Notes
The script does not delete or move the duplicate files, it only prints the file paths. It is the user's responsibility to review and handle the duplicate files as needed.
The script reads the entire file into memory to compute the hash, so it may not be suitable for very large files or directories with many files.
