import os
def list_all_files(path):
    return [os.path.relpath(os.path.join(root, file), path) for root, _, files in os.walk(path) for file in files]
def list_all_directories(path):
    return [os.path.relpath(os.path.join(root, directory), path) for root, dirs, _ in os.walk(path) for directory in dirs]
path = "/path/to/your/directory"
print("All Directories in the specified path:")
print("\n".join(list_all_directories(path)))
print("\nAll Files in the specified path:")
print("\n".join(list_all_files(path)))

#2 Task Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path 
import os
def check_path_access(path):
    return {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }
path = "/path/to/your/directory"
access_info = check_path_access(path)

#3 Task Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os
def test_path(path):
    if os.path.exists(path):
        print("Path exists.")
        print(f"Filename: {os.path.basename(path)}")
        print(f"Directory: {os.path.dirname(path)}")
    else:
        print("Path does not exist.")
test_path("/path/to/your/file.txt")

#4 Task Write a Python program to count the number of lines in a text file.
def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"Number of lines in {file_path}: {line_count}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
file_path = input("Enter the path to the text file: ")
count_lines(file_path)

#5 Task Write a Python program to write a list to a file.
def write_list_to_file():
    try:
        file_path = input("Enter the path to the file: ")
        my_list = input("Enter the list elements separated by space: ").split()
        with open(file_path, 'w') as file:
            file.write('\n'.join(my_list))
        print(f"The list has been successfully written to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
write_list_to_file()

#6 Task Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    with open(f"{letter}.txt", 'w') as f: f.write(f"This is file {letter}.txt.")

#7 Task Write a Python program to copy the contents of a file to another file
def copy_file(source, destination):
    with open(source, 'r') as s, open(destination, 'w') as d: d.write(s.read())
copy_file("source.txt", "destination.txt")

#8 Task Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os
def delete_file(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"File {file_path} has been deleted.")
    else:
        print(f"Cannot delete file {file_path}. Check access.")
file_path = input("Enter the path of the file to delete: ")
delete_file(file_path)